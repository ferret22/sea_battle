import random
from colorama import Fore, init, Style

init(autoreset=True)

emptiness = '*'
chars = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
shot = Fore.RED + 'X'
miss = Fore.BLUE + '•'
ship = Fore.GREEN + '■'
o_ships = 4
d_ships = 3
t_ships = 2
f_ships = 1


def draw_area(area_plr: list[list[str]], area_ai_view: list[list[str]]):
    print()
    print('Ваше поле\t\t Поле противника')
    print(*chars + ['  \t'] + chars)
    for idx in range(10):
        print(*area_plr[idx] + ['\t'] + area_ai_view[idx])
    print()


def check_to_shoot(idx1: int, idx2: int, area: list[list[str]]):
    cell = area[idx1][idx2]
    if cell == ship:
        return shot
    elif cell == emptiness:
        return miss


def enemy_shoot(area_player: list[list[str]], area_shoot: list[list[int]], shoot_count: list[int]):
    if shoot_count[0] != 0:
        id1, id2 = 0, 0
        for ars_shot in area_shoot:
            mx = max(ars_shot)
            if mx > id2:
                id2 = ars_shot.index(mx)
                id1 = area_shoot.index(ars_shot)
    else:
        id1, id2 = rand_coord()

    cell = check_to_shoot(id1, id2, area_player)
    print("Противник сходил: " + Fore.RED + chars[id2] + str(id1 + 1))
        
    if cell:
        area_shoot[id1][id2] = 0
        area_player[id1][id2] = cell
        shoot_count[0] = 0

        for line in area_shoot:
            while 50 in line:
                idx1 = area_shoot.index(line)
                idx2 = line.index(50)
                area_shoot[idx1][idx2] = 1

        if cell == shot:
            shoot_count[0] += 1

            if id1 != 0:
                area_shoot[id1 - 1][id2] *= 50
            if id1 != 9:
                area_shoot[id1 + 1][id2] *= 50
            if id2 != 0:
                area_shoot[id1][id2 - 1] *= 50
            if id2 != 9:
                area_shoot[id1][id2 + 1] *= 50


def check_area(area: list):
    count = 0
    for ar in area:
        if ship in ar:
            count += 1

    if count > 0:
        return True
    return False


def shoot_first_num(ans: str, area_ai: list[list[str]], area_ai_view: list[list[str]], idx: int):
    idx1 = int(ans[:idx]) - 1
    idx2 = chars.index(ans[idx].upper())
    cell = check_to_shoot(idx1, idx2, area_ai)
    if cell:
        area_ai[idx1][idx2] = cell
        area_ai_view[idx1][idx2] = cell


def shoot_second_num(ans: str, area_ai: list[list[str]], area_ai_view: list[list[str]]):
    idx1 = int(ans[1:]) - 1
    idx2 = chars.index(ans[0].upper())
    cell = check_to_shoot(idx1, idx2, area_ai)
    if cell:
        area_ai[idx1][idx2] = cell
        area_ai_view[idx1][idx2] = cell


def rand_coord():
    id1 = random.randint(0, 9)
    id2 = random.randint(0, 9)
    return id1, id2


def check_crd_d_ships(id1: tuple[int, int], id2: tuple[int, int]):
    if id1[0] - id2[0] == 0:
        if (id1[1] - id2[1] == 1) or (id1[1] - id2[1] == -1):
            return True
    elif (id1[0] - id2[0] == 1) or (id1[0] - id2[0] == -1):
        if id1[1] - id2[1] == 0:
            return True


def check_crd_t_ships(id1: tuple[int, int], id2: tuple[int, int], id3: tuple[int, int]):
    if (id1[0] == id2[0]) and (id2[0] == id3[0]):
        if ((id1[1] - id2[1] == 1) and (id2[1] - id3[1] == 1)) or ((id1[1] - id2[1] == -1) and (id2[1] - id3[1] == -1)):
            return True
    elif ((id1[0] - id2[0] == 1) and (id2[0] - id3[0] == 1)) or ((id1[0] - id2[0] == -1) and (id2[0] - id3[0] == -1)):
        if (id1[1] == id2[1]) and (id2[1] == id3[1]):
            return True


