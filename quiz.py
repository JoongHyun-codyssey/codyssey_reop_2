class Quiz:
    def __init__(self, id, question, choices, answer):
        self.id = id
        self.question = question
        self.choices = choices
        self.answer = answer

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }