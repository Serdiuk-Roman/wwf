CM = 28
Base_line_width = 2
Small_line_width = 1


# cr.arc(400, 300, 100, 0 * deg, 360 * deg)
# cr.arc_negative(600, 300, 100, 180 * deg, 360 * deg)
# cr.close_path()
# cr.fill_preserve()
# cr.set_source_rgb(0, 0, 1.0)
# cr.set_line_width(10.00)
# cr.stroke()
# cr.select_font_face(
#     "Sans",
#     cairo.FONT_SLANT_NORMAL,
#     cairo.FONT_WEIGHT_NORMAL
# )
# cr.set_font_size(40)

# cr.scale(100, 100)
# path_ellipse(cr, 0.5, 0.5, 1.0, 0.3, pi / 4.0)
# x, y = 0.5, 0.5
# cr.save()
# cr.translate(x, y)
# cr.rotate(pi / 4.0)
# cr.scale(1.0 / 2.0, 0.3 / 2.0)
# cr.arc(0.0, 0.0, 1.0, 0.0, 2.0 * pi)
# cr.restore()

# stroke
# reset identity matrix so line_width is a constant
# width in device-space, not user-space
# cr.save()
# cr.identity_matrix()


"""Create a PDF file for each example"""

# from __future__ import print_function

# import os
# import sys
# import cairo

# from snippets import get_snippets


# def do_snippet(snippet):
#     if verbose_mode:
#         print('processing %s' % snippet.name)

#     width_in_inches, height_in_inches = 2, 2
#     width_in_points, height_in_points = \
#         width_in_inches * 72, height_in_inches * 72
#     width, height = width_in_points, height_in_points

#     try:
#         os.makedirs(os.path.join("_build", "pdf"))
#     except EnvironmentError:
#         pass
#     filename = os.path.join("_build", "pdf", "%s.pdf" % snippet.name)

#     surface = cairo.PDFSurface(filename, width_in_points, height_in_points)
#     cr = cairo.Context(surface)

#     cr.save()
#     snippet.draw_func(cr, width, height)
#     cr.restore()
#     cr.show_page()
#     surface.finish()


# cr.translate(f_weight / 2, f_height / 2)
# cr.move_to(f_weight / 2, f_height / 2)


# cr.select_font_face(
#     "Sans",
#     cairo.FONT_SLANT_NORMAL,
#     cairo.FONT_WEIGHT_NORMAL
# )
# cr.set_font_size(40)

# cr.move_to(10, 50)
# cr.show_text("Disziplin ist Macht.")
# cr.show_page()

# 226 × 169 мм (640x480)
# 309 × 219 мм мм (877x620)

# 72 dpi (web) = 595x842 px
# 300 dpi (print) = 2480x3508 px
# 600 dpi (print) = 4960x7016 px

# cr.move_to(0, 10)
# cr.arc(10, 10, 10, math.pi, 1.5 * math.pi)
# cr.stroke_preserve()
