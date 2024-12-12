first = 'Мама мыла раму'                                    # 1 Задание, создание функции лямбда
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):                         # 2 Задание, замыкание
    def write_everything(*data_set):
        with open(file_name, 'w', encoding="utf-8") as file:
            for i in data_set:
                file.write(f'{i}\n')
            return data_set
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


from random import choice, random                           # 3 Задание, Метод __call_
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self,):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())