def check_crd_f_ships(id1: tuple[int, int], id2: tuple[int, int], id3: tuple[int, int], id4: tuple[int, int]):
    if (id1[0] == id2[0]) and (id2[0] == id3[0]) and (id3[0] == id4[0]):
        if ((id1[1] - id2[1] == 1) and (id2[1] - id3[1] == 1) and (id3[1] - id4[1] == 1)) or \
                ((id1[1] - id2[1] == -1) and (id2[1] - id3[1] == -1) and (id3[1] - id4[1] == -1)):
            return True
    elif ((id1[0] - id2[0] == 1) and (id2[0] - id3[0] == 1) and (id3[0] - id4[0] == 1)) or \
            ((id1[0] - id2[0] == -1) and (id2[0] - id3[0] == -1) and (id3[0] - id4[0] == -1)):
        if (id1[1] == id2[1]) and (id2[1] == id3[1]) and (id3[1] == id4[1]):
            return True


def check_mass_area(ids: tuple[int, int], area_mass: list[list[int]]):
    id1, id2 = ids[0], ids[1]
    if area_mass[id1][id2] == 1:
        return True
    return False


def stay_sharp(ids: tuple[int, int], area: list[list[str]], area_mass: list[list[int]]):
    id1 = ids[0]
    id2 = ids[1]
    area[id1][id2] = ship

    # Увеличение весов на основной линии
    area_mass[id1][id2] *= 50
    if id2 != 0:
        area_mass[id1][id2 - 1] += 1
    if id2 != 9:
        area_mass[id1][id2 + 1] += 1

    # Увеличение весов на верхней линии
    if id1 != 0:
        area_mass[id1 - 1][id2] += 1
        if id2 != 0:
            area_mass[id1 - 1][id2 - 1] += 1
        if id2 != 9:
            area_mass[id1 - 1][id2 + 1] += 1

    # Увеличение весов на нижней линии
    if id1 != 9:
        area_mass[id1 + 1][id2] += 1
        if id2 != 0:
            area_mass[id1 + 1][id2 - 1] += 1
        if id2 != 9:
            area_mass[id1 + 1][id2 + 1] += 1


def create_o_ships(area: list[list[str]], area_mass: list[list[int]]):
    count = 0
    while count != o_ships:
        id1 = rand_coord()
        if check_mass_area(id1, area_mass):
            stay_sharp(id1, area, area_mass)
            count += 1


def create_d_ships(area: list[list[str]], area_mass: list[list[int]]):
    count = 0
    while count != d_ships:
        id1 = rand_coord()
        id2 = rand_coord()
        if check_crd_d_ships(id1, id2):
            if check_mass_area(id1, area_mass) and check_mass_area(id2, area_mass):
                stay_sharp(id1, area, area_mass)
                stay_sharp(id2, area, area_mass)
                count += 1


def create_t_ships(area: list[list[str]], area_mass: list[list[int]]):
    count = 0
    while count != t_ships:
        id1 = rand_coord()
        id2 = rand_coord()
        id3 = rand_coord()
        if check_crd_t_ships(id1, id2, id3):
            if check_mass_area(id1, area_mass) and check_mass_area(id2, area_mass) and check_mass_area(id3, area_mass):
                stay_sharp(id1, area, area_mass)
                stay_sharp(id2, area, area_mass)
                stay_sharp(id3, area, area_mass)
                count += 1


def create_f_ships(area: list[list[str]], area_mass: list[list[int]]):
    count = 0
    while count != f_ships:
        id1 = rand_coord()
        id2 = rand_coord()
        id3 = rand_coord()
        id4 = rand_coord()
        if check_crd_f_ships(id1, id2, id3, id4):
            if check_mass_area(id1, area_mass) and check_mass_area(id2, area_mass) and \
                    check_mass_area(id3, area_mass) and check_mass_area(id4, area_mass):
                stay_sharp(id1, area, area_mass)
                stay_sharp(id2, area, area_mass)
                stay_sharp(id3, area, area_mass)
                stay_sharp(id4, area, area_mass)
                count += 1


def create_ships(areas: list[list[list[str]]], mass_areas: list[list[list[int]]]):
    plr = Fore.GREEN + 'Вашего'
    en = Fore.RED + 'Противника'

    for area in areas:
        idx = areas.index(area)
        area_mass = mass_areas[idx]

        if idx == 0:
            print('Генерация ' + plr + Style.RESET_ALL + ' поля')
        else:
            print('Генерация поля ' + en)

        create_f_ships(area, area_mass)
        create_t_ships(area, area_mass)
        create_d_ships(area, area_mass)
        create_o_ships(area, area_mass)
