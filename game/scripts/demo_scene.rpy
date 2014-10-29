label demo_act_IV:
    if "1"  in cleared_items and "2" in cleared_items and "3" in cleared_items and "4" in cleared_items and "talk_1" in cleared_items and "talk_2" in cleared_items:
        $ cleared_area = 1
    
    if cleared_area == 0:
        $ current_talk = "demo_witness_talk_1"
        $ current_background = "demo_background_1"
        $ demo_background_1_response = 0
        call nav_screen_label
    
    e "Done talking/exploring."
    
    jump endgame

    return
    
screen demo_background_1:
    imagemap:
        ground "assets/backgrounds/background2.png"
        hover "assets/backgrounds/background2.png"
        hotspot (113, 173, 151, 122) action [SetVariable("demo_background_1_response", 1), Jump("demo_background_1_answer")]
        hotspot (434, 287, 161, 156) action [SetVariable("demo_background_1_response", 2), Jump("demo_background_1_answer")]
        hotspot (151, 493, 197, 176) action [SetVariable("demo_background_1_response", 3), Jump("demo_background_1_answer")]
        hotspot (714, 453, 162, 158) action [SetVariable("demo_background_1_response", 4), Jump("demo_background_1_answer")]
        
    textbutton _("Return") action [SetVariable("demo_background_1_response", 0), SetVariable("loop2", 1), Jump("demo_background_1_answer")]
        
label demo_background_1_answer:
    hide placeholder
    if demo_background_1_response == 1:
        "You clicked #1"
        $ cleared_items.append("1")
    elif demo_background_1_response == 2:
        "You clicked #2"
        $ cleared_items.append("2")
    elif demo_background_1_response == 3:
        "You clicked #3"
        $ cleared_items.append("3")
    elif demo_background_1_response == 4:
        "You clicked #4"
        $ cleared_items.append("4")
        
    show placeholder at center
    
    if loop2 == 1:
        $loop2 = 0
        hide screen demo_background_1
        jump demo_act_IV
    
    call screen demo_background_1
    
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
                
                $ cleared_items.append("talk_1")
                
            "Test 2":
                
                "Test 2"
                
                $ cleared_items.append("talk_2")
                
            "Finished talking.":
                $ loop = 0
                
    call demo_act_IV