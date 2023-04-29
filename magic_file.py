from sea_btl import shot, ship

__author__ = 'Ferret22'


def do_cheat_code(code: str, status: str, area_plr: list[list[str]], area_ai: list[list[str]],
                  area_ai_view: list[list[str]]):
    cheat_codes = ['killme', 'killai', 'fme', 'vienem']
    stats = ['gen', 'in_game']
    cheat_id = None
    status_id = stats.index(status)

    if code in cheat_codes:
        cheat_id = cheat_codes.index(code)

    if cheat_id == 0 and status_id == 1:
        kill_me(area_plr)

    if cheat_id == 1 and status_id == 1:
        kill_ai(area_ai, area_ai_view)

    if cheat_id == 2 and status_id == 0:
        return 1

    if cheat_id == 3 and status_id == 1:
        return area_ai


def kill_me(area_plr: list[list[str]]):
    for line in area_plr:
        while ship in line:
            id1 = area_plr.index(line)
            id2 = line.index(ship)
            area_plr[id1][id2] = shot


def kill_ai(area_ai: list[list[str]], area_ai_view: list[list[str]]):
    for line in area_ai:
        while ship in line:
            id1 = area_ai.index(line)
            id2 = line.index(ship)
            area_ai_view[id1][id2] = shot
            area_ai[id1][id2] = shot
