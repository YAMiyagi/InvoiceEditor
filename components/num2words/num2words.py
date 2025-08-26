from num2words import num2words

def convertNum2Words(num):
    try:
        words = num2words(int(num), lang='ru')
        words = words.capitalize()
        return words
    except ValueError:
        return "Неверный ввод. Пожалуйста, введите действительное число."