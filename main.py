class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
    Dead = 3
@namespace
class SpriteKind:
    Ground = SpriteKind.create()
    Cloud = SpriteKind.create()
def initGround():
    global ground1, ground2
    ground1 = sprites.create(img("""
            ...................................................................................4444...........................................................................
                    ..................................................................................455554..........................................................................
                    444444444444444444444444444444444444444444444444444444444444444444444444444444444455555544444444444444444....44444444444444444444444444444444444444444444444444444
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555444455555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    554444554555555555555555555555554554444555555555555555555555555544445545555555555555455555555555555555555555555444455455555555555455444555555555555555554554445555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555444455455555555555555555555555554444545555555455555555555555445455555555444455455555444455455555555555555555545555555555555554444554555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
        """),
        SpriteKind.Ground)
    ground2 = sprites.create(img("""
            .....................................................4444..................4444...................................................................................
                    ....................................................455554................455554..................................................................................
                    444444444444444444444444444444444444444444444444444455555544444444444444445555554444444444444444444444444444444444444444444444444444444444444444444444444444444444
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555544455455555555555555555444554555555555554554444555555555555555555555555554555555555555545544445555555555555555555555555444455455555555555555555555555455444455
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555455444455555555555555545555555555555555554554444555554554444555555554544555555555555554555555545444455555555555555555555555554554444555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                    555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
        """),
        SpriteKind.Ground)
    ground1.set_position(scene.screen_width() / 2, 120)
    ground2.set_position(ground1.x + scene.screen_width(), 120)
    ground1.vx = -100
    ground2.vx = -100
    ground1.z = 2
    ground2.z = 2
def initRaptor():
    global raptor, run, jump, dead
    raptor = sprites.create(img("""
            ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ......4.4.4...666...............
                    .....45454544691164444444.......
                    .....45555555691f666665554......
                    ......44444446999999696454......
                    .............6999999996.4.......
                    .............699966666..........
                    .............69696.66...........
                    .............696966996..........
                    .............696999996..........
                    .............696666996..........
                    .............69996.66...........
                    .............69996..............
                    .............69996..............
                    .............69996..............
                    .............69996..............
                    .............69996..............
                    .............69996..............
                    ..............696...............
                    ..............696...............
                    ..............696...............
                    ..............696...............
                    ..............696...............
                    ..............6996..............
                    ..............6666..............
        """),
        SpriteKind.player)
    run = animation.create_animation(ActionKind.Walking, 100)
    run.add_animation_frame(img("""
        ................................
                ................................
                ................................
                ................................
                ................................
                ................................
                ................................
                ................................
                ......4.4.4...666...............
                .....45454544691164444444.......
                .....45555555691f666665554......
                ......44444446999999696454......
                .............6999999996.4.......
                .............699966666..........
                .............69696.66...........
                .............696966996..........
                .............696999996..........
                .............696666996..........
                .............69996.66...........
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                ..............696...............
                .............69696..............
                ............696.696.............
                .........66696...69666..........
                .........6996.....6996..........
                ..........696.....696...........
                ...........66.....66............
    """))
    run.add_animation_frame(img("""
        ................................
                ................................
                ................................
                ................................
                ................................
                ................................
                ................................
                ................................
                ......4.4.4...666...............
                .....45454544691164444444.......
                .....45555555691f666665554......
                ......44444446999999696454......
                .............6999999996.4.......
                .............699966666..........
                .............69696.66...........
                .............696966996..........
                .............696999996..........
                .............696666996..........
                .............69996.66...........
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                ..............696...............
                ..............696...............
                ..............696...............
                ..............696...............
                ..............696...............
                ..............6996..............
                ..............6666..............
    """))
    run.add_animation_frame(img("""
        ................................
                ................................
                ................................
                ................................
                ................................
                ................................
                ................................
                ................................
                ......4.4.4...666...............
                .....45454544691164444444.......
                .....45555555691f666665554......
                ......44444446999999696454......
                .............6999999996.4.......
                .............699966666..........
                .............69696.66...........
                .............696966996..........
                .............696999996..........
                .............696666996..........
                .............69996.66...........
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                ..............696...............
                .............69696..............
                ............696.696.............
                .........66696...69666..........
                .........6996.....6996..........
                ..........696.....696...........
                ...........66.....66............
    """))
    animation.attach_animation(raptor, run)
    jump = animation.create_animation(ActionKind.Jumping, 200)
    jump.add_animation_frame(img("""
        ................................
                ................................
                ..............666...............
                .............69996..............
                .............69996..............
                ..............696...............
                ..............696...............
                ..............696...............
                ......4.4.4...666...............
                .....45454544691164444444.......
                .....45555555691f666665554......
                ......44444446999999696454......
                .............6999999996.4.......
                .............699966666..........
                .............69696.66...........
                .............696966996..........
                .............696999996..........
                .............696666996..........
                .............69996.66...........
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                ..............696...............
                .............69696..............
                ............696.696.............
                .........66696...69666..........
                .........6996.....6996..........
                ..........696.....696...........
                ...........66.....66............
    """))
    animation.attach_animation(raptor, jump)
    dead = animation.create_animation(ActionKind.Dead, 200)
    dead.add_animation_frame(img("""
        ................................
                ................................
                ................................
                ................................
                ................................
                ................................
                ................................
                ................................
                ......4.4.4...11111.............
                .....45454544611111444444.......
                .....45555555611f116665554......
                ......44444446111119696454......
                .............6111119996.4.......
                .............699966666..........
                .............69696.66...........
                .............696966996..........
                .............696999996..........
                .............696666996..........
                .............69996.66...........
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                .............69996..............
                ..............696...............
                ..............696...............
                ..............696...............
                ..............696...............
                ..............696...............
                ..............6996..............
                ..............6666..............
    """))
    animation.attach_animation(raptor, dead)
    raptor.z = 3
    raptor.set_position(15, 94)

