from app_dir.sketch.sketch_config import CM, black, g8, Small_line_width,\
    centered_text, centered_vertical_text

class FramePainter:

    def draw(self, ctx, sx, sy, frame_type):
        painter = get_painter(frame_type)
        painter(ctx, sx, sy)


def get_painter(frame_type):
    if frame_type == 'ww_outside':
        return _draw_ww_external
    elif frame_type == 'ww_inside':
        return _draw_ww_internal
    else:
        raise ValueError(frame_type)


def _draw_ww_external(ctx, sx, sy):

    ww_external_points = (
        (2, 0),
        (-1, -1),
        (0, -4),
        (10, -10),
        (0, -4),
        (4, 0),
        (0, 4),
        (5, 0),
        (0, -1),
        (-4, 0),
        (0, -5),
        (15, 0),
        (0, 5),
        (-4, 0),
        (0, 1),
        (5, 0),
        (0, -10),
        (-5, 0),
        (0, -5),
        (5, 0),
        (0, -25),
        (-5, 0),
        (0, -5),
        (5, 0),
        (0, -10),
        (-15, 0),
        (0, 1),
        (4, 0),
        (0, 5),
        (-15, 0),
        (0, -5),
        (4, 0),
        (0, -1),
        (-5, 0),
        (0, 10),
        (-14, 0),
        (0, -3),
        (1, -1),
        (-2, 0),
        (0, 5),
        (13, 0),
        (2, 2),
        (0, 2),
        (-2, 2),
        (-3, 0)
    )

    ctx.move_to(sx + CM, sy + 3 * CM)

    for point in ww_external_points:
        ctx.rel_line_to(*point)

    ctx.close_path()
    ctx.set_source_rgb(*g8)
    ctx.fill_preserve()
    ctx.set_line_width(Small_line_width)
    ctx.set_source_rgb(*black)
    ctx.stroke()
    ctx.set_font_size(8)
    centered_text(
        ctx, sx / CM, sy / CM, 2.5, 0.5,
        text="Сечение лутки"
    )
    ctx.set_font_size(14)
    centered_vertical_text(
        ctx, sx / CM, sy / CM + 1, 1, 2,
        text="Наружная"
    )


def _draw_ww_internal(ctx, sx=18.5 * CM, sy=10 * CM):

    ctx.set_font_size(8)
    centered_text(
        ctx, sx / CM, sy / CM, 2.5, 0.5,
        text="Сечение лутки"
    )
    ctx.set_font_size(14)
    centered_vertical_text(
        ctx, sx / CM + 1, sy / CM + 1, 1, 4,
        text="Внутреняя"
    )
