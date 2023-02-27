# объявление функции
def count_letter(text, letter):
    r = [i for i in text if letter in i]
    print(len(r))

# считываем данные
text = input()
symbol = input()
# вызываем функцию
count_letter(text, symbol)