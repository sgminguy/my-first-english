import streamlit as st
import json
import os
# Native audio input will be used
from ai_engine import transcribe_audio, generate_teacher_response, text_to_speech
from scoring import calculate_pronunciation_score
import time

# Load scenarios
def load_scenarios():
    with open("scenarios.json", "r", encoding="utf-8") as f:
        return json.load(f)["scenarios"]

scenarios = load_scenarios()

# UI Setup
st.set_page_config(page_title="초등학생 영어 친구", page_icon="🏫", layout="centered")

st.title("🌟 AI 영어 친구와 대화해요!")

# Session state initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_target_idx" not in st.session_state:
    st.session_state.current_target_idx = 0
if "current_scenario" not in st.session_state:
    st.session_state.current_scenario = scenarios[0]["title"]

# Scenario Selection
st.sidebar.header("어떤 상황에서 얘기할까요?")
scenario_names = [s["title"] for s in scenarios]
selected_title = st.sidebar.selectbox("상황 선택", scenario_names)

# Reset if scenario changes
if selected_title != st.session_state.current_scenario:
    st.session_state.current_scenario = selected_title
    st.session_state.current_target_idx = 0
    st.session_state.chat_history = []

selected_scenario = next(s for s in scenarios if s["title"] == selected_title)

st.subheader(f"📍 {selected_scenario['title']}")
st.write(selected_scenario['description'])

# Target sentence display
targets = selected_scenario["target_sentences"]
current_idx = st.session_state.current_target_idx

if current_idx < len(targets):
    target_sentence = targets[current_idx]
    st.info(f"💡 이렇게 말해볼까요? **\"{target_sentence}\"**")
else:
    st.success("🎉 모든 대화 연습을 완료했어요! 다른 상황을 선택해보세요.")
    target_sentence = None

# Audio Recording
audio_value = st.audio_input("🎤 마이크 버튼을 누르고 말해보세요!")

if audio_value:
    # Save audio temporarily
    audio_file_path = "temp_audio.wav"
    with open(audio_file_path, "wb") as f:
        f.write(audio_value.getvalue())
        
    with st.spinner("듣고 있어요... 🎧"):
        # 1. STT
        transcript = transcribe_audio(audio_file_path)
        
        if transcript:
            user_text = transcript
            st.write(f"👦 나: {user_text}")
            
            # 2. Pronunciation Score
            if target_sentence:
                score = calculate_pronunciation_score(target_sentence, user_text)
                st.session_state.score += score
                
                if score >= 70:
                    st.success(f"🌟 참 잘했어요! 발음 점수: {score}점")
                    st.session_state.current_target_idx += 1
                else:
                    st.warning(f"👍 괜찮아요, 다시 한번 해볼까요? 발음 점수: {score}점")
            
            # 3. LLM (AI Teacher)
            system_prompt = selected_scenario["system_prompt"]
            
            # AI에게 사용자가 원래 해야 했던 정답 문장을 알려주어 더 정확한 피드백을 유도합니다.
            if target_sentence:
                feedback_instruction = f"\n\nThe user was trying to say: '{target_sentence}'. The user actually said: '{user_text}'. If the user's sentence is wrong or grammar is incorrect, kindly explain in Korean how to fix it. Then, answer the user's message in English (1-2 simple sentences) to continue the roleplay."
                current_system_prompt = system_prompt + feedback_instruction
            else:
                current_system_prompt = system_prompt
                
            formatted_history = [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.chat_history]
            
            ai_response = generate_teacher_response(current_system_prompt, user_text, formatted_history)
            st.info(f"🤖 AI 선생님의 답변 및 교정:\n\n{ai_response}")
            
            # 4. TTS
            tts_file = text_to_speech(ai_response)
            if tts_file:
                st.success("🔊 아래의 재생 버튼(▶)을 눌러 AI 선생님의 진짜 목소리를 들어보세요! (스마트폰에서는 자동 재생이 차단될 수 있습니다)")
                
                # HTML audio for desktop autoplay
                audio_html = f"""
                    <audio autoplay="true">
                    <source src="{tts_file}" type="audio/mp3">
                    </audio>
                    """
                st.markdown(audio_html, unsafe_allow_html=True)
                
                # Visible audio widget for mobile users
                st.audio(tts_file, format="audio/mp3")
            
            # Save history
            st.session_state.chat_history.append({"role": "user", "content": user_text})
            st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
            
            # Cleanup temp file
            try:
                os.remove(audio_file_path)
            except:
                pass
            

# Score Display
st.sidebar.markdown("---")
st.sidebar.markdown(f"### 🏆 획득 포인트: {st.session_state.score}점")

# Chat History Display
with st.expander("지난 대화 보기"):
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"**나:** {msg['content']}")
        else:
            st.markdown(f"**AI 친구:** {msg['content']}")
