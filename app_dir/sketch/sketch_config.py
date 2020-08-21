import math

CM = 28
Base_line_width = 2
Small_line_width = 1


black = (0, 0, 0)
g1 = (0.1, 0.1, 0.1)
g2 = (0.2, 0.2, 0.2)
g3 = (0.3, 0.3, 0.3)
g4 = (0.4, 0.4, 0.4)
g5 = (0.5, 0.5, 0.5)
g6 = (0.6, 0.6, 0.6)
g7 = (0.7, 0.7, 0.7)
g8 = (0.8, 0.8, 0.8)
g9 = (0.9, 0.9, 0.9)
white = (1, 1, 1)


def perymetr(ctx):

    min_x = 2 * CM
    min_y = CM

    max_x = 29 * CM
    max_y = 20 * CM

    ctx.set_line_width(Small_line_width)

    ctx.set_source_rgb(*g8)
    # Вертикальные
    for i in range(31):
        ctx.move_to(CM * i, 0)
        ctx.line_to(CM * i, 5)
    for i in range(26):
        ctx.move_to((i + 3) * CM, min_y)
        ctx.line_to((i + 3) * CM, max_y)
    # Горизонтальные
    for j in range(22):
        ctx.move_to(0, CM * j)
        ctx.line_to(5, CM * j)
    for j in range(18):
        ctx.move_to(min_x, CM * (j + 2))
        ctx.line_to(max_x, CM * (j + 2))

    ctx.stroke()

    ctx.set_source_rgb(*g5)

    for k in range(6):
        ctx.move_to(5 * k * CM, 0)
        ctx.line_to(5 * k * CM, 595)
    for li in range(5):
        ctx.move_to(0, 5 * li * CM)
        ctx.line_to(842, 5 * li * CM)

    ctx.rectangle(min_x, min_y, max_x - min_x, max_y - min_y)

    ctx.set_source_rgb(*black)

    ctx.stroke()


def base_rectangle(ctx, start_x, start_y, delta_x, delta_y):
    ctx.rectangle(start_x * CM, start_y * CM, delta_x * CM, delta_y * CM)
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*black)
    ctx.stroke()


def thin_rectangle(ctx, start_x, start_y, delta_x, delta_y, text=""):
    ctx.rectangle(start_x * CM, start_y * CM, delta_x * CM, delta_y * CM)
    ctx.set_line_width(Small_line_width)
    ctx.set_source_rgb(*black)
    ctx.stroke()

    (xt, yt, width_t, height_t, dxt, dyt) = ctx.text_extents(text)

    ctx.move_to(
        start_x * CM + delta_x * CM / 2 - dxt / 2,
        start_y * CM + delta_y * CM / 2 - yt / 2
    )
    ctx.show_text(text)


def centered_text(ctx, start_x, start_y, delta_x, delta_y, text="hiden"):
    (xt, yt, width_t, height_t, dxt, dyt) = ctx.text_extents(text)

    ctx.move_to(
        start_x * CM + delta_x * CM / 2 - dxt / 2,
        start_y * CM + delta_y * CM / 2 - yt / 2
    )
    ctx.show_text(text)


def draw_brus_40(ctx, start_x, start_y, delta_x, delta_y):
    ctx.rectangle(start_x, start_y, delta_x, delta_y)
    ctx.set_source_rgb(*g8)
    ctx.fill_preserve()
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*black)
    ctx.stroke()


def draw_brus_18(ctx, start_x, start_y, delta_x, delta_y):
    ctx.rectangle(start_x, start_y, delta_x, delta_y)
    ctx.set_source_rgb(*g5)
    ctx.fill_preserve()
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*black)
    ctx.stroke()


def draw_carcase(ctx):

    tb40 = 0.2 * CM
    tb18 = 0.1 * CM

    sx, sy = 3 * CM, 7.5 * CM
    draw_brus_40(ctx, sx, sy, tb40, 9 * CM)

    draw_brus_40(ctx, sx + tb40, sy + 1 * CM, tb40, 1.5 * CM)
    draw_brus_40(ctx, sx + tb40, sy + 3.5 * CM, tb40, 2 * CM)
    draw_brus_18(ctx, sx + tb40 + tb40, sy + 3.5 * CM, tb18, 2 * CM)
    draw_brus_40(ctx, sx + tb40, sy + 6.5 * CM, tb40, 1.5 * CM)

    draw_brus_40(ctx, sx + tb40, sy, 4 * CM - 2 * tb40, tb40)
    draw_brus_40(ctx, sx + tb40, sy + 9 * CM, 4 * CM - 2 * tb40, - tb40)

    sx = sx + 4 * CM - tb40
    draw_brus_40(ctx, sx, sy + 1 * CM, -tb40, 1.5 * CM)
    draw_brus_40(ctx, sx, sy + 3.5 * CM, -tb40, 2 * CM)
    draw_brus_18(ctx, sx - tb40, sy + 3.5 * CM, -tb18, 2 * CM)
    draw_brus_40(ctx, sx, sy + 6.5 * CM, -tb40, 1.5 * CM)

    draw_brus_40(ctx, sx, sy, tb40, 9 * CM)


def draw_finishing_cutting(ctx):
    ctx.rectangle(8.5 * CM, 7.5 * CM, 4 * CM, 9 * CM)
    ctx.set_source_rgb(*g8)
    ctx.fill_preserve()
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*black)
    ctx.stroke()


