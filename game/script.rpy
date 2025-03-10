# Vous pouvez placer le script de votre jeu dans ce fichier.
# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
#Fade tout l'écran, disolve ciblé
#vpunch and hpunch pour shake cam
#init:
#   transform (nameVariable)
#       zoom 2
#       xpos 0.5
#       ypos 0.5
#play music or sound "nameMusique" fadein 0.5 volume 1 // fade music
#stop music "nameMusique" fadeout 0.5 volume 0
#pause 2.0 // wait tout cour
#{w=2.0} // wait pendant txt
#define variable = "..."
#"my name is [name]"
#renpy.input
#strip().capitalize()
#%(characterName)s
#jump labelName
          
# Déclarez les personnages utilisés dans le jeu.
define you = Character('You', color="#ffffff")
define unknown = Character('???')
define lala = Character('Lala', color="#FFC0CB")
define world = Character('{b}World', color="#808080")
define enemy = Character('Monster', color="#ff0000")
default player_trust = 0
default flag_end = "0"
default remaining_HPpotion = 5


# Le jeu commence ici
label start:

    #scene #nameBackground
    #show #namePerso at #where
    image frame = im.FactorScale("frame.png", 6)
    scene frame
    
    unknown "..."
    unknown "h.."
    unknown "hey ..."   
    unknown "WAKE UP !!!" with vpunch
    image bgdonjon normal = im.FactorScale("bgdonjon normal.png", 1.1)
    scene bgdonjon normal with dissolve
    scene frame with dissolve
    scene bgdonjon normal with dissolve
    scene frame with dissolve
    scene bgdonjon normal with dissolve
    you "Ahhhhhhhhh !"
    unknown "hello"
    
    menu: #menu de choix  
        "WHAT !?":
            unknown "?!"
            $ flag_q1 = "1"
            
        "WHO ARE YOU !?":
            unknown "?!"
            $ flag_q1 = "2"
            
        "WHAT'S APENING ?":
            unknown "?!"
            $ flag_q1 = "3"
            
        "WHERE AM I ?":
            unknown "?!"
            $ flag_q1 = "4"
        
            
    
    menu: #menu de choix  
        "WHAT !?" if flag_q1 != "1":
            unknown "Hey !"
            $ flag_q2 = "1"
        "WHO ARE YOU !?" if flag_q1 != "2":
            unknown "Hey !"
            $ flag_q2 = "2"
        "WHAT'S APENING ?" if flag_q1 != "3":
            unknown "Hey !"
            $ flag_q2 = "3"
        "WHERE AM I ?" if flag_q1 != "4":
            unknown "Hey !"
            $ flag_q2 = "4"
    
           
    menu: #menu de choix  

        "WHAT !?" if flag_q1 != "1" and flag_q2 != "1":
            unknown "HEY !!!" with vpunch
        "WHO ARE YOU !?" if flag_q1 != "2" and flag_q2 != "2":
            unknown "HEY !!!" with vpunch
        "WHAT'S APENING ?" if flag_q1 != "3" and flag_q2 != "3":
            unknown "HEY !!!" with vpunch
        "WHERE AM I ?" if flag_q1 != "4" and flag_q2 != "4":
            unknown "HEY !!!" with vpunch
        "<thinking> Didn't it already happen before ?" if flag_end == "1":
            you "Maybe i'm just imagining things"
            $ player_trust +=1
            world "Player trust +1, actual player trust = [player_trust]"
            
            
                    
    unknown "Calm down ..."
    you "Ok,{w=1.0} ok, {w=1.0} sorry for that "
    unknown "Don't worry it's okay."
    you "Thanks, otherwise, who are you ?"
    lala "Me ? I'm Lala"
    ".{w=1.0}.{w=1.0}."
    lala "So, aren't you gonna present yourself ?"
    you "My name ?"
    you "What was my name again ?"
    $ name = renpy.input("What is your name ?")
    $ name = name.strip().capitalize()
    lala "So ?"
    you "Yhea, sorry my name is [name]"
    lala "Ok [name], can i ask you why you are sleeping here ?"
    
  
    menu: #menu de choix
    
        "I don't know.":
            lala "You don't ? [name] do you even know WHERE you are ?"
            $ player_trust +=1
            $ flag_q3 = "1"
            world "Player trust +1, actual player trust = [player_trust]"
            
        "I thought it was a good place to sleep.":
            lala "[name] do you really think this is a good place to sleep ?"
            $ flag_q3 = "2"
             
