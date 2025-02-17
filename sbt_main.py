from sea_btl import emptiness, draw_area, create_ships, enemy_shoot
from sea_btl import shoot_first_num, shoot_second_num, check_area
import os
import random
from colorama import Fore, Style
from magic_file import do_cheat_code
import time

__author__ = 'Ferret22'


def create_areas():  # Создаём игровые поля
    t0 = time.process_time()
    os.system('CLS')
    area_player = [[emptiness for _ in range(10)] + [str(i + 1)] for i in range(10)]
    area_ai = [[emptiness for _ in range(10)] + [str(i + 1)] for i in range(10)]

    area_mass_plr = [[1 for _ in range(10)] for _ in range(10)]
    area_mass_ai = [[1 for _ in range(10)] for _ in range(10)]

    area_ai_view = [[emptiness for _ in range(10)] + [str(i + 1)] for i in range(10)]

    create_ships([area_player, area_ai], [area_mass_plr, area_mass_ai])
    print('Генерация завершена!')
    draw_area(area_player, area_ai_view)

    t1 = time.process_time()
    print(f"Time elapsed: {t1 - t0} sec.")
    return area_player, area_ai, area_ai_view


# Функция, которая отвечает за стрельбу игрока
def player_shoot(ans: str, area_plr: list[list[str]], area_ai: list[list[str]], area_ai_view: list[list[str]]):
    status = 'in_game'
    ar_ai_view = do_cheat_code(ans, status, area_plr, area_ai, area_ai_view)
    if ar_ai_view is None:
        ar_ai_view = area_ai_view

    if len(ans) >= 2:
        if ans[0].isdigit():
            if ans[1].isdigit():
                shoot_first_num(ans, area_ai, ar_ai_view, 2)
                draw_area(area_plr, ar_ai_view)
            else:
                shoot_first_num(ans, area_ai, ar_ai_view, 1)
                draw_area(area_plr, ar_ai_view)
        elif ans[1].isdigit():
            if len(ans) == 3:
                if ans[2].isdigit():
                    shoot_second_num(ans, area_ai, ar_ai_view)
                    draw_area(area_plr, ar_ai_view)
            else:
                shoot_second_num(ans, area_ai, ar_ai_view)
                draw_area(area_plr, ar_ai_view)
        else:
            print("Не возможно сделать выстрел!")
    else:
        print("Не возможно сделать выстрел!")

    return ar_ai_view


# Функция повторной генерации
def generate_area():
    n = '1'
    status = 'gen'
    areas = None
    num = None
    while n == '1':
        area_player, area_ai, area_ai_view = create_areas()

        n = input('Сгенерировать поля заново? (1.ДА/2.НЕТ):' + Fore.GREEN + ' ')
        print(Style.RESET_ALL)

        num = do_cheat_code(n, status, area_player, area_ai, area_ai_view)
        if num == 2:
            num = None
            area_ai_view = area_ai
        areas = (area_player, area_ai, area_ai_view)

    return areas, num


# Определяем за кем 1-й ход. 1 - игрок, 2 - ИИ
def choose_first_step():
    num = random.randint(1, 2)
    if num == 1:
        print(Fore.GREEN + 'Вы' + Style.RESET_ALL + ' ходите первым!')
        return num
    else:
        print(Fore.RED + 'Противник' + Style.RESET_ALL + ' ходит первым!')
        return num


# Основной игровой цикл. Работает пока кто-то не выиграет. После чего выводит соответсвующее сообщение
def game_cycle():
    os.system('CLS')
    areas, num = generate_area()
    ar_view = areas[2]

    if num is None:
        num = choose_first_step()

    shoot_count = [0, 0]
    area_shoot_ai = [[1 for _ in range(10)] for _ in range(10)]

    while check_area(areas[0]) and check_area(areas[1]):
        if num == 1:
            ans = input('Введите координаты:' + Fore.GREEN + ' ')
            print(Style.RESET_ALL)
            ar_view = player_shoot(ans, areas[0], areas[1], ar_view)

            if check_area(areas[1]) is True:
                enemy_shoot(areas[0], area_shoot_ai, shoot_count)
            else:
                break

            if ar_view is None:
                ar_view = areas[2]
            draw_area(areas[0], ar_view)

        else:
            enemy_shoot(areas[0], area_shoot_ai, shoot_count)
            if ar_view is None:
                ar_view = areas[2]
            draw_area(areas[0], ar_view)

            if check_area(areas[0]) is not True:
                break

            ans = input('Введите координаты:' + Fore.GREEN + ' ')
            print(Style.RESET_ALL)
            ar_view = player_shoot(ans, areas[0], areas[1], ar_view)

    if check_area(areas[0]):
        print(Fore.GREEN + 'Вы выиграли!')
        print(Style.RESET_ALL)
        draw_area(areas[0], ar_view)
    else:
        print(Fore.RED + 'Вы проиграли!')
        print(Style.RESET_ALL)
        draw_area(areas[0], areas[1])
    n = input('Нажмите <Enter>, чтобы продолжить... ')  # Нужна что-бы сразу после выигрыша/проигрыша, все поля не
    # стёрлись


# Функция старта игрового цикла
def game_start():
    ans = input('Хотите начать? (1.ДА/2.НЕТ)' + Fore.GREEN + ' ')
    print(Style.RESET_ALL)
    while ans == '1':
        game_cycle()
        ans = input('Хотите начать? (1.ДА/2.НЕТ)' + Fore.GREEN + ' ')
        print(Style.RESET_ALL)


if __name__ == '__main__':
    print(Fore.MAGENTA + 'ДОБРО ПОЖАЛОВАТЬ В' + Fore.BLUE + ' "МОРСКОЙ БОЙ"')
    print(Style.RESET_ALL)
    game_start()
