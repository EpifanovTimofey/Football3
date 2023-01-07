import wrap
wrap.world.create_world(800,700)
wrap.add_sprite_dir("sprite")
ball = wrap.sprite.add("ball",400,400)
@wrap.always(50)
def move_ball():
    wrap.sprite.move(ball,4,4)