import wrap, time

wrap.world.create_world(800, 700)
wrap.add_sprite_dir("sprite")
ball = wrap.sprite.add("ball", 400, 400)
skorost_x = -4
skorost_y = 3
a = 0

@wrap.always(25)
def move_ball():
    global skorost_x, skorost_y
    wrap.sprite.move(ball, skorost_x, skorost_y)
    if wrap.sprite.get_left(ball) <= 0:
        wrap.sprite.move_left_to(ball, 0)
        skorost_x = -skorost_x
    if wrap.sprite.get_right(ball) >= 800:
        wrap.sprite.move_right_to(ball, 800)
        skorost_x = -skorost_x
    if wrap.sprite.get_top(ball) <= 0:
        wrap.sprite.move_top_to(ball,0)
        skorost_y = -skorost_y
    if wrap.sprite.get_bottom(ball) >= 700:
        wrap.sprite.move_bottom_to(ball,700)
        skorost_y = -skorost_y


@wrap.always(1000)
def skorost_ball():
    global skorost_x, skorost_y,a
    a += 1
    if a >= 10:
        skorost_x += skorost_x / 20
        skorost_y += skorost_y / 20
    print(skorost_y,skorost_x)
