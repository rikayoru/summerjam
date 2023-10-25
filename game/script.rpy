# Вы можете расположить сценарий своей игры в этом файле.
init python:
    def ChangeImage(images, speaking=False):
        if speaking == True:
            renpy.show(images)
            #
        else:
            renpy.show(images, what=im.MatrixColor(images + ".png", im.matrix.brightness(-0.5), im.matrix.saturation(0.1)))
            #
# Определение персонажей игры.
define adr = Character('Адриан', color="#000000", image = "adrian", callback=name_callback, cb_name = "adrian")
define hh = Character('hazel', color="#000000", image = "hazel", callback=name_callback, cb_name = "hazel")

# define new_textbox = False
# define jac = Character('Джейс', color="#000000", image = "jace", callback=name_callback, cb_name = "jace")
#именно с ним и его картинками чето не так

define mc = Character('[myname]', color="#000000", image = "portr") #, callback=name_callback, cb_name = "portr" 
# При объявлении ГГ  вместо имени пишется переменная с именем в квадратных скобках

# Вместо использования оператора image можете просто складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png", а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# можно сделать выборы через имеджбаттоны и поставить модуль хз чтобы нельзя пропустить
label start:
    $ myname = "Эмма"
    default maxlove = 100 # Добавляем переменную с максимальным уровнем отношений.
    default love_jacky = 50 # Переменная отношений с Джеки.
    
    #default from_current=True
    screen info: # переменные числами
        vbox:
            xminimum 400
            align(.99, .01)
            textbutton _("♥") action SetField(persistent, "info", not persistent.info) xalign 1.0
            if persistent.info:
                hbox:
                    xalign 1.0
                    text "Очки отношений: " outlines [(1, "#000", 0, 0)]
                    text "[love_jacky]" xalign 1.0 outlines [(1, "#000", 0, 0)]
                    #textbutton _("+10") action AddToSet(love_jacky, +10)
                    #textbutton _("-10") action AddToSet(love_jacky, =-10)
    screen lovemeter: # Экран с полоской отношений Джеки
        tag gameview
        vbar: # Добавляем в экран единственный элемент - вертикальную полоску
            # Прописываем параметры полоски - ширину, высоту и расположение в экране
    
            xsize 50
            ysize 345
            xalign 0.95
            yalign 0.3
    
            value AnimatedValue(value=love_jacky, range=maxlove, delay=1.0)  # Привязываем значение полоски к переменной love_jacky, а максимальное значение - к maxlove. При изменении переменной полоска будет плавно изменяться за 1 секунду (delay).
          
            # Указываем картинки для полной и пустой полоски
            # Для горизонтальной полоски нужно заменить vbar на bar, и вместо bottom_bar и top_bar укажем параметры left_bar и right_bar.
            bottom_bar Frame("gui/bar/bottom1.png",10,10)
            top_bar Frame("gui/bar/top1.png",10,10)
    screen pro_buttons:
        # style window # modal True  СТОПАЕТ ИГРУ
        imagebutton:
            xalign 0.91
            yalign 0.8
            idle "gui/button/save.png"
            hover "gui/button/save.png"
            action QuickSave()
        imagebutton:
            xalign 0.99
            yalign 0.8
            idle "gui/button/load.png"
            hover "gui/button/load.png"
            action QuickLoad()
        imagebutton:
            xalign 0.985
            yalign 0.95
            idle "gui/button/skip.png"
            hover "gui/button/skip.png"
            action Skip() alternate Skip(fast=True, confirm=True)
            # gui/button/button.png 
            

    show screen lovemeter # В игре нам остаётся только показать наш экран.
    show screen info
    scene bg room
    # $ myname = "Эмма" #прописать имя ГГ по умолчанию

    # init:
    #     define my_line = ["потуги в реакции"]
    #     define answer = ['Реплика 1', 'iuiudh88', 'sdosodi']

    # $ my_line = ["нука"]
    # $ answer = ['раз 1', 'два', 'sdosodi']
    menu:
        # e "[my_line]"
        "Start Game":
            jump strtgame
        "Test":
            jump testt
    "skerefkjrfeof"