label Question:    
    menu: #menu de choix
        
            "I don't, but you do right ?" if flag_q3 == "1":
                lala "<Pfiou> Ok [name]."
                lala "Here you are in the center of one of the most DANGEROUS dungeon that there is."
                $ player_trust +=1
                world "Player trust +1, actual player trust = [player_trust]"
                
            "Is this that BAD of a place to sleep ?" if flag_q3 == "2":
                lala "Are you REALLY asking me this question"
                menu :
                    "Yes":
                        lala "<ugh> YES, it is." 
                        lala "Here you are in the center of one of the most DANGEROUS dungeon that there is."
                        $ flag_q4 = "1"
                    "No":
                        lala "<oof> You reassure me"
                        $ flag_q4 = "2"
                        jump Question
                
            "Can you tell me where we are ?":
                lala "Here you are in the center of one of the most DANGEROUS dungeon that there is."
                $ player_trust +=1
                world "Player trust +1, actual player trust = [player_trust]"
                
    you "A dungeon ? you mean the ones with monsters ?"
    lala "Yes, this ones."
    lala "Now you do understand why i'm skeptical about you being here [name], right ?"
    you "Yhea <haha>"
    
    menu:
        "Shout out to dodge":
            if player_trust >= 2:
                lala "<dodge>"
                $ player_trust += 2
                world "Player trust +2, actual player trust = [player_trust]"
                lala "Come behind me!{w=0.5} Quick!!!"
                $ flag_norm = "1" 
                jump Fight
            if player_trust == 1:
                lala "<hesitantly dodge>"
                lala "<get hurt> aie!"
                $ player_trust += 1
                world "Player trust +1, actual player trust = [player_trust]"
                lala "<ugh>[name] get behind me!"
                $ flag_norm = "2"
                jump Fight
            if player_trust <= 0:
                lala "What ?"
                lala "<doesn't dodge>"
                lala "<get seriously hurt by the attack and fall on the ground>"
                "She look at you with eyes filled with fear and begging for help"
                menu:
                    "Let her die and try an escape":
                        "<Lala Died>"
                        "While the monster is busy devouring her you try to escape"
                        "The monster see you and jump on you"
                        "While the monster is slowly eating you, in your last moment of consciousness you take a last look at Lala's body and think deeply"
                        default preferences.text_cps = 5
                        "<You Died>"
                        default preferences.text_cps = 40
                        jump BadEnd
                    
                    "Try to help her":
                        "When the monster is going for the last hit, you jump on it and manage to make it fall"
                        "While the monster try to come back on it's feet you take a look back and see a dead Lala looking at you"
                        "<Lala Died>"
                        "Shaken by what your seeing you don't the incoming attack and die"
                        default preferences.text_cps = 5
                        "<You Died>"
                        default preferences.text_cps = 40
                        jump BadEnd
        
        "Jump on her":
            if player_trust >= 2:
                you "<jump on her>"
                lala "[name]! What are y-" with hpunch
                "You successfully manage to make the both of you escape attack"
                $ player_trust += 2
                world "Player trust +2, actual player trust = [player_trust]"
                lala "Come behind me!{w=0.5} Quick!!!" 
                $ flag_norm = "1"
                jump Fight
            if player_trust == 1:
                you "<jump on her"
                "<You try to jump on her, but Lala dodge you and luckily almost dodge the incoming attack too"
                lala "<get hurt> aie!" with hpunch
                $ player_trust += 1
                world "Player trust +1, actual player trust = [player_trust]"
                lala "<ugh>[name] get behind me!"
                $ flag_norm = "2"
                jump Fight
            if player trust <= 0:
                you "<jump on her>"
                "You try to jump on her, but Lala dodge and mistakenly cut you"
                "While your bleeding to death you witness Lala fight the creature while looking at you with sorry eyes"
                "<You died>"
                jump BadEnd

