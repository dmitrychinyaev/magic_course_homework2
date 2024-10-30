# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму дробей.
# Ввод:
# 1/2
# 2/3
# Вывод:
# 7/6  (будет еще круче если упростите до 1+1/6)



def sumFraction(first_fr: str, second_fr: str) -> str:
    """
    Функция, которая которая принимает две строки вида “a/b” - дробь с числителем и знаменателем и
    и возвращает сумму дробей.
    """
    #Берем числитель и знаменатель у обоих дробей
    slashPositionFirst = first_fr.index("/")
    firstNumerator = int(first_fr[:slashPositionFirst])
    firstDenominator = int(first_fr[slashPositionFirst+1:])

    slashPositionSecond = second_fr.index("/")
    secondNumerator = int(second_fr[:slashPositionSecond])
    secondDenominator = int(second_fr[slashPositionSecond+1:])

    #Рассчитываем результат числитель и знаменатель
    resultDenominator = firstDenominator * secondDenominator
    resultNumerator = (firstNumerator * secondDenominator) + (secondNumerator * firstDenominator)

    #Теперь смотрим на числитель и определяем что выводить
    #Здесь вариант если числитель меньше знаменателя
    if (resultNumerator < resultDenominator):
        return str(resultNumerator) + "/" + str(resultDenominator)
    #Тут вариант когда числитель и знаменатель равны
    elif (resultDenominator == resultNumerator):
        return 1
    #Здесь вариант, когда числитель больше знаменателя. В цикле уменьшаем числитель на значение
    #знаменателя, увеличиваем счетчик. Если числитель больше 0 и не равен знаменателю, то выводим
    #счетчик плюс числитель и знаменатель. Если числитель = 0, то выводим счетчик. Если числитель 
    #равен знаменателю, то выводим счетчик + 1
    elif (resultNumerator > resultDenominator):
        count = 0
        while resultNumerator > resultDenominator :
            resultNumerator = resultNumerator - resultDenominator
            count = count + 1

        if(resultNumerator<resultDenominator):    
            return str(count) + "+" + str(resultNumerator) + "/" + str(resultDenominator)
        elif (resultNumerator == 0):
            return str(count)
        elif (resultDenominator == resultNumerator):
            count = count + 1
            return str(count)
    
    
print(sumFraction("9/3","3/3"))