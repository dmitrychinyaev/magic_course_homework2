# Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def findSecondPositionOfElement(list, elementToFind):
    if(list.count(elementToFind) < 2) or (len(list) == 0):
        return -1
    count = 0
    for i in range(len(list)):
        if(list[i] == elementToFind):
            count = count + 1
            if(count == 2):
                return i
    return -1 
    

list_to_find = [3.14, True, "Hello world!", 12, 3.14]
element = 3.14    
print(findSecondPositionOfElement(list_to_find, element))

