import numpy as np


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # Фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_v3(number):
    """Используем алгоритм бинарного поиска для угадывания числа"""
    count = 1
    predict = 50
    minimum = 0
    maximum = 100
    while number != predict:
        count += 1
        if number > predict:
            minimum = predict + 1
        else:
            maximum = predict - 1
        predict = (minimum + maximum) // 2
    return count


score_game(game_core_v3)