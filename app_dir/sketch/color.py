from setting import CM, Small_line_width


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

palitra = (black, g1, g2, g3, g4, g5, g6, g7, g8, g9, white)


def perymetr(ctx):

    ctx.set_line_width(Small_line_width)

    # horyzont
    for i in range(31):
        ctx.move_to(CM * i, 0)
        ctx.line_to(CM * i, 4)
    # vertycal
    for j in range(22):
        ctx.move_to(0, CM * j)
        ctx.line_to(4, CM * j)
    for k in range(7):
        ctx.move_to(5 * k * CM, 0)
        ctx.line_to(5 * k * CM, 10)
    for l in range(5):
        ctx.move_to(0, 5 * l * CM)
        ctx.line_to(10, 5 * l * CM)

    ctx.rectangle(2 * CM, CM, 27 * CM, 19 * CM)

    ctx.set_source_rgb(*g5)

    ctx.stroke()
