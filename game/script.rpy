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

# images
image lala angry = im.FactorScale("Girl/Angry.png", 0.7)
image lala annoyed = im.FactorScale("Girl/annoyed.png", 0.7)
image lala annoyed2 = im.FactorScale("Girl/annoyed2.png", 0.7)
image lala awkward = im.FactorScale("Girl/awkward.png", 0.7)
image lala calmblush2 = im.FactorScale("Girl/Calm blush 2.png", 0.7)
image lala happy1 = im.FactorScale("Girl/Happy 1.png", 0.7)
image lala happy2 = im.FactorScale("Girl/Happy 2.png", 0.7)
image lala happyblush = im.FactorScale("Girl/Happy blush.png", 0.7)
image lala normal = im.FactorScale("Girl/Normal.png", 0.7)
image lala sad = im.FactorScale("Girl/Sad.png", 0.7)
image lala scared = im.FactorScale("Girl/Scared.png", 0.7)
image lala shoked = im.FactorScale("Girl/Shoked.png", 0.7)
image lala smileblush2 = im.FactorScale("Girl/smile blush 2.png", 0.7)
image lala smile = im.FactorScale("Girl/smile1.png", 0.7)
image lala smile2 = im.FactorScale("Girl/smile2.png", 0.7)
image lala surprisedblush2 = im.FactorScale("Girl/Surprised blush 2.png", 0.7)
image lala surprisedblush = im.FactorScale("Girl/Surprised blush.png", 0.7)
image lala surprised = im.FactorScale("Girl/Surprised.png", 0.7)
image monster = im.FactorScale("Monster1.png", 3.2)

# Le jeu commence ici
label start:

    #scene #nameBackground
    #show #namePerso at #where
    image frame = im.FactorScale("frame.png", 6)
    scene frame
    stop music
    default lala_mp = 50
    default lala_hp = 100
    default monster = 100
    
    
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
    show lala annoyed with dissolve
    you "Ahhhhhhhhh !"
    play music "Sound/IG Song.mp3" fadeout 0.5 fadein 0.5 volume 0.5 loop
    show lala annoyed2
    unknown "hello"
    
    menu: #menu de choix  
        "WHAT !?":
            show lala surprised
            unknown "?!"
            $ flag_q1 = "1"
            
        "WHO ARE YOU !?":
            show lala surprised
            unknown "?!"
            $ flag_q1 = "2"
            
        "WHAT'S APENING ?":
            show lala surprised
            unknown "?!"
            $ flag_q1 = "3"
            
        "WHERE AM I ?":
            show lala surprised
            unknown "?!"
            $ flag_q1 = "4"
        
            
    
    menu: #menu de choix  
        "WHAT !?" if flag_q1 != "1":
            show lala annoyed2
            unknown "Hey !"
            $ flag_q2 = "1"
        "WHO ARE YOU !?" if flag_q1 != "2":
            show lala annoyed2
            unknown "Hey !"
            $ flag_q2 = "2"
        "WHAT'S APENING ?" if flag_q1 != "3":
            show lala annoyed2
            unknown "Hey !"
            $ flag_q2 = "3"
        "WHERE AM I ?" if flag_q1 != "4":
            show lala annoyed2
            unknown "Hey !"
            $ flag_q2 = "4"
    
           
    menu: #menu de choix  

        "WHAT !?" if flag_q1 != "1" and flag_q2 != "1":
            show lala angry
            unknown "HEY !!!" with vpunch
        "WHO ARE YOU !?" if flag_q1 != "2" and flag_q2 != "2":
            show lala angry
            unknown "HEY !!!" with vpunch
        "WHAT'S APENING ?" if flag_q1 != "3" and flag_q2 != "3":
            show lala angry
            unknown "HEY !!!" with vpunch
        "WHERE AM I ?" if flag_q1 != "4" and flag_q2 != "4":
            show lala angry
            unknown "HEY !!!" with vpunch
        "<thinking> Didn't it already happen before ?" if flag_end == "1":
            you "Maybe i'm just imagining things"
            $ player_trust +=1
            world "Player trust +1, actual player trust = [player_trust]"
            
            
         
    show lala annoyed           
    unknown "Calm down !"
    you "Ok,{w=1.0} ok, {w=1.0} sorry for that "
    show lala annoyed2
    unknown "Don't worry it's okay."
    you "Thanks, otherwise, who are you ?"
    show lala surprised
    lala "Me ? I'm Lala"
    show lala normal
    ".{w=1.0}.{w=1.0}."
    show lala smile2
    lala "So, aren't you gonna present yourself ?"
    show lala smile
    you "My name ?"
    you "What was my name again ?"
    $ name = renpy.input("What is your name ?")
    $ name = name.strip().capitalize()
    show lala smile2
    lala "So ?"
    show lala smile
    you "Yhea, sorry my name is [name]"
    show lala smile2
    lala "Ok [name], can i ask you why you are sleeping here ?"
    
  
    menu: #menu de choix
    
        "I don't know.":
            show lala surprised
            lala "You don't ? [name] do you even know WHERE you are ?"
            $ player_trust +=1
            $ flag_q3 = "1"
            world "Player trust +1, actual player trust = [player_trust]"
            
        "I thought it was a good place to sleep.":
            show lala awkward
            lala "[name] do you really think this is a good place to sleep ?"
            $ flag_q3 = "2"
             
