import numpy as np
import statistics as s

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    min_limit = 0
    max_limit = 101
    while True:
        count += 1
        predict_number = int((max_limit - min_limit)/2 + min_limit) 
        
        if predict_number > number:
            max_limit = predict_number
        elif predict_number < number:
            min_limit = predict_number
        else:
            break # Число угадано
    return count

def score_game(random_predict) -> int:
    """Возвращает среднее количество попыток

    Args:
        random_predict ([type]): функция расчета

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    
    np.random.seed(1)
    
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(s.mean(count_ls))
    
    print(f'Ваш алгоритм находит число в среднем за {score} раз')
    
    return score

if __name__ == '__main__':
    score_game(random_predict)