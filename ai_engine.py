import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def transcribe_audio(audio_file_path):
    """Transcribe audio to text using Whisper."""
    try:
        with open(audio_file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file,
                response_format="text"
            )
        return transcript
    except Exception as e:
        print(f"Error in transcription: {e}")
        return None

def generate_teacher_response(system_prompt, user_message, chat_history=None):
    """Generate response from GPT-4o."""
    if chat_history is None:
        chat_history = []
        
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(chat_history)
    messages.append({"role": "user", "content": user_message})
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in LLM: {e}")
        return "I'm sorry, I have a little problem right now."

def text_to_speech(text, output_file_path="response.mp3"):
    """Convert text to speech using OpenAI TTS."""
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="nova", # Nova is a gentle voice suitable for kids
            input=text
        )
        response.stream_to_file(output_file_path)
        return output_file_path
    except Exception as e:
        print(f"Error in TTS: {e}")
        return None
