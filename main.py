from quiz_game import QuizGame

def main():
    quiz_game = QuizGame()

    game_is_on = True

    while game_is_on:
        result = quiz_game.show_menu()
        game_is_on = result

if __name__ == "__main__":
    main()