def draw_table(ctx):
    # Таблица для размера полотна
    ctx.set_font_size(14)
    thin_rectangle(ctx, 2, 2, 4, 0.5, text="Полотно")
    ctx.set_font_size(12)
    thin_rectangle(ctx, 2, 2.5, 2, 0.5, text="Высота")
    thin_rectangle(ctx, 4, 2.5, 2, 0.5, text="Ширина")

    base_rectangle(ctx, 2, 2, 4, 2)

    # Таблица для базового бруса каркаса
    ctx.set_font_size(12)
    centered_text(
        ctx, 2, 4.5, 1.5, 0.5,
        text="Каркас"
    )
    ctx.set_font_size(10)
    centered_text(
        ctx, 2, 5, 1.5, 0.5,
        text="(грязн)"
    )
    thin_rectangle(ctx, 3.5, 4.5, 1, 0.5, text="шт")
    thin_rectangle(ctx, 3.5, 5, 1, 0.5, text="1")

    base_rectangle(ctx, 2, 4.5, 4.5, 1)

    # Таблица для декора полотна
    ctx.set_font_size(12)
    thin_rectangle(ctx, 7, 2, 4, 0.5, text="Модель")
    thin_rectangle(ctx, 7, 2.5, 4, 0.5, text="Полотно")
    thin_rectangle(ctx, 14, 2.5, 2, 0.5, text="Лутка")

    base_rectangle(ctx, 7, 2, 9, 2)

    # Таблица для бруса 40
    base_rectangle(ctx, 2, 17, 3, 3)

    # Таблица для бруса 18
    base_rectangle(ctx, 5, 17, 3, 3)

    # Таблица для чистового
    thin_rectangle(
        ctx, 8.5, 18, 2, 0.5,
        text="Длина"
    )
    thin_rectangle(
        ctx, 10.5, 18, 2, 0.5,
        text="Ширина"
    )
    base_rectangle(ctx, 8.5, 17, 4, 2.5)

    # Таблица для чернового
    thin_rectangle(ctx, 24, 17, 4, 0.5)
    thin_rectangle(ctx, 25.5, 17, 1.5, 0.5)
    for i in range(2):
        thin_rectangle(ctx, 24, 18 + i * 0.5, 4, 0.5)
        thin_rectangle(ctx, 25.5, 18 + i * 0.5, 1.5, 0.5)
    for i in range(2):
        thin_rectangle(ctx, 24, 19.5 + i * 0.5, 4, 0.5)
        thin_rectangle(ctx, 25.5, 19.5 + i * 0.5, 1.5, 0.5)

    base_rectangle(ctx, 23, 17, 1, 3.5)
    base_rectangle(ctx, 24, 17, 4, 3.5)


def strelka(ctx, sx=56, sy=56, vector=0):
    # big size
    bs = 5
    # half small size
    hss = 2
    ctx.move_to(sx, sy)
    if vector == 0:
        ctx.line_to(sx + bs, sy - hss)
        ctx.line_to(sx + bs, sy + hss)
    elif vector == 1:
        ctx.line_to(sx + hss, sy + bs)
        ctx.line_to(sx - hss, sy + bs)
    elif vector == 2:
        ctx.line_to(sx - bs, sy - hss)
        ctx.line_to(sx - bs, sy + hss)
    elif vector == 3:
        ctx.line_to(sx - hss, sy - bs)
        ctx.line_to(sx + hss, sy - bs)
    ctx.close_path()
    ctx.set_line_width(1.00)
    ctx.set_source_rgb(*black)
    # ctx.fill()
    ctx.fill_preserve()
    ctx.stroke()


def razmer_h(ctx, x, y, dx, v, d=0.5, text="пусто"):
    # x, y - начальная точка
    # dx - длина на рисунке
    # v - направление отсупа вниз(+) или вверх(-)
    # d - размер отступа на рисунке
    # text - само значенние
    ctx.set_line_width(Small_line_width)
    ctx.move_to(x, y + 4 * v)
    ctx.line_to(x, y + d * CM * v)
    ctx.move_to(x + dx, y + 4 * v)
    ctx.line_to(x + dx, y + d * CM * v)
    ctx.move_to(x + 2, y + (d * CM - 4) * v)
    ctx.line_to(x + dx - 2, y + (d * CM - 4) * v)
    ctx.stroke()
    strelka(ctx, x + 2, y + (d * CM - 4) * v, vector=0)
    strelka(ctx, x + dx - 2, y + (d * CM - 4) * v, vector=2)

    (xt, yt, width_t, height_t, dxt, dyt) = ctx.text_extents(text)

    ctx.move_to(x + dx / 2 - dxt / 2, y + (d * CM - 4) * v - 2)
    ctx.show_text(text)


def razmer_v(ctx, x, y, dy, v, d=0.5, text="пусто"):
    # x, y - начальная точка
    # dy - длина на рисунке
    # v - направление отсупа вправо(+) или влево(-)
    # d - размер отступа на рисунке
    # text - само значенние
    ctx.set_line_width(Small_line_width)
    ctx.move_to(x + 4 * v, y)
    ctx.line_to(x + d * CM * v, y)
    ctx.move_to(x + 4 * v, y + dy)
    ctx.line_to(x + d * CM * v, y + dy)
    ctx.move_to(x + (d * CM - 4) * v, y + 2)
    ctx.line_to(x + (d * CM - 4) * v, y + dy - 2)
    ctx.stroke()
    strelka(ctx, x + (d * CM - 4) * v, y + 2, vector=1)
    strelka(ctx, x + (d * CM - 4) * v, y + dy - 2, vector=3)

    (xt, yt, width_t, height_t, dxt, dyt) = ctx.text_extents(text)
    ctx.save()
    ctx.move_to(x + (d * CM - 4) * v - 2, y + dy / 2 + dxt / 2)
    ctx.rotate(3 * math.pi / 2)
    ctx.show_text(text)
    ctx.restore()
