from random import randint

def main_1():
    x = float(input('Сторона А: '))
    y = float(input('Сторона Б: '))
    print('Площадь прямоугольника =', x * y)

def main_2():
    while True:
        a = int(input('Загадайте число от 1 до 10:'))
        if a == randint(1, 10):
            print('Я угадал твое число', a)
        else:
            print('Делаю ещё попытку')

if __name__ == '__main__':
    # main_1()
    main_2()