def on_button_pressed():
    if raptor.y == 94 and end == 0:
        raptor.vy = -160
        animation.set_action(raptor, ActionKind.Jumping)
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def on_on_overlap(sprite, otherSprite):
    global end
    end = 1
    animation.set_action(raptor, ActionKind.Dead)
    pause(50)
    game.over(False, effects.melt)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

cloud: Sprite = None
cactus: Sprite = None
choice = 0
dead: animation.Animation = None
jump: animation.Animation = None
run: animation.Animation = None
raptor: Sprite = None
ground2: Sprite = None
ground1: Sprite = None
end = 0
idle = None
game.set_dialog_cursor(img("""
    ................................
        ..1111111111111111111111111111..
        .111111111111111111111111111111.
        11111111111111111111111111111111
        11111111111111111111111111111111
        11111111111111111111111111111111
        11414141111166666111111111111111
        14545454111699999611111111111111
        14545454444699999644444444441111
        1455555555561f911655555555541111
        144444444446119f1644445454541111
        11111111111699966666666654541111
        11111111111699999999999961411111
        11111111111699999996969961111111
        11111111111699999999999961111111
        11111111111699966666666611111111
        111111111116999f1f1f1f1111111111
        1111111111169999f6f1f11111111111
        11111111111699999611111111111111
        11111111111699999611111111111111
        11111111111699999611111111111111
        11111111111699999611111111111111
        11111111111699999611111111111111
        11111111111699999611111111111111
        11111111111699999611111111111111
        11111111111699999611111111111111
        11111111111699999611111111111111
        11111111111699999611111111111111
        11111111111699999611111111111111
        11111111111699999611111111111111
        .111111111169999961111111111111.
        ..1111111116999996111111111111..
"""))
game.splash("Lumpy Run")
scene.set_background_color(9)
initGround()
initRaptor()
info.set_score(0)
end = 0
game.show_long_text("Press any button to jump.", DialogLayout.TOP)

def on_on_update():
    if raptor.y < 94:
        raptor.ay = 400
    else:
        raptor.ay = 0
        raptor.y = 94
        if end == 0:
            animation.set_action(raptor, ActionKind.Walking)
game.on_update(on_on_update)

def on_update_interval():
    info.change_score_by(1)
game.on_update_interval(50, on_update_interval)

