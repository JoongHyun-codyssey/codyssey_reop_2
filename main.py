from quiz_game import QuizGame

def main():
    quiz_game = QuizGame()

    game_is_on = True

    quiz_function = {
        1: quiz_game.guess_quiz,
        2: quiz_game.add_quiz,
        3: quiz_game.list_quiz,
        4: quiz_game.check_score,
    }

    while game_is_on:
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
        choose_number = int(input("메뉴 번호를 선택하세요: "))

        for i in range(1, 5):
            if choose_number == i:
                quiz_function[i]()
                # print(quiz_function[i]())
            elif choose_number == 5:
                print("퀴즈를 종료합니다!")
                game_is_on = False
                break
            else:
                print("제대로 된 번호를 입력하세요")

if __name__ == "__main__":
    main()
