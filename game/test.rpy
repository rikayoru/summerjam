label testt:
    menu:
        "Тест 0. Имя" if True:


            call givename
            "ебааать"
        "Тест 1. Лавмер с вариантами" if True:

            call test_one
        "Тест 2. Ачивки и Достижения" if True:
            call test_two
        "Тест 3. Система репутации" if True:
            return
        "Тест 4. Инвентарь" if True:
            return
        "Тест 5. Записи, постоянные" if True:
            return
        "Тест 6. Виды и спрайты персонажей" if True:
            return
    jump start


    return
label givename:
    $ myname = renpy.input("Как зовут вашу героиню?", length=10, allow="ячсмитьбюфывапролджэйцукенгшщзхъ-ЯЧСМИТЬБЮФЫВАПРОЛДЖЭЙЦУКЕНГШЩЗХЪ").strip()

    if myname == "":
        $ myname = "Эмма1"
    elif myname == "Трик":
        e "Эээ, это имя занято, бэйба"
        jump givename
    elif myname == "Рика":
        e "Добро пожаловать"





    my "My name is [myname]!"
    return

label test_one:

    menu:
        "Плохой вариант" if True:
            $ love_jacky -= 10
            "че обижаешь"
        "Хороший вариант" if True:
            $ love_jacky += 10
            "ой спасибооо"
        "Никакой" if True:
            "ну лох получается"
    "аааааааааааа"
    menu:
        "Еще плохой вариант" if love_jacky == 40:
            $ love_jacky -= 10
            "че обижаешь"
        "Оч хороший вариант" if love_jacky == 60:
            $ love_jacky += 10
            "ой спасибооо"
        "ашалееть" if True:
            "ну лох получается"
    "найс выбор согласись"
    "Теперь с реакциями"
    menu:
        "Пойти в подвал" if True:
            if love_jacky > 50:
                $ love_jacky += love_jacky * 0.05
                "С тобой, хоть на край света!"
            elif love_jacky == 10:

                "Эммм....ладно"
            elif love_jacky < 50:
                $ love_jacky -= 10 * 2
                "Сбрендил???!"

            "ну, в подвале мы ничего не нашли"
            "че обижаешь"
        "Городской парк" if True:





            $ love_jacky += 10
            "ой спасибооо"
        "Стоять на месте" if True:



            "ну лох получается"
    "че какаво!"
    return
label test_two:
    "hi"
    $ AddAchive("Старт", "Начинаем ебене")

    "zzzz"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc