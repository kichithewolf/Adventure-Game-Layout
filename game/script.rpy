# You can place the script of your game in this file.

image placeholder = "assets/portraits/placeholder.png"

image background1 = "assets/backgrounds/background1.png"
image background2 = "assets/backgrounds/background2.png"

# Declare characters used by this game.
define e = Character('Player Character', color="#c8ffc8")
define w = Character('Witness', color = "c8ffc9")


# The game starts here.
label start:
    python:
        player = Player("Derp")
        chocolate = Item("Chocolate",image="gui/inv_chocolate.png")
        banana = Item("Banana", image="gui/inv_banana.png")    
        gun = Item("Gun", image="gui/inv_gun.png")
        laser = Item("Laser Gun", image="gui/inv_laser.png")
        
        
        gun = Person("Gun", image="gui/pro_gun.png")
        laser = Person("Laser Gun", image="gui/pro_laser.png")
        
        
        inventory = Inventory()
        profile = Profiles()
    
    scene background1
    
    "Prologue"

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    $ save_name = "Act 1"
    
    "Act 1"
    
    e "Done with prologue, save name should change here."
    
    $ save_name = "Act 2"
    
    "Act 2"
    
    e "Adding stuff to inventory!"
    
    $inventory.add(chocolate)
    $inventory.add(banana)
    
    e "Added chocolate and banana."
    
    "Act 3"
    
    e "Adding profiles."
    
    $profile.add(gun)
    $profile.add(laser)
    
    e "Added profiles."
    
    "Act 4"
    
    e "Updating journal"
    
    e "Journal updated."
    
    "Act IV"
    
    $ cleared_area = 0
    
    scene background2
    
    show placeholder at center
    
    call demo_act_IV

label endgame:
    
    "End game"
    
    return
    
label demo_act_IV:
    
    if cleared_area == 0:
        $ current_talk = "demo_witness_talk_1"
        $ current_background = "demo_background_1"
        $ demo_background_1_response = 0
        call nav_screen_label
    
    e "Done talking with witness/victim/random person/parrot."
    
    jump endgame

    return
    
screen demo_background_1:
    textbutton _("Return") action Return()
    
    imagemap:
        ground "assets/backgrounds/background2.png"
        hover "assets/backgrounds/background2.png"
        hotspot (113, 173, 151, 122) action [SetVariable("demo_background_1_response", 1), Return()]
        hotspot (434, 287, 161, 156) action [SetVariable("demo_background_1_response", 2), Return()]
        hotspot (151, 493, 197, 176) action [SetVariable("demo_background_1_response", 3), Return()]
        hotspot (714, 453, 162, 158) action [SetVariable("demo_background_1_response", 4), Return()]
        
label demo_background_1_answer:
    if demo_background_1_response == 1:
        "You clicked #1"
    elif demo_background_1_response == 2:
        "You clicked #2"
    elif demo_background_1_response == 3:
        "You clicked #3"
    elif demo_background_1_response == 4:
        "You clicked #4"
        
    call demo_background_1
    
    return

label demo_witness_talk_1:
    $loop = 1
    while loop == 1:
        menu:
            "Hello":
                e "Hello."
                
                "Hello there."
                
                e "Bye."
                
                "Goodbye."
                
            "Test 2":
                
                "Test 2"
                
            "Finished talking.":
                $ loop = 0
                $ cleared_area = 1
                
    call demo_act_IV