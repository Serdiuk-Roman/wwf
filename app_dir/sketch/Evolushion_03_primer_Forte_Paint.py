import cairo
import os


def brus_40(ctx, start_x, start_y, delta_x, delta_y):
    pass


def mdf(ctx, start_x, start_y, delta_x, delta_y):
    pass


def carcase(ctx):
    pass


def finishing_cutting(ctx):
    pass


def finish_cut(ctx):
    pass


def lutka(ctx):
    pass


def se4enie_lutky(ctx):
    pass


def lyshtva(ctx):
    pass


def strelka(ctx, sx=56, sy=56, vector=0):
    pass


def razmer_v(ctx, x1, y1, x2, y2, v, d):
    pass


def razmer_h(ctx, x1, y1, x2, y2, v, d):
    pass


def razmer(ctx):
    pass
    # finishing_cutting
    # lutka
    # se4enie_lutky

# import color
# from setting import CM, Base_line_width, Small_line_width
# import hatch

# Толщина бруса
TIMBER_THICKNESS = 27
# Толщина лутки
FRAME_THICKNESS = 36
# боковой зазор
SIDE_CLEARANCES = 6
# Вертикальные зазоры
VERTICAL_CLEARANCES = 12


def create_from_png(image_name):

    dir_path = os.path.dirname(os.path.realpath(__file__))

    print(os.chdir(dir_path))

    os.chdir(dir_path)

    ims = cairo.ImageSurface.create_from_png(image_name)

    return ims


def draw_pdf():

    filename = "Evolushion_03_primer_Forte_Paint.pdf"

    surface = cairo.PDFSurface(filename, 842, 595)
    ctx = cairo.Context(surface)

    # ims = cairo.ImageSurface.create_from_png(image_name)
    # mask_img = create_from_png("Evolshion_03_primer.png")

    ims = cairo.ImageSurface.create_from_png("Evolshion_03_primer.png")
    ctx.set_source_surface(ims, 0, 0)
    ctx.paint()

    ctx.select_font_face("Times New Roman")
    ctx.set_font_size(12)

    ctx.move_to(50, 50)
    ctx.show_text("Hello World")

    # surface.show_page()
    ctx.save()
    ctx.restore()


if __name__ == "__main__":
    draw_pdf()
