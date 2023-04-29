from sea_btl import emptiness, shot, miss, ship
from sea_btl import o_ships, f_ships, t_ships, d_ships
from sea_btl import check_crd_f_ships, check_crd_d_ships, check_crd_t_ships, rand_coord

area_player = [[emptiness for _ in range(10)] + [str(i + 1)] for i in range(10)]
area_mass_plr = [[1 for _ in range(10)] for _ in range(10)]
area_ai = [[emptiness for _ in range(10)] + [str(i + 1)] for i in range(10)]
area_mass_ai = [[1 for _ in range(10)] for _ in range(10)]


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


def create_o_ships(area: list[list[str]], area_mass: list[list[int]]):
    count = 0
    while count != o_ships:
        id1 = rand_coord()
        if check_mass_area(id1, area_mass):
            stay_sharp(id1, area, area_mass)
            count += 1


def create_area_ships(area: list[list[str]], area_mass: list[list[int]]):
    create_f_ships(area, area_mass)
    create_t_ships(area, area_mass)
    create_d_ships(area, area_mass)
    create_o_ships(area, area_mass)
