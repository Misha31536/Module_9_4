# Lambda-функция:
# Даны 2 строки:
# first = 'Мама мыла раму'
# second = 'Рамена мало было'
# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
# Здесь ? - место написания lambda-функции.

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))

# Замыкание:
#Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
# Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set -
# параметр принимающий неограниченное количество данных любого типа.
# Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
# Функция get_advanced_writer возвращает функцию write_everything.

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf8') as file:
            for line in data_set:
                file.write(str(line) + '\n')
    return write_everything

write = get_advanced_writer('Module_9_4')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:
# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
# В этом классе также определите метод __call__ который будет случайным образом выбирать
# слово из words и возвращать его. Для случайного выбора с одинаковой вероятностью для
# каждого данного в коллекции можете использовать функцию choice из модуля random.

from random import choice

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        rand = choice(self.words)
        return rand

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())