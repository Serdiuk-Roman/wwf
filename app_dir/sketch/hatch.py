import cairo
from setting import Small_line_width
import color


def hatcing(var=1, hatch_scale=1):
    # horizontale
    # verticale
    # north east
    # north west
    # decart

    size_unit = (4, 4, 6, 6, 6, 8)
    sx = size_unit[var] * hatch_scale
    sy = size_unit[var] * hatch_scale
    pattern_surface = cairo.PDFSurface(None, sx, sy)
    ctx = cairo.Context(pattern_surface)
    ctx.set_line_width(Small_line_width)
    ctx.set_source_rgb(*color.g5)
    if var == 0:
        ctx.move_to(0, sy / 2)
        ctx.line_to(sx, sy / 2)
    elif var == 1:
        ctx.move_to(sx / 2, 0)
        ctx.line_to(sx / 2, sy)
    elif var == 2:
        ctx.move_to(0, sy)
        ctx.line_to(sx, 0)
    elif var == 3:
        ctx.move_to(0, 0)
        ctx.line_to(sx, sy)
    elif var == 4:
        ctx.move_to(0, sy / 2)
        ctx.line_to(sx, sy / 2)
        ctx.move_to(sx / 2, 0)
        ctx.line_to(sx / 2, sy)
    elif var == 5:
        ctx.move_to(0, 0)
        ctx.line_to(sx, sy)
        ctx.move_to(0, sy)
        ctx.line_to(sx, 0)
    else:
        return None
    ctx.stroke()
    pattern = cairo.SurfacePattern(pattern_surface)
    pattern.set_extend(cairo.EXTEND_REPEAT)
    return pattern
