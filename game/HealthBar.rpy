screen bars():

      bar :
          value lala_hp 
          range 100
          left_bar "lalalife fullhp.png"
          right_bar "lalalife emptyhp.png"
          xysize(400,50)
          xalign 0.01
          yalign 0.01
      text "{b}[lala_hp]/100" ypos 0.01 xpos 0.075
      text "{size=+10}{b}Lala{/size}" ypos 0.08 xpos 0.01
      
      bar :
            value lala_mp 
            range 50
            left_bar "lalalife full.png"
            right_bar "lalalife empty.png"
            xysize(200,50)
            xalign 0.01
            yalign 0.05
      text "{b}[lala_mp]/50" ypos 0.0475 xpos 0.035
        
      bar :
          value monster
          range 100
          left_bar "lalalife fullhp.png"
          right_bar "lalalife emptyhp.png"
          xysize(400,50)
          xalign 0.99
          yalign 0.01
      text "{b}[monster]/100" ypos 0.01 xpos 0.855
      text "{size=+10}{b}{color=#ff0000}Monster{/color}{/size}" ypos 0.05 xpos 0.785