from quiz_game import QuizGame

def main():
    quiz_game = QuizGame()

    game_is_on = True

    while game_is_on:
        game_is_on = quiz_game.show_menu()

if __name__ == "__main__":
    main()
