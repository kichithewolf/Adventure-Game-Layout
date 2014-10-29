###############################
# Inventory
#
###############################

init -1 python:
    from operator import attrgetter # we need this for sorting items

    inv_page = 0 # initial page of teh inventory screen
    item = None
    class Player(renpy.store.object):
        def __init__(self, name):
            self.name=name
    player = Player("Derp")
    
    class Item(store.object):
        def __init__(self, name, image=""):
            self.name = name
            self.image=image # image file to use for this item

    class Inventory(store.object):
        def __init__(self):
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)

    def item_use():
        item.use()

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_top.size=20
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2
    
    style.button.background=Frame("gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000"


    showitems = False #turn True to debug the inventory
    def display_items_overlay():
        if showitems:
            inventory_show = "Inventory: "
            for i in range(0, len(inventory.items)):
                item_name = inventory.items[i].name
                if i > 0:
                    inventory_show += ", "
                inventory_show += item_name
            
            ui.frame()
            ui.text(inventory_show, color="#000")
    config.overlay_functions.append(display_items_overlay)

screen inventory_button:
    textbutton "Show Inventory" action [ Show("inventory_screen"), Hide("inventory_button")] align (.95,.04)
    
screen inventory_screen:
    tag menu
    add "gui/inventory.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.95,.04) spacing 20:
        textbutton "Close Inventory" action [ Hide("inventory_screen"), Show("inventory_button"), Return(None)]
    $ x = 515 # coordinates of the top left item position
    $ y = 25
    $ i = 0
    $ sorted_items = sorted(inventory.items, key=attrgetter('name'), reverse=True)
    $ next_inv_page = inv_page + 1            
    if next_inv_page > int(len(inventory.items)/9):
        $ next_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 190
            if i%3==0:
                $ y += 170
                $ x = 515
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
            imagebutton idle pic hover pic xpos x ypos y action [NullAction()] hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] at inv_eff
            #add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(inventory.items)>9:
            textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos .475 ypos .83

screen gui_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

init -1:
    transform inv_eff: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.5 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 1.0
        on hover:
            linear 0.2 alpha 2.5

    image information = Text("INFORMATION", style="tips_top")
    #Tooltips-inventory:
    image tooltip_inventory_chocolate=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Generic chocolate to heal\n40 points of health.", style="tips_bottom"))
    image tooltip_inventory_banana=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("A healthy banana full of potassium! You can also use it as ammo for your guns! O.O Recharges 20 bullets.", style="tips_bottom"))
    image tooltip_inventory_gun=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("An gun that looks like something a cop would\ncarry around. Most effective on humans.", style="tips_bottom"))
    image tooltip_inventory_laser=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("An energy gun that shoots photon beams.\nMost effective on aliens.", style="tips_bottom"))


###############################
# Profiles
#
###############################

init -1 python:
    from operator import attrgetter # we need this for sorting items

    pro_page = 0 # initial page of teh inventory screen
    item = None
    
    class Person(store.object):
        def __init__(self, name, image=""):
            self.name = name
            self.image=image # image file to use for this item

    class Profiles(store.object):
        def __init__(self):
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)

    def item_use():
        item.use()

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_top.size=20
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2
    
    style.button.background=Frame("gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000"

screen profile_button:
    textbutton "Show Profiles" action [ Show("profile_screen"), Hide("profile_button")] align (.95,.04)
    
screen profile_screen:
    tag menu
    add "gui/inventory.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.95,.04) spacing 20:
        textbutton "Close Profiles" action [ Hide("profile_screen"), Show("profile_button"), Return(None)]
    $ x = 515 # coordinates of the top left item position
    $ y = 25
    $ i = 0
    $ sorted_items = sorted(profile.items, key=attrgetter('name'), reverse=True)
    $ next_pro_page = pro_page + 1            
    if next_pro_page > int(len(profile.items)/9):
        $ next_pro_page = 0
    for item in sorted_items:
        if i+1 <= (pro_page+1)*9 and i+1>pro_page*9:
            $ x += 190
            if i%3==0:
                $ y += 170
                $ x = 515
            $ pic = item.image
            $ my_tooltip = "tooltip_profile_" + pic.replace("gui/pro_", "").replace(".png", "") # we use tooltips to describe what the item does.
            imagebutton idle pic hover pic xpos x ypos y action [NullAction()] hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] at pro_eff
            #add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(profile.items)>9:
            textbutton _("Next Page") action [SetVariable('pro_page', next_pro_page), Show("profile_screen")] xpos .475 ypos .83

screen gui_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

init -1:
    transform pro_eff: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.5 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 1.0
        on hover:
            linear 0.2 alpha 2.5

    image information = Text("INFORMATION", style="tips_top")
    #Tooltips-profile:
    image tooltip_profile_chocolate=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Generic chocolate to heal\n40 points of health.", style="tips_bottom"))
    image tooltip_profile_banana=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("A healthy banana full of potassium! You can also use it as ammo for your guns! O.O Recharges 20 bullets.", style="tips_bottom"))
    image tooltip_profile_gun=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("This is totally a person and not a lazy way of recycling assets.", style="tips_bottom"))
    image tooltip_profile_laser=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("This is totally a person and not a lazy way of recycling assets.", style="tips_bottom"))
    
screen journal:
    textbutton _("Return") action Return()