def on_update_interval2():
    ground1.vx += -1
    ground2.vx += -1
game.on_update_interval(1000, on_update_interval2)

def on_update_interval3():
    global choice, cactus
    choice = randint(0, 4)
    if choice == 0:
        cactus = sprites.create_projectile_from_side(img("""
                ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ..............fff...............
                            .............f777f..............
                            .............f177f..............
                            .............f777f...f..........
                            .........f...f771f..f7f.........
                            ........f7f..f777f..f7f.........
                            ........17f..f777f..f1f.........
                            ........f7f..f777f..f7f.........
                            ........f71fff777f..f7f.........
                            ........f77777777f..f7f.........
                            .........ffff1777fff17f.........
                            .............f77777777f.........
                            .............f777fffff..........
                            .............f771f..............
                            .............f717f..............
                            .............f777f..............
                            .............f777f..............
                            .............f717f..............
                            .............f777f..............
                            .............f777f..............
            """),
            ground1.vx,
            0)
        cactus.y = 94
        cactus.z = 2
    elif choice == 1:
        cactus = sprites.create_projectile_from_side(img("""
                ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ..............fff...............
                            .............f717f..............
                            .............f777f..............
                            .............f777f..............
                            .........f...f771f...f..........
                            ........f7f..f777f..f7f.........
                            ........f1f..f777f..f71.........
                            ........f71..f777f..f7f.........
                            ........f7f..f177ffff7f.........
                            ........f7f..f77777177f.........
                            ........f7ff1f777fffff..........
                            ........f17777777f..............
                            .........fffff777f..............
                            .............f771f..............
                            .............f777f..............
                            .............1777f..............
                            .............f777f..............
                            .............f717f..............
                            .............f777f..............
                            .............f777f..............
            """),
            ground1.vx,
            0)
        cactus.y = 94
        cactus.z = 2
    elif choice == 2:
        cactus = sprites.create_projectile_from_side(img("""
                ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ..............fff........f......
                            .............f717f......f7f.....
                            .............f777f......f7f.....
                            .............f777f......f1f.....
                            .............f771f...f..f7f.....
                            .............f777f..f7f.f7f.....
                            .............f777f..f71.f7f.....
                            .........f...f777f..f7ff17f.....
                            ........f7f..f177ffff77777f.....
                            ........f71..f77777177ffff......
                            ........f7ff1f777fffff..........
                            ........f17777777f..............
                            .........fffff777f..............
                            .............f771f..............
                            .............f777f..............
                            .............1777f..............
                            .............f777f..............
                            .............f717f..............
                            .............f777f..............
                            .............f777f..............
            """),
            ground1.vx,
            0)
        cactus.y = 94
        cactus.z = 2
game.on_update_interval(1000, on_update_interval3)

def on_update_interval4():
    global cloud
    if Math.percent_chance(40):
        cloud = sprites.create_projectile_from_side(img("""
                ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            ................................
                            .........111....................
                            .......111111...................
                            ......111111111....1111.........
                            ......111111111.111111111.......
                            ......11111111111111111111......
                            .....1111111111111111111111111..
                            ..1111111111111111111111111111..
                            .11111111111111111111111111111..
                            .11111111111111111111111111111..
                            .1111111111111111111111111111...
                            .1111111111111111111111111111...
                            ..1111111111111111111111111111..
                            ..1111111111111111111111111111..
                            ..1111111111111111111111111111..
                            ..1111111.11111111111111111111..
                            ...........111111111..1111111...
                            ............11111...............
                            ................................
                            ................................
                            ................................
            """),
            ground1.vx / 4,
            0)
        cloud.y = randint(20, 60)
        cloud.set_kind(SpriteKind.Cloud)
        cloud.z = 1
game.on_update_interval(1500, on_update_interval4)

def on_forever():
    if ground2.x < -1 * (scene.screen_width() / 2):
        ground2.x = ground1.x + scene.screen_width()
forever(on_forever)

def on_forever2():
    if ground1.x < -1 * (scene.screen_width() / 2):
        ground1.x = ground2.x + scene.screen_width()
forever(on_forever2)
