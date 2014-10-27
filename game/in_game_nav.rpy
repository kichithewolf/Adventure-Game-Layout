screen custom_menu():
    tag menu
    imagemap:
        ground "assets/menu/game_menu_default.png"
        hover "assets/menu/game_menu_selected.png"
        hotspot (121, 140, 206, 140) action ShowMenu("inventory_screen")
        hotspot (420, 138, 198, 136) action ShowMenu("profiles")
        hotspot (708, 133, 206, 140) action ShowMenu("journal")
        hotspot (119, 467, 226, 176) action ShowMenu("preferences")
        hotspot (435, 464, 244, 192) action ShowMenu("load")
        hotspot (734, 457, 231, 202) action ShowMenu("save")
        hotspot (886, 1, 135, 46) action ShowMenu("main_menu")