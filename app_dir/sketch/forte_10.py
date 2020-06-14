import color
from setting import CM, Base_line_width, Small_line_width
import hatch


def brus_40(ctx, start_x, start_y, delta_x, delta_y):
    ctx.rectangle(start_x, start_y, delta_x, delta_y)
    # ctx.set_source_rgb(*color.white)
    # ctx.fill_preserve()
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*color.black)
    ctx.stroke()


def mdf(ctx, start_x, start_y, delta_x, delta_y):
    ctx.rectangle(start_x, start_y, delta_x, delta_y)
    ctx.set_source_rgb(*color.g7)
    ctx.fill_preserve()
    ctx.set_line_width(Small_line_width)
    ctx.set_source_rgb(*color.black)
    ctx.stroke()


def carcase(ctx):

    tmdf = 2
    tb = 8

    sx, sy = 3 * CM, 7 * CM
    brus_40(ctx, sx + 4, sy, tb, 10 * CM)
    mdf(ctx, sx, sy, tmdf, 10 * CM)
    mdf(ctx, sx + 2, sy, tmdf, 10 * CM)

    krai = 2 * tmdf + tb
    brus_40(ctx, sx + krai, sy + 1.5 * CM, tb, 1.5 * CM)
    brus_40(ctx, sx + krai, sy + 4 * CM, tb, 2 * CM)
    brus_40(ctx, sx + krai, sy + 7 * CM, tb, 1.5 * CM)

    brus_40(ctx, sx + krai, sy, 5 * CM - 2 * krai, tb)
    brus_40(ctx, sx + krai, sy + 10 * CM, 5 * CM - 2 * krai, - tb)

    mdf(ctx, sx + 2 * CM, sy + tb, tmdf, 10 * CM - 2 * tb)
    mdf(ctx, sx + 2.5 * CM, sy + tb, tmdf, 10 * CM - 2 * tb)
    mdf(ctx, sx + 3 * CM, sy + tb, tmdf, 10 * CM - 2 * tb)

    sx = 8 * CM - (2 * tmdf + tb)
    brus_40(ctx, sx, sy + 1.5 * CM, -tb, 1.5 * CM)
    brus_40(ctx, sx, sy + 4 * CM, -tb, 2 * CM)
    brus_40(ctx, sx, sy + 7 * CM, -tb, 1.5 * CM)

    brus_40(ctx, sx, sy, tb, 10 * CM)
    mdf(ctx, sx + tb, sy, tmdf, 10 * CM)
    mdf(ctx, sx + tb + tmdf, sy, tmdf, 10 * CM)


def finishing_cutting(ctx):
    ctx.rectangle(9 * CM, 7 * CM, 5 * CM, 10 * CM)
    ctx.set_source(hatch.hatcing(1, 1))
    ctx.fill_preserve()
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*color.black)
    ctx.stroke()


def finish_cut(ctx):
    cm = 28

    sx, sy = 16 * cm, 2 * cm
    delta = 2 * cm
    for i in range(6):
        for y in range(1):
            ctx.rectangle(
                sx + i * delta,
                sy + y * delta,
                delta,
                delta
            )
            ctx.set_source(hatch.hatcing(i, y + 1))
            ctx.fill_preserve()
            ctx.set_source_rgb(*color.black)
            ctx.stroke()


def lutka(ctx):
    sx, sy = 16 * CM, 7 * CM

    ctx.move_to(sx, sy)
    ctx.line_to(sx - 14, sy - 14)
    ctx.line_to(sx - 21, sy - 14)
    ctx.line_to(sx - 21, sy - 21)
    ctx.line_to(sx + 4 * CM + 21, sy - 21)
    ctx.line_to(sx + 4 * CM + 21, sy - 14)
    ctx.line_to(sx + 4 * CM + 14, sy - 14)
    ctx.line_to(sx + 4 * CM, sy)
    ctx.close_path()
    ctx.set_source(hatch.hatcing(0, 1))
    ctx.fill_preserve()
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*color.black)
    ctx.stroke()
    ctx.move_to(sx - 7, sy - 7)
    ctx.line_to(sx + 4 * CM + 7, sy - 7)
    ctx.stroke()

    ctx.move_to(sx, sy)
    ctx.line_to(sx - 14, sy - 14)
    ctx.line_to(sx - 21, sy - 14)
    ctx.line_to(sx - 21, sy + 10 * CM)
    ctx.line_to(sx, sy + 10 * CM)
    ctx.close_path()
    ctx.set_source(hatch.hatcing(1, 1))
    ctx.fill_preserve()
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*color.black)
    ctx.stroke()
    ctx.move_to(sx - 7, sy - 7)
    ctx.line_to(sx - 7, sy + 10 * CM)
    ctx.stroke()

    ctx.move_to(sx + 4 * CM, sy)
    ctx.line_to(sx + 4 * CM + 14, sy - 14)
    ctx.line_to(sx + 4 * CM + 21, sy - 14)
    ctx.line_to(sx + 4 * CM + 21, sy + 10 * CM)
    ctx.line_to(sx + 4 * CM, sy + 10 * CM)
    ctx.close_path()
    ctx.set_source(hatch.hatcing(1, 1))
    ctx.fill_preserve()
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*color.black)
    ctx.stroke()
    ctx.move_to(sx + 4 * CM + 7, sy - 7)
    ctx.line_to(sx + 4 * CM + 7, sy + 10 * CM)
    ctx.stroke()

    # ctx.set_source(hatch.hatcing(0, 1))
    # ctx.fill_preserve()
    # ctx.set_line_width(Base_line_width)
    # ctx.set_source_rgb(*color.black)


