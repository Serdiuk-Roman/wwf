from app_dir.sketch.sketch_config import CM, black, g8, Small_line_width,\
    centered_text, centered_vertical_text, white

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
        (5, 0),
        (0, 1),
        (-4, 0),
        (0, 5),
        (16, 0),
        (0, -5),
        (-4, 0),
        (0, -1),
        (17, 0),
        (0, 8),
        (-5, 0),
        (0, 3),
        (5, 0),
        (0, 27),
        (-5, 0),
        (0, 3),
        (5, 0),
        (0, 9),
        (-5, 0),
        (0, -1),
        (4, 0),
        (0, -5),
        (-16, 0),
        (0, 5),
        (4, 0),
        (0, 1),
        (-5, 0),
        (0, -3),
        (-4, 0),
        (0, 3),
        (-9, 9),
        (0, 3),
        (1, 1),
        (-2, 0),
        (0, -42),
        (5, 0),
        (2, -1),
        (1, -1.5),
        (-1, -1.5),
        (-2, -1),
        (-17, 0),
        (0, -3),
        (2, 0),
        (-1, 1),
        (0, 1),
        (13, 0)
    )

    ww_internal_points = (
        (17, 0),
        (0, -6),
        (11, 0),
        (0, 6),
        (-5, 0),
        (0, 5),
        (5, 0),
        (0, 25),
        (-5, 0),
        (0, 5),
        (-13, 0),
        (0, 3),
        (-3, 0),
        (0, -12),
        (-3, 0),
        (-2, 6),
        (0, 13),
        (-3, 3),
        (0, -33),
        (4, 0),
        (2, -1),
        (1, -2.5),
        (-1, -2.5),
        (-2, -1),
        (-3, 0)
    )

    ctx.move_to(sx + 0.5 * CM + 14, sy + 0.5 * CM)

    for point in ww_external_points:
        ctx.rel_line_to(*point)

    ctx.close_path()
    ctx.set_source_rgb(*g8)
    ctx.fill_preserve()
    ctx.set_line_width(Small_line_width)
    ctx.set_source_rgb(*black)
    ctx.stroke()

    ctx.move_to(sx + 0.5 * CM + 15, sy + 0.5 * CM + 7)

    for point in ww_internal_points:
        ctx.rel_line_to(*point)

    ctx.close_path()
    ctx.set_source_rgb(*white)
    ctx.fill_preserve()
    ctx.set_line_width(Small_line_width)
    ctx.set_source_rgb(*black)
    ctx.stroke()

    ctx.set_font_size(8)
    centered_text(
        ctx, sx / CM, sy / CM, 2.5, 0.5,
        text="Сечение лутки"
    )
    ctx.set_font_size(10)
    centered_vertical_text(
        ctx, sx / CM, sy / CM + 1.5, 1, 1,
        text="Наружная"
    )


def _draw_ww_internal(ctx, sx=19 * CM, sy=13 * CM):

    ww_external_points = (
        (2, 0),
        (-1, 1),
        (0, 12),
        (24, 0),
        (0, 1),
        (-3, 0),
        (0, 5),
        (16, 0),
        (0, -5),
        (-3, 0),
        (0, -1),
        (5, 0),
        (0, 7),
        (4, 0),
        (0, -7),
        (1, 0),
        (0, 9),
        (-5, 0),
        (0, 3),
        (5, 0),
        (0, 28),
        (-5, 0),
        (0, 3),
        (5, 0),
        (0, 8),
        (-5, 0),
        (0, -1),
        (3, 0),
        (0, -5),
        (-16, 0),
        (0, 5),
        (3, 0),
        (0, 1),
        (-5, 0),
        (0, -16),
        (-1, -1),
        (-5, 0),
        (-6, 6),
        (0, 3),
        (1, 1),
        (-2, 0),
        (0, -39),
        (8, 0),
        (0, -4),  # Радиус уплотнителля
        (-20, 0)
    )

    ww_internal_points = (
        (25, 0),
        (0, 5),
        (5, 0),
        (0, 26),
        (-5, 0),
        (0, 4),
        (-12, 0),
        (0, -9),
        (-2, -2),
        (-2, 0),
        (-1, -1),
        (0, -16),
        (-3, 0),
        (-2, 5),
        (0, 13),
        (-3, 3),
        (-1, 0)
    )

    ctx.set_font_size(8)
    centered_text(
        ctx, sx / CM, sy / CM, 2, 0.5,
        text="Сечение лутки"
    )

    ctx.move_to(sx, sy + 0.5 * CM)

    for point in ww_external_points:
        ctx.rel_line_to(*point)

    ctx.close_path()
    ctx.set_source_rgb(*g8)
    ctx.fill_preserve()
    ctx.set_line_width(Small_line_width)
    ctx.set_source_rgb(*black)
    ctx.stroke()

    ctx.move_to(sx + 14, sy + 0.5 * CM + 21)

    for point in ww_internal_points:
        ctx.rel_line_to(*point)

    ctx.close_path()
    ctx.set_source_rgb(*white)
    ctx.fill_preserve()
    ctx.set_line_width(Small_line_width)
    ctx.set_source_rgb(*black)
    ctx.stroke()

    ctx.set_font_size(10)
    centered_vertical_text(
        ctx, sx / CM, sy / CM, 1, 4,
        text="Внутреняя"
    )
    # ctx.set_font_size(10)
    # centered_text(
    #     ctx, (sx + 40) / CM, (sy + 25) / CM, 2.5, 0.5,
    #     text="907"
    # )
