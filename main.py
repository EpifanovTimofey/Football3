import time

import wrap

wrap.world.create_world(800, 700)
wrap.world.set_back_color(100, 200, 30)
wrap.add_sprite_dir("sprite")
ball = wrap.sprite.add("ball", 400, 350)
skorost_x = -4
skorost_y = 3
a = 0
igrok1 = 0
igrok2 = 0
player1 = wrap.sprite.add("ball", 135, 300, "Player1")
player2 = wrap.sprite.add("ball", 665, 300, "Player2")
player3 = wrap.sprite.add("ball", 400, 500, "Player3", False)
text1 = wrap.sprite.add_text(str(igrok1), 345, 50,font_size=100)
text2 = wrap.sprite.add_text(str(igrok2), 455, 50,font_size=100)
wrap.sprite.add_text(":", 400, 40,font_size=100)
mode = "centre"
time1 = time.time()


# time.sleep(3)

def move_ball():
    global skorost_x, skorost_y
    # Мячик
    if wrap.sprite.get_top(ball) <= 0:
        wrap.sprite.move_top_to(ball, 0)
        skorost_y = -skorost_y

    if wrap.sprite.get_bottom(ball) >= 700:
        wrap.sprite.move_bottom_to(ball, 700)
        skorost_y = -skorost_y
    # Отбивание мяча
    if wrap.sprite.is_collide_sprite(ball, player1):
        wrap.sprite.move_left_to(ball, wrap.sprite.get_right(player1))
        skorost_x = -skorost_x

    if wrap.sprite.is_collide_sprite(ball, player2):
        wrap.sprite.move_right_to(ball, wrap.sprite.get_left(player2))
        skorost_x = -skorost_x

    wrap.sprite.move(ball, skorost_x, 0)

    if wrap.sprite.is_collide_sprite(ball, player3) and wrap.sprite.is_visible(player3):
        if skorost_x < 0:
            wrap.sprite.move_left_to(ball, wrap.sprite.get_right(player3))
        if skorost_x > 0:
            wrap.sprite.move_right_to(ball, wrap.sprite.get_left(player3))
        skorost_x = -skorost_x

    wrap.sprite.move(ball, 0, skorost_y)

    if wrap.sprite.is_collide_sprite(ball, player3) and wrap.sprite.is_visible(player3):
        if skorost_y < 0:
            wrap.sprite.move_top_to(ball, wrap.sprite.get_bottom(player3))
        if skorost_y > 0:
            wrap.sprite.move_bottom_to(ball, wrap.sprite.get_top(player3))
        skorost_y = -skorost_y


@wrap.always(25)
def move_ball1():
    global mode
    if mode == "centre":
        time2 = time.time()
        if time2 - time1 >= 3:
            mode = "move_ball"

    if mode == "move_ball":
        move_ball()


@wrap.on_key_down(wrap.K_w, wrap.K_s, wrap.K_UP, wrap.K_DOWN, wrap.K_a, wrap.K_d, wrap.K_LEFT, wrap.K_RIGHT,
                  wrap.K_SPACE, wrap.K_v)
def move_player(key):
    global skorost_x
    if key == wrap.K_s:
        wrap.sprite.move(player1, 0, 140)
    if key == wrap.K_w:
        wrap.sprite.move(player1, 0, -140)

    if key == wrap.K_DOWN:
        wrap.sprite.move(player2, 0, 140)
    if key == wrap.K_UP:
        wrap.sprite.move(player2, 0, -140)

    if key == wrap.K_a and wrap.sprite.is_visible(player3) == True or key == wrap.K_LEFT and wrap.sprite.is_visible(
            player3) == True:
        wrap.sprite.move(player3, -100, 0)
        if wrap.sprite.is_collide_sprite(ball, player3):
            wrap.sprite.move_right_to(ball, wrap.sprite.get_left(player3))
    if key == wrap.K_d and wrap.sprite.is_visible(player3) == True or key == wrap.K_RIGHT and wrap.sprite.is_visible(
            player3) == True:
        wrap.sprite.move(player3, 100, 0)
        if wrap.sprite.is_collide_sprite(ball, player3):
            wrap.sprite.move_left_to(ball, wrap.sprite.get_right(player3))

    if key == wrap.K_SPACE:
        wrap.sprite.show(player3)
    if key == wrap.K_v:
        wrap.sprite.hide(player3)

        # Игрок 1
    if wrap.sprite.get_top(player1) <= 0:
        wrap.sprite.move_top_to(player1, 0)

    if wrap.sprite.get_bottom(player1) >= 700:
        wrap.sprite.move_bottom_to(player1, 700)
        # Игрок 2
    if wrap.sprite.get_top(player2) <= 0:
        wrap.sprite.move_top_to(player2, 0)

    if wrap.sprite.get_bottom(player2) >= 700:
        wrap.sprite.move_bottom_to(player2, 700)
        # Игрок 3
    if wrap.sprite.get_left(player3) <= 0:
        wrap.sprite.move_left_to(player3, 0)

    if wrap.sprite.get_right(player3) >= 800:
        wrap.sprite.move_right_to(player3, 800)


@wrap.always(1000)
def skorost_ball():
    global skorost_x, skorost_y, a
    if mode == "move_ball":
        a += 1
        if a >= 10:
            skorost_x += skorost_x /  20
            skorost_y += skorost_y /  20
    # print(skorost_y, skorost_x)


@wrap.always()
def ball1():
    global skorost_x, skorost_y, igrok1, igrok2, text1, text2, text3, mode, a, time1
    # wrap.sprite.remove(text1)
    # wrap.sprite.remove(text2)
    # wrap.sprite.remove(text3)
    # text1 = wrap.sprite.add_text(str(igrok1), 345, 50)
    # text2 = wrap.sprite.add_text(str(igrok2), 455, 50)
    # text3 = wrap.sprite.add_text(":", 400, 40)
    # wrap.sprite.set_size_percent(text1, 500, 500)
    # wrap.sprite.set_size_percent(text2, 500, 500)
    # wrap.sprite.set_size_percent(text3, 500, 500)

    if wrap.sprite.get_left(ball) <= 0:
        wrap.sprite.move_to(ball, 400, 350)
        igrok2 += 1
        skorost_x = -4
        skorost_y = 3
        mode = "centre"
        a = 0
        time1 = time.time()

    if wrap.sprite.get_right(ball) >= 800:
        wrap.sprite.move_to(ball, 400, 350)
        igrok1 += 1
        skorost_x = -4
        skorost_y = 3
        mode = "centre"
        a = 0
        time1 = time.time()
    wrap.sprite_text.set_text(text1,str(igrok1))
    wrap.sprite_text.set_text(text2,str(igrok2))

@wrap.on_key_down(wrap.K_q)
def dopolnenie1(key):
    if key == wrap.K_q:
        wrap.sprite.set_height_proportionally(ball, 200)


@wrap.on_key_up(wrap.K_q)
def dopolnenie2(key):
    if key == wrap.K_q:
        wrap.sprite.set_height_proportionally(ball, 40)


@wrap.on_key_down(wrap.K_x)
def chiti1(key):
    if key == wrap.K_x:
        wrap.sprite.set_height(player1, 700)
        if wrap.sprite.get_top(player1) <= 0:
            wrap.sprite.move_top_to(player1, 0)

        if wrap.sprite.get_bottom(player1) >= 700:
            wrap.sprite.move_bottom_to(player1, 700)


@wrap.on_key_up(wrap.K_x)
def chiti2(key):
    global mode
    if key == wrap.K_x:
        mode = "move_ball"
        wrap.sprite.set_height(player1, 150)