label Question:    
    menu: #menu de choix
        
            "I don't, but you do right ?" if flag_q3 == "1":
                show lala normal
                lala "<Pfiou> Ok [name]."
                show lala smile2
                lala "Here you are in the center of one of the most DANGEROUS dungeon that there is."
                show lala smile
                $ player_trust +=1
                world "Player trust +1, actual player trust = [player_trust]"
                
            "Is this that BAD of a place to sleep ?" if flag_q3 == "2":
                show lala annoyed2
                lala "Are you REALLY asking me this question"
                show lala annoyed
                menu :
                    "Yes":
                        show lala annoyed2
                        lala "<ugh> YES, it is." 
                        lala "Here you are in the center of one of the most DANGEROUS dungeon that there is."
                        $ flag_q4 = "1"
                        show lala annoyed
                        
                    "No":
                        show lala awkward
                        lala "<oof> You reassure me"
                        $ flag_q4 = "2"
                        jump Question
                
            "Can you tell me where we are ?":
                show lala smile2
                lala "Here you are in the center of one of the most DANGEROUS dungeon that there is."
                $ player_trust +=1
                show lala smile
                world "Player trust +1, actual player trust = [player_trust]"
    
                
    you "A dungeon ? you mean the ones with monsters ?"
    show lala awkward
    lala "Yes, this ones."
    lala "Now you do understand why i'm skeptical about you being here [name], right ?"
    you "Yhea <haha>"
    
    menu:
        "Shout out to dodge":
            if player_trust >= 2:
                show lala shoked
                play sound "Sound/Escape Attack.wav"
                lala "<dodge>"
                hide lala with dissolve
                $ player_trust += 2
                world "Player trust +2, actual player trust = [player_trust]"
                show lala surprisedblush
                lala "Thanks"
                lala "Now come behing me"
                show lala annoyed
                $ flag_norm = "1" 
                jump Fight
            if player_trust == 1:
                show lala surprised
                lala "<hesitantly dodge>"
                play sound "Sound/Avoid get hit.wav"
                hide lala with dissolve
                lala "<get hurt> aie!"
                $ player_trust += 1
                world "Player trust +1, actual player trust = [player_trust]"
                show lala angry
                lala "<ugh>[name] get behind me ! I'll kill it" with vpunch
                $ flag_norm = "2"
                jump Fight
            if player_trust <= 0:
                show lala annoyed2
                lala "What ?"
                hide lala with dissolve
                lala "<doesn't dodge>"
                play sound "Sound/Get hit.wav"
                lala "<get seriously hurt by the attack and fall on the ground>" with hpunch
                show lala scared
                "She look at you with eyes filled with fear and begging for help"
                menu:
                    "Let her die and try an escape":
                        show lala sad with dissolve
                        "<Lala Died>"
                        hide lala with dissolve
                        "While the monster is busy devouring her you try to escape"
                        "The monster see you and jump on you" with hpunch
                        "While the monster is slowly eating you, in your last moment of consciousness you take a last look at Lala's body and think deeply"
                        default preferences.text_cps = 5
                        "<You Died>"
                        default preferences.text_cps = 40
                        jump BadEnd
                    
                    "Try to help her":
                        hide lala with dissolve
                        "When the monster is going for the last hit, you jump on it and manage to make it fall"
                        show lala sad
                        "While the monster try to come back on it's feet you take a look back and see a near dead Lala looking at you"
                        hide lala with dissolve
                        "<Lala Died>"
                        "Shaken by what your seeing you don't the incoming attack and die"
                        default preferences.text_cps = 5
                        "<You Died>"
                        default preferences.text_cps = 40
                        jump BadEnd
        
        "Jump on her":
            if player_trust >= 2:
                hide lala
                you "<jump on her>"
                show lala surprisedblush2 with dissolve
                lala "[name]! What are y-" with hpunch
                play sound "Sound/Escape Attack.wav"
                "You successfully manage to make the both of you escape attack"
                $ player_trust += 2
                world "Player trust +2, actual player trust = [player_trust]"
                lala "Come behind me!{w=0.5} Quick!"
                show lala smileblush2
                $ flag_norm = "1"
                jump Fight
            if player_trust == 1:
                you "<jump on her>"
                show lala surprisedblush with dissolve
                pause 0.5
                hide lala with dissolve
                "<You try to jump on her, but Lala dodge you and luckily almost entirely dodge the incoming attack too"
                play sound "Sound/Avoid get hit.wav"
                lala "<get hurt> aie!" with hpunch
                $ player_trust += 1
                world "Player trust +1, actual player trust = [player_trust]"
                show lala surprised
                lala "<ugh>[name] get behind me!"
                $ flag_norm = "2"
                jump Fight
            if player trust <= 0:
                you "<prepare to jump on her>"
                show lala shoked
                pause 0.5
                hide lala with dissolve
                "You try to jump on her, but Lala dodge and hit you"
                play sound "Sound/full hit.wav" volume 2.0
                "On landing you hit your head on the ground"
                show lala annoyed2
                lala "Why did you do that ?"
                you "..."
                show lala awkward
                lala "hey can you hear me ?"
                you "..."
                lala "<Try to lift you>"
                "While trying to lift you a lot of blood start flawing of your head"
                show lala scared
                lala "Hey! are you okay !"
                lala "Respond !!"
                lala "<Hear a strange sound>"
                show lala sad
                lala "so you where trying to help me ... {w=0.5}Sorry"
                "While your bleeding to death you witness Lala fight the creature while looking at you with sorry eyes"
                "<You died>"
                jump BadEnd

