def guessing_cycle(name, game_round):
    number_of_correct_answers = 0
    for _ in range(3):
        if (game_round()):
            number_of_correct_answers += 1
        else:
            print(f"Let's try again, {name}!")
            break

    if (number_of_correct_answers == 3):
        print(f"Congratulations, {name}!")
