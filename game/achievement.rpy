default persistent.AddAchive = []
init python:
    allAchievements = {
        "Старт",
        "Мастер",
        "Жесть",
        "How was the fall?"
    }
    #dictionary = ("Вопрос 1":"Ответ 1",
    #"Вопрос 2":"Ответ 2",
    #"Вопрос 3":"Ответ 3",
    #"Вопрос 4":"Ответ 4")
    #score = 0
    #colourText = None
    #globalValue = None
    #currentAnswer = None
    #hasAchive = False
    maxCountAchives = 16
    
    def AddAchive(achive, message):
        if not achive in persistent.AddAchive:
            persistent.AddAchive.append(achive)
            renpy.show_screen("notifyAchive", message, achive)

##
screen notifyAchive(message, title): #currentImage

    zorder 100
    style_prefix "notify"

    frame at notifyAchive_appear:
        #background Frame("#cvet2393489")
        # if currentImage != None:
        text "{size=+10}[title]{/size}\n[message!tq]" # \n[currentImage]

    timer 3.25 action Hide('notifyAchive')

transform notifyAchive_appear:
    on show:
        xalign .5
        alpha 1
        linear .25 yalign .5
    on hide:
        linear .5 yalign -0.5
        
##

screen AchiveScreen():
    tag menu
    python:
        lockedSlots = maxCountAchives - len(persistent.AddAchive)
    use game_menu("Достижения", scroll="viewport"): # АЙТЕМС КАРТИНКИ ЕБАНЫЕ
        grid 2 8:
            xspacing 40
            yspacing 15
            for id in allAchievements: #id, item\\\.items():
                if id in persistent.AddAchive:
                    frame:
                        xysize(400,200)
                        text id xalign .5
                        #add item xalign .5 yalign 1.0(kartinka)
            for index in range(lockedSlots):
                frame:
                    xysize(430,115)
                    #text "Заблокировано"
                    #add item xalign .5 yalign 1.0(kartinka)