label Fight:
    image bgdonjon fight = im.FactorScale("bgdonjon fight.png", 1.1)
    scene bgdonjon fight with vpunch
    stop music
    play music "Sound/Fight Song.mp3" fadeout 0.5 fadein 0.5 volume 0.5 loop
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
    
    show monster
    you "What is that thing ?!"
    show lala annoyed2 at left
    show monster at right
    lala "That is one of the monster i was talking about"
    lala "Sorry, but we don't have time for small talk ! Be on your guard and pay attention, i'll take care of it"
    jump combat

label combat:
    scene bgdonjon fight
    show lala annoyed at left
    show monster at right

    while lala_hp > 0 and monster > 0:
        
        if turn == "Lala":
            $ flag_defense = "0"
            menu:
                "Attack":
                    $ damage = renpy.random.randint(10, 20)
                    $ monster -= damage
                    show lala angry
                    play sound "Sound/Attack.mp3" volume 3
                    "Lala attacked and inflicted [damage] damage !" with vpunch
                    show lala annoyed at left
                    if damage >= 18:
                        enemy "<Growls>"
                
                "Magic":
                    if lala_mp >= 10:
                        $ damage = renpy.random.randint(20, 30)
                        $ monster -= damage
                        $ lala_mp -= 10
                        show lala angry
                        play sound "Sound/Fireball.wav" volume 2
                        pause 0.1
                        play sound "Sound/fb explo.wav" volume 2
                        "Lala used a magic attack (-10MP) and inflicted [damage] damage !" with vpunch
                        show lala annoyed at left
                        if damage >= 28:
                            enemy "Gharg!"
                    else:
                        show lala annoyed2 at left
                        lala "I don't have enough MP!"
                        show lala annoyed at left
                        jump combat  # Recommence le choix
            
                "Defense":
                    play sound "Sound/Protect.mp3" volume 2
                    lala "Lala is prepared to counter the next attack"
                    $ flag_defense = "1"
                
                "Life Potion" if potion_used == "0" and remaining_HPpotion >= 1:
                    if lala_hp < 100:
                        $ hpBack = renpy.random.randint(10, 20)
                        $ lala_hp = min(100, lala_hp + hpBack)
                        $ potion_used = "1"
                        $ remaining_HPpotion -= 1
                        show lala surprisedblush at left
                        play sound "Sound/Potion.wav"
                        "Lala used a potion (remain [remaining_HPpotion]), she healed back [hpBack] HP"
                        show lala annoyed
                        jump combat
                    else:
                        show lala annoyed2 at left
                        lala "I'm not even hurt!"
                        show lala annoyed at left
                        jump combat  # Recommence le choix
            
            $ turn = "enemy"

        else:
            $ potion_used = "0"
            $ enemy_damage = renpy.random.randint(10, 25)
            show lala shoked
            "Monster attack!"
            if flag_defense == "1":
                $ enemy_damage -= 8
            play sound "Sound/Protect sucess.wav"
            $ lala_hp -= enemy_damage
            show lala scared at left
            "Lala took [enemy_damage] damage!" with hpunch
            $randResponse = renpy.random.choice (['ugh','You!','You annoy me!'])
            show lala angry at left
            lala "[randResponse]"
            show lala annoyed at left
            
            $ turn = "Lala"
    
        if lala_hp <= 0:
            show lala sad at center with dissolve
            lala "I'm sorry..."
            hide screen bars
            jump BadEnd  # Fin du combat
    
        if monster <= 0:
            hide monster
            show lala happyblush at center with dissolve
            lala "We survived!"
            hide screen bars
            if player_trust <= 2:
                jump NormalEnd  # Fin du combat
            if player_trust >= 3:
                jump GoodEnd
    
    
