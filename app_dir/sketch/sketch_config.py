
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

    ctx.set_line_width(Small_line_width)

    ctx.set_source_rgb(*g8)
    # Вертикальные
    for i in range(31):
        ctx.move_to(CM * i, 0)
        ctx.line_to(CM * i, 5)
    for i in range(26):
        ctx.move_to((i + 3) * CM, CM)
        ctx.line_to((i + 3) * CM, CM * 21)
    # Горизонтальные
    for j in range(22):
        ctx.move_to(0, CM * j)
        ctx.line_to(5, CM * j)
    for j in range(18):
        ctx.move_to(2 * CM, CM * (j + 2))
        ctx.line_to(29 * CM, CM * (j + 2))

    ctx.stroke()

    ctx.set_source_rgb(*g5)

    for k in range(6):
        ctx.move_to(5 * k * CM, 0)
        ctx.line_to(5 * k * CM, 595)
    for li in range(5):
        ctx.move_to(0, 5 * li * CM)
        ctx.line_to(842, 5 * li * CM)

    ctx.rectangle(2 * CM, CM, 27 * CM, 20 * CM)

    ctx.set_source_rgb(*black)

    ctx.stroke()
