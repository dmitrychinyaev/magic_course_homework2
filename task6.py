# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19



def findDifferenceInFractionPart(numbers : list[float]) -> float:
    """
    Функция, которая находит разницу между максимальным и минимальным значением дробной части элементов.
    """
    max = 0
    min = 0
    for number in numbers:
        number = number - int(number)
        if(number>max):
            max = number
        if(number<min):
            min = number
    return max - min

list = [1.1, 1.2, 3.1, 5, 10.01]
print(findDifferenceInFractionPart(list))