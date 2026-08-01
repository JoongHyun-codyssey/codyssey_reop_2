from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quiz_list = [
            {
                "id": 1,
                "question": "대한민국의 수도는?",
                "choices": ["부산", "인천", "서울", "대전"],
                "answer": "3"
            },
            {
                "id": 2,
                "question": "1 + 1의 결과는?",
                "choices": ["1", "2", "3", "4"],
                "answer": "2"
            },
            {
                "id": 3,
                "question": "파이썬의 창시자는?",
                "choices": [
                    "제임스 고슬링",
                    "귀도 반 로섬",
                    "데니스 리치",
                    "브렌던 아이크"
                ],
                "answer": "2"
            }
        ]
        self.best_score = self.load_best_score()

    def guess_quiz(self):
        guessed_quiz = 0

        for quiz in self.quiz_list:
            choices = "\n".join(
                f"{i}. {choice}"
                for i, choice in enumerate(quiz["choices"], start=1)
            )
            quiz_text = f"""
📋 퀴즈를 시작합니다! (총 {len(self.quiz_list)}문제)
------------------
[문제 {quiz['id']}]
{quiz['question']}
{choices}
            """
            print(quiz_text)
            answer = input("정답을 입력하세요 (1~4): ")
            if answer == quiz["answer"]:
                print("✅정답입니다!\n------------------")
                guessed_quiz += 1
            else:
                print("❌오답입니다!")

        if guessed_quiz == len(self.quiz_list):
            result_text = f"""
🏆 결과 : {len(self.quiz_list)}문제 중 {guessed_quiz}문제 정답! ({guessed_quiz * 20}점)
"""
        return "퀴즈 맞추기"

    def add_quiz(self):
        choices = []
        print("📌새로운 퀴즈를 추가합니다.\n")

        while True:
            quiz_question = input("문제를 입력하세요: ").strip()

            if not quiz_question:
                print("문제를 제대로 입력해주세요!")
                continue

            is_duplicate = False

            for quiz in self.quiz_list:
                # quiz_list를 Quiz 객체로 연결 후 quiz.question로 변경
                if quiz["question"] == quiz_question:
                    is_duplicate = True
                    break

            if is_duplicate:
                print("등록된 질문이 이미 있습니다")
                continue

            break

        for i in range(1, 5):
            while True:
                choice = input(f"선택지 {i}: ").strip()
                if choice:
                    choices.append(choice)
                    break

                print("선택지는 공백으로 입력할 수 없습니다.")

        while True:
            try:
                answer = int(input(f"정답 번호(1-4): "))
                if answer not in range(1, 5):
                    print("1부터 4사이의 번호를 입력해주세요.")
                    continue
                break
            except ValueError:
                print("숫자만 입력해주세요")

        new_quiz = Quiz(id=len(self.quiz_list) + 1, question=quiz_question, choices=choices, answer=answer)
        self.quiz_list.append(new_quiz)

        return "✅퀴즈가 추가되었습니다!"


    def list_quiz(self):
        if len(self.quiz_list) != 0:
            for quiz in self.quiz_list:
                print(f"{quiz["id"]}. {quiz["question"]}")

        return "퀴즈 목록 보기"

    def check_score(self):
        return "점수 확인하기"

    def end_quiz(self):
        return "퀴즈 끝내기"
