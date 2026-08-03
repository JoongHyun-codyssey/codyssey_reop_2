from quiz import Quiz

import json

class QuizGame:
    def __init__(self):
        self.quiz_list = self.load_quiz_list()
        self.best_score = self.load_best_score()

    def show_menu(self):
        quiz_function = {
            1: self.guess_quiz,
            2: self.add_quiz,
            3: self.list_quiz,
            4: self.check_score,
        }

        print(
            "\n"
            "================================\n"
            "           QUIZ GAME\n"
            "================================\n"
            "  [1] 퀴즈 출제\n"
            "  [2] 퀴즈 등록\n"
            "  [3] 퀴즈 목록\n"
            "  [4] 점수 확인\n"
            "  [5] 종료\n"
            "--------------------------------"
        )
        while True:
            try:
                choose_number = int(input("메뉴 번호를 선택하세요: "))

                if choose_number < 1 or choose_number > 5:
                    print("잘못된 메뉴 번호입니다.")
                    continue

                break

            except ValueError:
                print("숫자만 입력해주세요.")
                continue
            except KeyboardInterrupt:
                print("\nCtrl+C로 종료할 수 없습니다. 메뉴 번호를 입력해 주세요.")
                continue

        if choose_number == 5:
            print("퀴즈를 종료합니다!")
            return False

        if choose_number in quiz_function:
            quiz_function[choose_number]()
            return True

        return True

    def guess_quiz(self):
        guessed_quiz = 0

        print(f"📋 퀴즈를 시작합니다! (총 {len(self.quiz_list)}문제)\n")
        for quiz in self.quiz_list:
            choices = "\n".join(
                f"{i}. {choice}"
                for i, choice in enumerate(quiz.choices, start=1)
            )
            quiz_text = (
                "------------------\n"
                f"[문제 {quiz.id + 1}]\n"
                f"{quiz.question}\n"
                f"{choices}\n"
                "------------------\n"
            )
            print(quiz_text)

            while True:
                answer = int(input("정답을 입력하세요 (1~4): "))
                if answer not in (1, 2, 3, 4):
                    print("⚠️잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
                    continue

                if answer == quiz.answer:
                    print("✅정답입니다!\n------------------")
                    guessed_quiz += 1
                else:
                    print("❌오답입니다!")
                break

        result_text = (
                f"결과 : {len(self.quiz_list)}문제 중 {guessed_quiz}문제 정답! ({guessed_quiz * 20}점)"
            )
        print (result_text)

        if self.best_score < guessed_quiz * 20:
            print("🎉 새로운 최고 점수입니다!")
            self.save_best_score(int(guessed_quiz * 20))

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
                if quiz.question == quiz_question:
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

        new_quiz = Quiz(id=self.get_new_quiz_id(), question=quiz_question, choices=choices, answer=answer)
        self.save_quiz_list(new_quiz)
        self.quiz_list = self.load_quiz_list()

        return "✅퀴즈가 추가되었습니다!"


    def list_quiz(self):
        if len(self.quiz_list) != 0:
            print(f"📋등록된 퀴즈 목록 (총 {len(self.load_quiz_list())}개)")
            print(f"-----------------------------")
            for quiz in self.quiz_list:
                quiz_list_text = f"{quiz.id + 1}. {quiz.question}"
                print(quiz_list_text)
            print(f"-----------------------------")

        return "퀴즈 목록 보기"

    def check_score(self):
        print(f"🏆최고 점수:{self.load_best_score()}")
        return "최고 점수 확인"

    def get_new_quiz_id(self):
        try:
            with open("state.json", mode="r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        saved_quiz_list = data.get("quiz_list", [])
        return len(saved_quiz_list)

    def load_quiz_list(self):
        try:
            with open("state.json", mode="r", encoding="utf-8") as file:
                data = json.load(file)

                quiz_data_list = (
                    data.get("quiz_list") or data.get("modern_quiz_list", [])
                )

                return [
                    Quiz(
                        id=quiz["id"],
                        question=quiz["question"],
                        choices=quiz["choices"],
                        answer=quiz["answer"]
                    )
                    for quiz in quiz_data_list
                ]

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def load_best_score(self):
        try:
            with open("state.json", mode="r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("best_score", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            return 0

    def save_best_score(self, new_best_score):
        try:
            with open("state.json", mode="r", encoding="utf-8") as file:
                json_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            json_data = {}

        json_data["best_score"] = new_best_score

        with open("state.json", mode="w", encoding="utf-8") as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)

    def save_quiz_list(self, new_quiz):
        try:
            with open("state.json", mode="r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data["quiz_list"].append(new_quiz
                                 .to_dict())

        with open("state.json", mode="w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)