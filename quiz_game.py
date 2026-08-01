from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quiz_list = [
            {"id":1, "question": "대한민국의 수도는?", "answer": "서울"},
            {"id":2, "question": "1 + 1은?", "answer": "2"},
            {"id":3, "question": "파이썬의 창시자는?", "answer": "귀도 반 로섬"}]
        self.score = 0

    def guess_quiz(self):
        return "퀴즈 맞추기"

    def add_quiz(self, question, answer):
        if question.strip() == "" or answer.strip() == "":
            new_quiz = Quiz(len(self.quiz_list) + 1,question.strip(), answer.strip())
            self.quiz_list.append(new_quiz)
        return "퀴즈가 추가되었습니다."

    def list_quiz(self):
        if len(self.quiz_list) != 0:
            for quiz in self.quiz_list:
                print(f"{quiz["id"]}. {quiz["question"]}")

        return "퀴즈 목록 보기"

    def check_score(self):
        return "점수 확인하기"

    def end_quiz(self):
        return "퀴즈 끝내기"
