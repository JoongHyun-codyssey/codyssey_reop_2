from quiz import Quiz

import json

class QuizGame:
    def __init__(self):
        self.quiz_list = self.load_quiz_list()
        self.best_score = self.load_best_score()

    def guess_quiz(self):
        return "퀴즈 맞추기"

    def add_quiz(self):
        return "퀴즈 추가하기"

    def list_quiz(self):
        return "퀴즈 목록 보기"

    def check_score(self):
        return "점수 확인하기"

    def end_quiz(self):
        return "퀴즈 끝내기"

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
            data = {
                "best_score" : new_best_score
            }
            with open("state.json", mode="w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

    def save_quiz_list(self, quiz):
        data = {
            "quiz_list" : [
                quiz.to_dict()
                for quiz in self.quiz_list
            ]
        }

        with open("state.json", mode="w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)