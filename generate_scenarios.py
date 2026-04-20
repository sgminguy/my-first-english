import json

scenarios_data = {
  "scenarios": [
    {"id": "school", "title": "학교에서 친구 만나기 🏫", "desc": "학교에서 만난 친구에게 반갑게 인사해 보세요.", "role": "classmate", "targets": ["Hello, how are you?", "I am fine, thank you.", "Let's play together!"]},
    {"id": "shopping", "title": "마트에서 물건 사기 🍎", "desc": "마트에서 사과를 사고 싶다고 말해 보세요.", "role": "cashier at a grocery store", "targets": ["Hello, can I have an apple?", "How much is it?", "Here you go."]},
    {"id": "restaurant", "title": "식당에서 음식 주문하기 🍔", "desc": "식당에서 햄버거와 주스를 주문해 보세요.", "role": "waiter at a restaurant", "targets": ["I am hungry.", "I want a hamburger.", "Can I have some juice, please?"]},
    {"id": "park", "title": "공원에서 친구와 놀기 ⚽", "desc": "공원에서 친구에게 같이 축구를 하자고 말해 보세요.", "role": "friend at the park", "targets": ["What are you doing?", "Let's play soccer.", "Kick the ball to me!"]},
    {"id": "home", "title": "집에서 부모님과 대화하기 🏠", "desc": "집에 돌아와서 엄마에게 배고프다고 말해 보세요.", "role": "loving mother at home", "targets": ["Mom, I am home!", "I am very hungry.", "What is for dinner?"]},
    {"id": "hospital", "title": "병원에서 의사 선생님 만나기 🩺", "desc": "병원에 가서 머리가 아프다고 말해 보세요.", "role": "friendly doctor", "targets": ["Hello, doctor.", "My head hurts.", "Thank you, doctor."]},
    {"id": "library", "title": "도서관에서 책 빌리기 📚", "desc": "도서관 사서 선생님께 책을 빌리고 싶다고 말해보세요.", "role": "librarian", "targets": ["I want to read a book.", "Can I borrow this?", "Thank you."]},
    {"id": "zoo", "title": "동물원에서 동물 구경하기 🦁", "desc": "동물원에서 원숭이와 사자를 보며 이야기해보세요.", "role": "friend at the zoo", "targets": ["Look at the monkey!", "It is very funny.", "Where is the lion?"]},
    {"id": "toy_store", "title": "장난감 가게에서 장난감 고르기 🧸", "desc": "가게에서 로봇 장난감이 마음에 든다고 말해보세요.", "role": "toy store clerk", "targets": ["Wow, look at this toy.", "I like this robot.", "I want to buy it."]},
    {"id": "birthday", "title": "생일 파티 축하해주기 🎂", "desc": "친구의 생일 파티에 가서 축하 인사를 건네보세요.", "role": "friend having a birthday", "targets": ["Happy birthday to you!", "This is a present for you.", "Let's eat the cake!"]},
    {"id": "amusement_park", "title": "놀이공원에서 놀이기구 타기 🎢", "desc": "놀이공원에서 롤러코스터를 타자고 말해보세요.", "role": "friend at the amusement park", "targets": ["This is so fun!", "Let's ride the rollercoaster.", "I am excited."]},
    {"id": "beach", "title": "바닷가에서 모래놀이 하기 🏖️", "desc": "해변에서 모래성을 만들자고 제안해보세요.", "role": "friend at the beach", "targets": ["The sea is beautiful.", "Let's make a sandcastle.", "The water is cold."]},
    {"id": "morning", "title": "아침에 일어나서 인사하기 🌅", "desc": "아침에 일어났을 때 아빠에게 인사해보세요.", "role": "loving father in the morning", "targets": ["Good morning, Dad.", "Did you sleep well?", "I am ready for school."]},
    {"id": "bedtime", "title": "자기 전에 밤 인사하기 🌙", "desc": "잠들기 전에 엄마에게 잘 자라고 인사해보세요.", "role": "loving mother at bedtime", "targets": ["I am sleepy.", "Good night, Mom.", "Sweet dreams."]},
    {"id": "bus_stop", "title": "버스 정류장에서 버스 타기 🚌", "desc": "친구와 함께 학교 버스를 기다리며 이야기해보세요.", "role": "friend at the bus stop", "targets": ["Here comes the bus.", "Let's get on.", "Let's sit together."]},
    {"id": "movie", "title": "영화관에서 티켓 사기 🍿", "desc": "영화관 직원에게 팝콘과 영화 티켓을 사보세요.", "role": "movie theater clerk", "targets": ["Two tickets, please.", "I want popcorn too.", "Enjoy the movie!"]},
    {"id": "ice_cream", "title": "아이스크림 가게에서 맛 고르기 🍦", "desc": "아이스크림 가게에서 딸기 맛을 고르고 싶다고 해보세요.", "role": "ice cream shop worker", "targets": ["I want strawberry ice cream.", "It looks delicious.", "Thank you very much."]},
    {"id": "art_class", "title": "미술 시간에 그림 그리기 🎨", "desc": "미술 시간에 친구에게 내 그림을 보여주세요.", "role": "classmate in art class", "targets": ["Look at my picture.", "I drew a house.", "Your picture is pretty too."]},
    {"id": "music_class", "title": "음악 시간에 노래 부르기 🎵", "desc": "음악 시간에 피아노 치는 친구와 대화해보세요.", "role": "classmate in music class", "targets": ["Let's sing a song.", "You play the piano well.", "It sounds great."]},
    {"id": "gym_class", "title": "체육 시간에 달리기 하기 🏃", "desc": "체육 시간에 친구와 함께 달리기를 해보세요.", "role": "classmate in gym class", "targets": ["Let's run fast.", "You are so fast!", "I am tired now."]},
    {"id": "playground", "title": "놀이터에서 미끄럼틀 타기 🛝", "desc": "놀이터에서 친구와 미끄럼틀을 타자고 하세요.", "role": "friend at the playground", "targets": ["Let's go to the playground.", "I want to ride the slide.", "It's my turn!"]},
    {"id": "pet_shop", "title": "동물병원/펫샵에서 강아지 보기 🐶", "desc": "귀여운 강아지를 보며 이야기해보세요.", "role": "pet shop owner", "targets": ["Wow, a cute puppy!", "Can I touch it?", "It is so soft."]},
    {"id": "lost_found", "title": "분실물 센터에서 가방 찾기 🎒", "desc": "선생님께 파란색 가방을 잃어버렸다고 말해보세요.", "role": "helpful teacher at the lost and found", "targets": ["Excuse me, teacher.", "I lost my bag.", "It is a blue bag."]},
    {"id": "supermarket", "title": "슈퍼마켓에서 우유 사기 🥛", "desc": "우유가 어디 있는지 직원에게 물어보세요.", "role": "supermarket worker", "targets": ["Where is the milk?", "I found it.", "Let's go pay."]},
    {"id": "grandparents", "title": "할머니 댁 방문하기 👵", "desc": "할머니 댁에 가서 할머니께 반갑게 인사해보세요.", "role": "loving grandmother", "targets": ["Hello, Grandma!", "I missed you so much.", "This food is yummy."]},
    {"id": "swimming", "title": "수영장에서 수영하기 🏊", "desc": "수영장에서 친구와 함께 물놀이를 해보세요.", "role": "friend at the swimming pool", "targets": ["Let's jump into the water.", "Can you swim?", "It is so cool."]},
    {"id": "camping", "title": "캠핑장에서 모닥불 피우기 ⛺", "desc": "가족과 캠핑을 가서 별을 구경해보세요.", "role": "father at the camping trip", "targets": ["The stars are beautiful.", "Let's eat marshmallows.", "I love camping."]},
    {"id": "museum", "title": "박물관에서 공룡 화석 보기 🦖", "desc": "박물관에서 큰 공룡 화석을 보며 이야기하세요.", "role": "friend at the museum", "targets": ["Look at the dinosaur!", "It is very big.", "This is awesome."]},
    {"id": "aquarium", "title": "아쿠아리움에서 상어 보기 🦈", "desc": "아쿠아리움에서 여러 가지 물고기를 구경해보세요.", "role": "friend at the aquarium", "targets": ["Wow, look at the fish.", "Is that a shark?", "They swim fast."]},
    {"id": "halloween", "title": "할로윈 날 사탕 받기 🎃", "desc": "이웃집 문을 두드리고 사탕을 달라고 해보세요.", "role": "neighbor giving out candy", "targets": ["Trick or treat!", "Give me some candy.", "Happy Halloween!"]}
  ]
}

formatted_scenarios = []
for s in scenarios_data["scenarios"]:
    prompt = f"You are an AI English teacher role-playing as a {s['role']}. The user is an 8-year-old child. First, correct the user's English if there are any grammatical errors, in a very kind and encouraging way using Korean. Then, respond to the user's message in English. Use very simple English words. Keep your English response to 1 or 2 short sentences."
    formatted_scenarios.append({
        "id": s["id"],
        "title": s["title"],
        "description": s["desc"],
        "system_prompt": prompt,
        "target_sentences": s["targets"]
    })

with open("scenarios.json", "w", encoding="utf-8") as f:
    json.dump({"scenarios": formatted_scenarios}, f, ensure_ascii=False, indent=2)

print("Created 30 scenarios successfully!")