label NormalEnd:
    stop music
    hide lala
    image bgdonjon escape = im.FactorScale("bgdonjon escape.png", 1.1)
    scene bgdonjon escape with dissolve
    play music "Sound/IG Song.mp3" fadeout 0.5 fadein 0.5 volume 0.5 loop
    show lala happy2
    lala "[name] here's the exit"
    show lala happy1
    you "Yes ..."
    show lala surprised
    lala "Are you okay ?"
    show lala smile
    menu: #menu de choix  
            "Yhea, everithing is okay. Thanks":
                show lala happy2
                lala "No problem i was happy to help goodbye"
                show lala happy1
                you "ah..."
                show lala happy2
                lala "[name] you want something ?"
                show lala happyblush
                you "No it's okay bye"
                
            "Can we stay together ?":
                show lala smile2
                lala "Sorry i still have things to do"
                show lala smile
                you "So it's a goodbye ?"
                show lala smile2
                lala "Yes, it is. Happy to have met you"
                show lala smile
                you "Me too, Goodbye"
                show lala happy1
                lala "Hum"
    hide lala with dissolve
    "End"
    return
label BadEnd:
    stop music
    hide lala
    image bgdonjon fail = im.FactorScale("bgdonjon fail.png", 1.1)
    scene bgdonjon fail with dissolve
    "Bad End"
    $ flag_end = "1"
    jump start
label GoodEnd:
    stop music
    hide lala
    play music "Sound/IG Song.mp3" fadeout 0.5 fadein 0.5 volume 0.5 loop
    image bgdonjon goodend = im.FactorScale("bgdonjon goodend.png", 1.1)
    scene bgdonjon goodend with dissolve
    show lala happy2
    lala "[name] here's the exit"
    show lala happyblush
    you "Yes ..."
    show lala surprisedblush
    lala "Are you okay ?"
    you "Yhea, everithing is okay."
    you "Thanks"
    show lala happy2
    lala "No problem i was happy to help"
    show lala smileblush2
    you "Can..{w=0.5}Can i stay with you a bit longueur ?"
    show lala surprisedblush
    pause 0.5
    show lala surprisedblush2
    pause 0.5
    lala "Are you serious ?"
    menu:
        "Yes":
            show lala smileblush2
            pause 0.5
            show lala calmblush2
            pause 0.5
            show lala smileblush2
            "Good End"
                        
        "No":
            show lala shoked
            lala "Am i funny to you ?"
            show lala angry
            lala "Go die"
            show lala sad
            pause 2.0
            hide lala with dissolve
            "GO DIE YOU JERK!!!"
            "Jerk End"
                    
    return