def se4enie_lutky(ctx):
    sx, sy = 17.5 * CM, 17 * CM
    ctx.move_to(sx, sy)
    ctx.line_to(sx, sy - 68)
    ctx.line_to(sx + 22, sy - 68)
    ctx.line_to(sx + 22, sy - 90)
    ctx.line_to(sx + 43, sy - 90)
    ctx.line_to(sx + 43, sy - 34)
    ctx.line_to(sx + 39, sy - 34)
    ctx.line_to(sx + 39, sy - 40)
    ctx.line_to(sx + 36, sy - 40)
    ctx.line_to(sx + 36, sy - 34)

    ctx.line_to(sx + 32, sy - 34)
    ctx.line_to(sx + 32, sy - 50)
    ctx.line_to(sx + 25, sy - 50)
    ctx.line_to(sx + 25, sy)
    ctx.close_path()
    ctx.set_source(hatch.hatcing(2, 1))
    ctx.fill_preserve()
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*color.black)
    ctx.stroke()


def lyshtva(ctx):
    sx, sy = 23 * CM, 7 * CM
    ctx.rectangle(sx, sy, 4 * CM, -20)
    ctx.set_source(hatch.hatcing(0, 1))
    ctx.fill_preserve()
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*color.black)
    ctx.stroke()
    ctx.rectangle(sx, sy - 20, -20, 10 * CM + 20)
    ctx.set_source(hatch.hatcing(1, 1))
    ctx.fill_preserve()
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*color.black)
    ctx.stroke()
    ctx.rectangle(sx + 4 * CM, sy - 20, 20, 10 * CM + 20)
    ctx.set_source(hatch.hatcing(1, 1))
    ctx.fill_preserve()
    ctx.set_line_width(Base_line_width)
    ctx.set_source_rgb(*color.black)
    ctx.stroke()


def strelka(ctx, sx=56, sy=56, vector=0):
    # big size
    bs = 8
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
    ctx.set_source_rgb(*color.black)
    # ctx.fill()
    ctx.fill_preserve()
    ctx.stroke()


def razmer_v(ctx, x1, y1, x2, y2, v, d):
    ctx.set_line_width(1.00)
    ctx.move_to(x1 + 4 * v, y1)
    ctx.line_to(x1 + d * v, y1)
    ctx.move_to(x2 + 4 * v, y2)
    ctx.line_to(x2 + d * v, y2)
    ctx.move_to(x1 + (d - 4) * v, y1 + 2)
    ctx.line_to(x2 + (d - 4) * v, y2 - 2)
    ctx.stroke()
    strelka(ctx, x1 + (d - 4) * v, y1 + 2, vector=1)
    strelka(ctx, x2 + (d - 4) * v, y2 - 2, vector=3)


def razmer_h(ctx, x1, y1, x2, y2, v, d):
    ctx.set_line_width(1.00)
    ctx.move_to(x1, y1 + 4 * v)
    ctx.line_to(x1, y1 + d * v)
    ctx.move_to(x2, y2 + 4 * v)
    ctx.line_to(x2, y2 + d * v)
    ctx.move_to(x1 + 2, y1 + (d - 4) * v)
    ctx.line_to(x2 - 2, y2 + (d - 4) * v)
    ctx.stroke()
    strelka(ctx, x1 + 2, y1 + (d - 4) * v, vector=0)
    strelka(ctx, x2 - 2, y2 + (d - 4) * v, vector=2)


