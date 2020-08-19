
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


def thin_rectangle(ctx, start_x, start_y, delta_x, delta_y):
    ctx.rectangle(start_x * CM, start_y * CM, delta_x * CM, delta_y * CM)
    ctx.set_line_width(Small_line_width)
    ctx.set_source_rgb(*black)
    ctx.stroke()


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
    thin_rectangle(ctx, 2, 2.5, 2, 0.5)
    thin_rectangle(ctx, 4, 2.5, 2, 0.5)
    thin_rectangle(ctx, 2, 3, 2, 1)

    base_rectangle(ctx, 2, 2, 4, 2)

    ctx.set_font_size(14)
    ctx.move_to(3 * CM, 2.4 * CM)
    ctx.show_text("Полотно")
    ctx.set_font_size(12)
    ctx.move_to(2.3 * CM, 2.9 * CM)
    ctx.show_text("Высота")
    ctx.move_to(4.2 * CM, 2.9 * CM)
    ctx.show_text("Ширина")

    # Таблица для базового бруса каркаса
    thin_rectangle(ctx, 3.5, 4.5, 1, 0.5)
    thin_rectangle(ctx, 3.5, 5, 1, 0.5)

    base_rectangle(ctx, 2, 4.5, 4.5, 1)

    ctx.set_font_size(12)
    ctx.move_to(2.1 * CM, 4.9 * CM)
    ctx.show_text("Каркас")
    ctx.set_font_size(10)
    ctx.move_to(2.2 * CM, 5.4 * CM)
    ctx.show_text("(грязн)")
    ctx.move_to(3.8 * CM, 4.9 * CM)
    ctx.show_text("шт")
    ctx.move_to(3.9 * CM, 5.4 * CM)
    ctx.show_text("1")
    ctx.set_font_size(18)
    ctx.move_to(4.7 * CM, 5.2 * CM)
    ctx.show_text("40х")

    # Таблица для декора полотна
    thin_rectangle(ctx, 7, 2, 3, 0.5)
    thin_rectangle(ctx, 10, 2, 5, 0.5)
    thin_rectangle(ctx, 7, 2.5, 6, 0.5)
    thin_rectangle(ctx, 13, 2.5, 2, 0.5)
    thin_rectangle(ctx, 13, 3, 2, 1)

    base_rectangle(ctx, 7, 2, 8, 2)

    ctx.set_font_size(12)
    ctx.move_to(7.5 * CM, 2.4 * CM)
    ctx.show_text("Модель")
    ctx.move_to(7.5 * CM, 2.9 * CM)
    ctx.show_text("Полотно")
    ctx.move_to(13.5 * CM, 2.9 * CM)
    ctx.show_text("Лутка")

    # Таблица для бруса 40
    for i in range(5):
        thin_rectangle(ctx, 2, 17.5 + i * 0.5, 1.5, 0.5)
        thin_rectangle(ctx, 3.5, 17.5 + i * 0.5, 1.5, 0.5)

    base_rectangle(ctx, 2, 17, 3, 3.5)

    # Таблица для бруса 18
    thin_rectangle(ctx, 5, 17.5, 1.5, 0.5)
    thin_rectangle(ctx, 6.5, 17.5, 1.5, 0.5)

    base_rectangle(ctx, 5, 17, 3, 3)

    # Таблица для чистового
    thin_rectangle(ctx, 8.5, 18, 2, 0.5)
    thin_rectangle(ctx, 10.5, 18, 2, 0.5)
    thin_rectangle(ctx, 8.5, 18.5, 2, 1)

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
