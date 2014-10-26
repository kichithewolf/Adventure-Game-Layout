#show screen in_game_nav_button

screen in_game_nav_button():
    vbox xalign 1.0 yalign 0.0:
        imagebutton:
            idle "assets/buttons/ingamenav.png"
            hover "assets/buttons/ingamenavhover.png"
            action ui.callsinnewcontext("in_game_nav_label")

label in_game_nav_label:
    window hide
    call screen in_game_nav
    return
            
screen in_game_nav():
    tag menu
    
    frame:
        has vbox
        textbutton _("Something") action Return()
        textbutton _("Something") action Return()
        textbutton _("Something") action Return()
        textbutton _("Return") action Return()