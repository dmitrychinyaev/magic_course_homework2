# В большой текстовой строке подсчитать
# количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.

def countWordsInText(text):
    text = text.lower()
    wordsList = text.replace(",", "").replace(".", "").split()
    dict_count_words = {}

    for word in wordsList:
        if word in dict_count_words:
            dict_count_words[word] += 1
        else:
            dict_count_words[word] = 1

    # Сортируем словарь по убыванию количества слов. Эту строчку подсмотрел) 
    return sorted(dict_count_words.items(), key=lambda item: item[1], reverse=True)

print(countWordsInText("Привет всем! Меня зовут Привет привет. Как тебя зовут?"))