def razmer(ctx):
    razmer_v(ctx, 3 * CM, 7 * CM, 3 * CM, 17 * CM, -1, 14)

    razmer_v(ctx, 3 * CM + 20, 7 * CM, 3 * CM + 20, 11 * CM, 1, 28)
    razmer_v(ctx, 3 * CM + 20, 11 * CM, 3 * CM + 20, 13 * CM, 1, 28)
    razmer_v(ctx, 3 * CM + 20, 13 * CM, 3 * CM + 20, 17 * CM, 1, 28)

    razmer_v(ctx, 8 * CM - 20, 7 * CM, 8 * CM - 20, 8.5 * CM, -1, 14)
    razmer_v(ctx, 8 * CM - 20, 8.5 * CM, 8 * CM - 20, 10 * CM, -1, 14)
    razmer_v(ctx, 8 * CM - 20, 14 * CM, 8 * CM - 20, 15.5 * CM, -1, 14)
    razmer_v(ctx, 8 * CM - 20, 15.5 * CM, 8 * CM - 20, 17 * CM, -1, 14)

    razmer_h(ctx, 3 * CM, 7 * CM, 8 * CM, 7 * CM, -1, 28)
    razmer_h(ctx, 3 * CM + 12, 7 * CM, 8 * CM - 12, 7 * CM, -1, 14)

    # finishing_cutting
    razmer_h(ctx, 9 * CM, 7 * CM, 14 * CM, 7 * CM, -1, 28)
    razmer_v(ctx, 14 * CM, 7 * CM, 14 * CM, 17 * CM, 1, 28)

    # lutka
    razmer_v(ctx, 16 * CM, 7 * CM - 7, 16 * CM, 17 * CM, 1, 21)
    razmer_h(ctx, 16 * CM - 21, 7 * CM - 21, 20 * CM + 21, 7 * CM - 21, -1, 14)
    razmer_h(ctx, 16 * CM - 7, 7 * CM, 20 * CM + 7, 7 * CM, 1, 28)
    razmer_v(ctx, 20 * CM + 21, 7 * CM - 21, 20 * CM + 21, 17 * CM, 1, 38)
    razmer_v(ctx, 20 * CM + 21, 7 * CM - 14, 20 * CM + 21, 17 * CM, 1, 21)

    # se4enie_lutky
    razmer_v(ctx, 17.5 * CM, 17 * CM - 90, 17.5 * CM, 17 * CM, -1, 14)
    ctx.move_to(17.5 * CM + 22 - 4, 17 * CM - 90)
    ctx.line_to(17.5 * CM - 4, 17 * CM - 90)
    ctx.stroke()

    razmer_v(ctx, 17.5 * CM + 22, 17 * CM - 68,
             17.5 * CM + 22, 17 * CM - 90, -1, 14)
    ctx.move_to(17.5 * CM + 12, 17 * CM - 54)
    ctx.line_to(17.5 * CM + 12, 17 * CM - 104)
    ctx.stroke()

    razmer_v(ctx, 17.5 * CM + 43, 17 * CM - 90,
             17.5 * CM + 43, 17 * CM - 34, 1, 21)
    razmer_v(ctx, 17.5 * CM + 43, 17 * CM - 34,
             17.5 * CM + 43, 17 * CM, 1, 21)
    ctx.move_to(17.5 * CM + 43 - 11 - 6 + 2, 17 * CM)
    ctx.line_to(17.5 * CM + 43 + 4, 17 * CM)
    ctx.stroke()

    razmer_h(ctx,
             17.5 * CM, 17 * CM,
             17.5 * CM + 32, 17 * CM,
             1, 21)
    ctx.move_to(17.5 * CM + 43 - 11, 17 * CM - 34 + 4)
    ctx.line_to(17.5 * CM + 43 - 11, 17 * CM + 4)
    ctx.stroke()

    razmer_h(ctx,
             17.5 * CM, 17 * CM,
             17.5 * CM + 43, 17 * CM,
             1, 35)
    ctx.move_to(17.5 * CM + 43, 17 * CM - 34 + 4)
    ctx.line_to(17.5 * CM + 43, 17 * CM + 4)
    ctx.stroke()

    razmer_h(ctx,
             17.5 * CM + 43, 17 * CM - 90,
             17.5 * CM, 17 * CM - 90,
             -1, 21)
    ctx.move_to(17.5 * CM - 14, 17 * CM - 90 - 17)
    ctx.line_to(17.5 * CM + 43 + 14, 17 * CM - 90 - 17)
    ctx.move_to(17.5 * CM + 22, 17 * CM - 90 - 4)
    ctx.line_to(17.5 * CM + 22, 17 * CM - 90 - 21)
    ctx.move_to(17.5 * CM + 22 + 3, 17 * CM - 90 - 21)
    ctx.line_to(17.5 * CM + 22 - 3, 17 * CM - 90 - 21 + 8)
    ctx.stroke()

    # lyshtva
    razmer_h(ctx, 23 * CM - 20, 7 * CM - 20, 27 * CM + 20, 7 * CM - 20, -1, 28)
    razmer_h(ctx, 23 * CM, 7 * CM - 20, 27 * CM, 7 * CM - 20, -1, 14)
    razmer_v(ctx, 27 * CM + 20, 7 * CM - 20, 27 * CM + 20, 17 * CM, 1, 21)
