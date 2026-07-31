from quiz_game import QuizGame

game_is_on = True

quiz_game = QuizGame()

quiz_function = {
    1: quiz_game.guess_quiz,
    2: quiz_game.add_quiz,
    3: quiz_game.list_quiz,
    4: quiz_game.check_score,
}

while game_is_on:
    print("1. 퀴즈 출제\n2. 퀴즈 등록\n3. 퀴즈 목록\n4. 점수 확인\n5. 종료")
    choose_number = int(input("실행하실 번호를 입력하세요!\n"))

    for i in range(1, 5):
        if choose_number == i:
            quiz_function[i]()
            # print(quiz_function[i]())
        elif choose_number == 5:
            print("퀴즈를 종료합니다!")
            game_is_on = False
            break
