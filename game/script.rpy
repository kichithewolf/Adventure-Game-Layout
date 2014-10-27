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
        inventory = Inventory()
    
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

    return