label strtgame:
    # $ new_textbox = False
    # scene bg wew1
    scene bg wew2 with dissolve
    # show portr normal0 at left
    mc normal "\"ГеймстудияВперед\" – небольшая, но развивающаяся компания, которая движется вперед и разрабатывает супер игры, не обделяя свои проекты инновационными механиками и нестандартными решениями."
    mc smile "Обычно, подобное свойственно больше для инди-разработчиков. Все же, уникальные и новые вещи всегда сопровождаются большими рисками."
    # (СУКА ЗНАЕШЬ ПОЧЕМУ ПРОВАЛЫ У КОМПАНИИ?? ПОТОМУ ЧТО НАДО ИГРУ ГДЕ МОЖНО ГРАБИТЬ КОРОВАНЫ. НЕТ ТАКОЙ ИГРЫ ПОКА У НИХ ВОТ И ВАЛЯТСЯ)
    # (Я СЕРЬЕЗНО ЭТУ РЕПЛИКУ ТРИКУ ВПИХНУ НА СЕРЬЕЗЕ БЛЯТЬ)
    show adrian annoyed0 at right
    # второй вид на вход в здание лишний. текста мало, картинок много
    show hazel normal0 at left
    adr smile0 "Первые проекты аудитория встретила с большим успехом. Последние несколько – мягко говоря не очень."
    # $ new_textbox = True
    show screen pro_buttons
    # scene bg wew3 with dissolv

    hh smile0 "sgfdgfhdgdjfu"
    
    adr nervous0 "Студия еще держится, а в разработке находится новый продукт."
    # scene cg post2 with dissolve
    extend "У него действительно есть перспективы на рынке, поэтому лучше бы ему быть успешным."
    # scene cg post3 with dissolve
    mc normal "Потому что я – главный геймдизайнер(продуктменеджер хз кто ты) у этой игры. И если провалится он, меня вероятнее всего сократят."
    
    # (*для больших бюджетов:
    # сюда можно вставить слайдшоу: пикча здания, пикча входа(?), пропускных ворот(+рука с пропуском) близко пропуск с портретом/именем. Потом вывести гг)
    # *черный экран, звуки лифта*
    scene black with dissolve
    
    "вздох. Сегодня будет нагруженный день...так, где мой ежедневник?.."
    # *звуки приехавшего лифта, фон офиса1*

    # (*большим бюджетам:
    # "Вот он. Нашла!"
    # *вылезает на прозрачном фоне страничка ежедневника с планами на день*)
    "Сегодня у меня проведение интервью и подготовка отчета(*хз ваще)"
    "Обходя просторный офис, я подошла к своему рабочему месту." #(добралась)
    scene bg lap
    "Нужно проверить почту."
    # (интерактив покликай на капутере
    # заходим в почту, нам выводит письмо (мб по вкладкам и письмам потыкать, хз)
    "Текст письма \n Добрый день! \n Напоминаем, что у Вас сегодня в ХХ назначена встреча с журналистом издательства \"ХэЗэ\". Не забудьте забрать материалы презентации из отдела по связям с общественностью(хз).  \n еще ченибудь \n Спс, отдел хуйпоймикто \"ГеймстудияВперед\"."
    scene ofc1
label intervue:
    scene bg ofc2
    "ddd"

label athome:
    scene ghoome
    "aaa"




    

label true_start:
    "hiiihihii"

    #scene bg room
    #$ ChangeImage(adrian_annoyed, speaking=True)
    # show jace_downcast at left 
    # show adrian_annoyed at right 
    #Jace_downcast
    # "jakslas;alsl"
    # "hi"
    # $ AddAchive("Старт", "Начинаем ебене")
    #$ get_achievement(test1, trans=achievement_transform)
    "zzzz"
    return