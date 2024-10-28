# Создайте вручную список содержащий элементы разных типов.
# Получите из него словарь списков, где ключ - тип элемента,
# а значение - список элементов данного типа.
# Для списка: [1, 2, "3", "4", True, 5.5]
# Ответ:  {int: [1, 2, 5], float: [5.5], str: ["3", "4"], bool: [True]}

listToFind = [1, 2, "3", "4", True, 5.5]

def findTypeElementAndPutInArr(list):
    #Заводим пустой словарь
    dict = {}
    for i in range (len(list)): 
        #Находим тип элемента и переводим его в str
        x = str(type(list[i])).split('\'')[1].split('\'')[0]
        #Ищем этот элемент в словаре. Если нет, то добавляем как новый ключ.
        if x in dict:
            dict.get(x).append(list[i])
        else:
            new_list = [list[i]] 
            dict[x] = new_list

    return dict

print(findTypeElementAndPutInArr(listToFind))