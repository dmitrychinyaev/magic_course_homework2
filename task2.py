# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def findSumOddNumbers(list):
    if(len(list)) < 1:
        return 0
    
    count = 0

    if len(list) % 2 == 0:
        for i in range(1,len(list), 2):
            count = count + list[i]

    if len(list) % 2 != 0:
        for i in range(1,len(list) - 1, 2):
            count = count + list[i]
    
    return count

list = [2, 3, 5, 9, 1, 10]
print(findSumOddNumbers(list))