label Fight:
    image bgdonjon fight = im.FactorScale("bgdonjon fight.png", 1.1)
    scene bgdonjon fight with vpunch
    show screen bars
    
    if flag_norm == "1":
        $ lala_hp = 100
        $ monster = 100
        $ lala_mp = 50
    
    if flag_norm == "2":
        $ lala_hp = 70
        $ monster = 100
        $ lala_mp -= 10
        
    $ turn = "Lala"
    $ potion_used = "0"
    
    you "What is that thing ?!"
    lala "That is one of the monster i was talking about"
    lala "Sorry, but we don't have time for small talk ! Be on your guard and pay attention, i'll take care of it"
    jump combat

label combat:
    scene bgdonjon fight

    while lala_hp > 0 and monster > 0:
        
        if turn == "Lala":
            $ flag_defense = "0"
            menu:
                "Attack":
                    $ damage = renpy.random.randint(10, 20)
                    $ monster -= damage
                    "Lala attacked and inflicted [damage] damage !"
                    if damage >= 18:
                        enemy "<Growls>"
                
                "Magic":
                    if lala_mp >= 10:
                        $ damage = renpy.random.randint(20, 30)
                        $ monster -= damage
                        $ lala_mp -= 10
                        "Lala used a magic attack and inflicted [damage] damage !"
                        if damage >= 28:
                            enemy "Gharg!"
                    else:
                        lala "I don't have enough MP!"
                        jump combat  # Recommence le choix
            
                "Defense":
                    lala "Lala is prepared to counter the next attack"
                    $ flag_defense = "1"
                
                "Life Potion" if potion_used == "0" and remaining_HPpotion >= 1:
                    if lala_hp < 100:
                        $ hpBack = renpy.random.randint(10, 20)
                        $ lala_hp = min(100, lala_hp + hpBack)
                        $ potion_used = "1"
                        $ remaining_HPpotion -= 1
                        "Lala used a potion (remain [remaining_HPpotion]), she healed back [hpBack] HP"
                        jump combat
                    else:
                        lala "I'm not even hurt!"
                        jump combat  # Recommence le choix
            
            $ turn = "enemy"

        else:
            $ potion_used = "0"
            $ enemy_damage = renpy.random.randint(10, 25)
            if flag_defense == "1":
                $ enemy_damage -= 8
            $ lala_hp -= enemy_damage
            "Monster attacked!"
            "Lala took [enemy_damage] damage!"
            
            $ turn = "Lala"
    
        if lala_hp <= 0:
            lala "I'm sorry..."
            hide screen bars
            jump BadEnd  # Fin du combat
    
        if monster <= 0:
            lala "We survived!"
            hide screen bars
            jump afterFight  # Fin du combat

label afterFight:
    scene bgdonjon normal with wiperight
    
    
label NormalEnd:
    image bgdonjon escape = im.FactorScale("bgdonjon escape.png", 1.1)
    scene bgdonjon escape with dissolve
    "End"
    return
label BadEnd:
    image bgdonjon fail = im.FactorScale("bgdonjon fail.png", 1.1)
    scene bgdonjon fail with dissolve
    "Bad End"
    $ flag_end = "1"
    jump start
label GoodEnd:
    image bgdonjon goodend = im.FactorScale("bgdonjon goodend.png", 1.1)
    scene bgdonjon goodend with dissolve
    "Good End"
    return