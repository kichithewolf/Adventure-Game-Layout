init:
    $ current_talk = "None"
    $ current_background = "None"

screen custom_menu():
    tag menu
    imagemap:
        ground "assets/menu/game_menu_default.png"
        hover "assets/menu/game_menu_selected.png"
        hotspot (121, 140, 206, 140) action ShowMenu("inventory_screen")
        hotspot (420, 138, 198, 136) action ShowMenu("profile_screen")
        hotspot (708, 133, 206, 140) action ShowMenu("journal")
        hotspot (119, 467, 226, 176) action ShowMenu("preferences")
        hotspot (435, 464, 244, 192) action ShowMenu("load")
        hotspot (734, 457, 231, 202) action ShowMenu("save")
        hotspot (886, 1, 135, 46) action ShowMenu("main_menu")
        
screen custom_navigation():
    vbox xalign 0.5 yalign 0.95:
        imagemap:
            ground "assets/menu/game_nav_default.png"
            hover "assets/menu/game_nav_selected.png"
            hotspot (78, 21, 154, 132) action NullAction()#Move
            hotspot (310, 18, 163, 136) action Jump(current_talk)#Talk
            hotspot (530, 18, 161, 137) action NullAction()#Present
            hotspot (728, 16, 161, 141) action Show(current_background)#Examine

screen button():
    vbox xalign 0.99 yalign 0.01:
        imagebutton:
            idle "assets/buttons/tracker_idle.png"
            hover "assets/buttons/tracker_hover.png"
            action ui.callsinnewcontext("nav_screen_label")
            
label nav_screen_label:
    window hide
    call screen custom_navigation
    return