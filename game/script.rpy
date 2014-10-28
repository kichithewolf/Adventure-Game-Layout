# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


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
    
    "Act IV"
    
    e "Updating journal"
    
    e "Journal updated."
    
    "Act IV"
    
    e "Done talking with witness/victim/random person/parrot."
    
    $ current_talk = "demo_witness_talk_1"
    
    call nav_screen_label
    
    "End game"

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
    call nav_screen_label