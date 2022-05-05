from itertools import filterfalse
import re

# список строк для проверки
strings = ['1213dddf', '3dfpdk.', '2313', 'вавава', 'ddв11211', 'ssdwfЯЮ1', 'ёю', 'э']


# Функция для проверки строки на присутсвие в ней кириллических символов.
# Если количество символов меньше 2, возвращает False, иначе True.
# Использую здесь юникод, чтобы захватить все символы кириллической раскладки.
# Можно использовать список вида [а-яА-ЯЁё]
def has_cyrillic(text):
    return len(re.findall('[\u0400-\u04FF]', text)) < 2


# Функция для создания нового списка из данного.
# Я использую изменение самого списка через слайс, а не создаю новый список.
# Таким образом в перспективе фильтрация списка отразится
# на всех его использованиях в коде:
# будет использоваться отфильтрованный список, а не грязный.
#
# Фильтрацию провожу через filterfalse, которая возвращает те айтемы списка,
# которые выдают False при проходе через has_cyrillic()
def check_list(list_of_strings):
    list_of_strings[:] = filterfalse(has_cyrillic, list_of_strings)
    return list_of_strings


if __name__ == '__main__':
    print(check_list(strings))
