"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) #Загадываем число

# Количество попыток
count = 0

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100:56"))
    
    if predict_number > number:
        print("Число меньше")
    elif predict_number < number:
        print("Число больше")
    else:
        print(f"Вы угадали, это число {number}. Попыток - {count}")
        break #Конец