from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quiz_list = []
        self.score = 0

    def guess_quiz(self):
        return "퀴즈 맞추기"

    def add_quiz(self, question, answer):
        if question.strip() == "" or answer.strip() == "":
            new_quiz = Quiz(question.strip(), answer.strip())
            self.quiz_list.append(new_quiz)
        return "퀴즈가 추가되었습니다."

    def list_quiz(self):
        return "퀴즈 목록 보기"

    def check_score(self):
        return "점수 확인하기"

    def end_quiz(self):
        return "퀴즈 끝내기"
