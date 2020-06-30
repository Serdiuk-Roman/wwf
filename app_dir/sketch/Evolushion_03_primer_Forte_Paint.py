from pathlib import Path
import math

import cairo

from app_dir import app

from app_dir.sketch.sketch_config import *


def brus_40(ctx):
    pass


def mdf(ctx):
    pass


def se4enie_lutky(ctx):
    pass


class Evolushion_03_primer_Forte_Paint():
    def __init__(self, ctx, order_number, positions_list):
        self.ctx = ctx
        self.order_number = order_number
        self.positions_list = positions_list

        self.surface_name = "Evolshion_03_primer.png"
        # Толщина бруса
        self.TIMBER_THICKNESS = 27
        # Толщина лутки
        self.FRAME_THICKNESS = 36
        # боковой зазор
        self.SIDE_CLEARANCES = 6
        # Вертикальные зазоры
        self.VERTICAL_CLEARANCES = 12

        self.mdf = []
        self.brus_40 = []
        self.brus_18 = []
        self.expander = []

        self.door_h = 2000
        self.door_w = 800

    def create_from_png(self):
        dir_path = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(dir_path, 'surface', self.surface_name)
        self.ims = cairo.ImageSurface.create_from_png(img_path)

    def draw_page(self):
        # ims = cairo.ImageSurface.create_from_png(image_name)
        # mask_img = create_from_png("Evolshion_03_primer.png")
        # размер изображения 1108x772 точок

        self.ctx.save()
        self.create_from_png()
        self.ctx.scale(0.76, 0.76)
        self.ctx.set_source_surface(self.ims, 0, 0)
        self.ctx.paint()
        self.ctx.restore()

        # Сетка сантиметровая(приблизительно)
        # perymetr(ctx)

    def draw_model_name(self):
        self.ctx.set_font_size(11)
        # Модель
        self.ctx.move_to(11.5 * CM, 2.4 * CM)
        self.ctx.show_text('Evolushion 03 primer')

    def draw_positions_number(self):
        self.ctx.set_font_size(42)
        # Номер позиции
        (x, y, width, height, dx, dy) = self.ctx.text_extents(
            str(self.positions_list)[1:-1]
        )
        self.ctx.move_to(28 * CM - dx, 2 * CM)
        self.ctx.show_text(str(self.positions_list)[1:-1])

    def draw_door_size(self):
        self.ctx.set_font_size(14)
        # Висота полотна
        self.ctx.move_to(2.7 * CM, 4 * CM)
        self.ctx.show_text(str(self.door_h))
        # Ширина полотна
        self.ctx.move_to(4.4 * CM, 4 * CM)
        self.ctx.show_text(str(self.door_w))

    def draw_finish_cut(self):
        self.ctx.set_font_size(14)
        # Висота полотна без кромки
        self.ctx.move_to(14.2 * CM, 19.7 * CM)
        self.ctx.show_text(str(self.door_h - 1))
        # Ширина полотна без кромки
        self.ctx.move_to(16 * CM, 19.7 * CM)
        self.ctx.show_text(str(self.door_w - 1))

    def draw_carcase_size(self):
        self.ctx.set_font_size(12)
        # Высота черновая, Стойка бруса и МДФ 6
        draft_size_h = str(self.door_h + 9 * 2)
        self.ctx.save()
        self.ctx.move_to(3 * CM, 13 * CM)
        self.ctx.rotate(3 * math.pi / 2)
        self.ctx.show_text(draft_size_h)
        self.ctx.restore()
        self.ctx.save()
        self.ctx.move_to(15.2 * CM, 13 * CM)
        self.ctx.rotate(3 * math.pi / 2)
        self.ctx.show_text(draft_size_h)
        self.ctx.restore()
        self.ctx.move_to(24 * CM, 19.05 * CM)
        self.ctx.show_text(draft_size_h)
        self.ctx.move_to(3 * CM, 18.61 * CM)
        self.ctx.show_text(draft_size_h)

        # Ширина черновая и МДФ 6
        draft_size_w = str(self.door_w + 9 * 2)
        self.ctx.move_to(6 * CM, 6.5 * CM)
        self.ctx.show_text(draft_size_w)
        self.ctx.move_to(12 * CM, 6.5 * CM)
        self.ctx.show_text(draft_size_w)
        self.ctx.move_to(25.7 * CM, 19.05 * CM)
        self.ctx.show_text(draft_size_w)

        # Поперечка бруса
        self.ctx.move_to(6 * CM, 7 * CM)
        self.ctx.show_text(str(self.door_w + 9 * 2 - 40 * 2))
        self.ctx.move_to(3 * CM, 19.05 * CM)
        self.ctx.show_text(str(self.door_w + 9 * 2 - 40 * 2))

        # Замочний брус
        self.ctx.save()
        self.ctx.move_to(5.4 * CM, 13 * CM)
        self.ctx.rotate(3 * math.pi / 2)
        self.ctx.show_text(str(int(draft_size_h) - 800 * 2))
        self.ctx.restore()
        self.ctx.move_to(3 * CM, 19.45 * CM)
        self.ctx.show_text(str(int(draft_size_h) - 800 * 2))
        self.ctx.move_to(6.5 * CM, 18.61 * CM)
        self.ctx.show_text(str(int(draft_size_h) - 800 * 2))

    def draw_frame_size(self):
        self.ctx.set_font_size(12)
        # Коробка
        self.frame_h = (
            self.door_h + self.VERTICAL_CLEARANCES + self.FRAME_THICKNESS
        )
        self.frame_w = (
            self.door_w + self.SIDE_CLEARANCES + 2 * self.FRAME_THICKNESS
        )

        # Лутка высоты
        self.ctx.save()
        self.ctx.move_to(18.5 * CM, 12 * CM)
        self.ctx.rotate(3 * math.pi / 2)
        self.ctx.show_text(str(self.door_h + self.VERTICAL_CLEARANCES))
        self.ctx.restore()
        self.ctx.save()
        self.ctx.move_to(23 * CM, 14 * CM)
        self.ctx.rotate(3 * math.pi / 2)
        self.ctx.show_text(str(self.frame_h))
        self.ctx.restore()
        self.ctx.save()
        self.ctx.move_to(22.5 * CM, 12 * CM)
        self.ctx.rotate(3 * math.pi / 2)
        self.ctx.show_text(str(self.frame_h - 17))
        self.ctx.restore()

        # Поперечка лутки
        self.ctx.move_to(19.4 * CM, 9.7 * CM)
        self.ctx.show_text(str(self.door_w + self.SIDE_CLEARANCES))
        self.ctx.move_to(19.4 * CM, 6.9 * CM)
        self.ctx.show_text(str(self.frame_w))

    def draw_casing_size(self):
        # Наличник
        self.ctx.set_font_size(12)
        self.ctx.move_to(25.4 * CM, 7 * CM)
        self.ctx.show_text(str(self.frame_w - 16 * 2))
        self.ctx.move_to(25.4 * CM, 6.5 * CM)
        self.ctx.show_text(str(self.frame_w - 16 * 2 + 70 * 2))
        self.ctx.save()
        self.ctx.move_to(28.3 * CM, 12 * CM)
        self.ctx.rotate(3 * math.pi / 2)
        self.ctx.show_text(str(self.frame_h - 16 + 70))
        self.ctx.restore()

    def draw_expander_size(self):
        # Доборы
        self.ctx.set_font_size(12)
        expander_h = (
            self.door_h + self.VERTICAL_CLEARANCES + self.FRAME_THICKNESS - 23
        )
        expander_w = self.frame_w
        self.ctx.move_to(17.7 * CM, 3.7 * CM)
        self.ctx.show_text(str(expander_h))
        self.ctx.move_to(17.9 * CM, 4.3 * CM)
        self.ctx.show_text(str(expander_w))

    def draw_position_casing_count(self):
        # Количество комплектов и наличников
        self.ctx.set_font_size(16)
        kol = len(self.positions_list)
        msg = "Изготовить {} компл.".format(kol)
        self.ctx.move_to(8 * CM, 1.3 * CM)
        self.ctx.show_text(msg)
        msg = "{} компл. наличников".format(kol)
        self.ctx.move_to(8 * CM, 1.9 * CM)
        self.ctx.show_text(msg)
        self.ctx.move_to(13.3 * CM, 4 * CM)
        self.ctx.show_text("1")


class Pdf_Generator():

    def __init__(self, order_number):
        self.order_number = order_number

    def set_output_file(self):

        sketch_dir = Path(app.instance_path).parent / "app_dir" / "sketch"

        filename = str(sketch_dir.joinpath(
            "resume",
            "{}.pdf".format(self.order_number)
        ))

        surface = cairo.PDFSurface(filename, 842, 595)
        self.ctx = cairo.Context(surface)
        self.ctx.select_font_face("Times New Roman")
        self.ctx.set_source_rgb(*black)

    def destr(self):
        # surface.show_page()
        self.ctx.save()
        self.ctx.restore()

    def run(self):
        self.set_output_file()
        e = Evolushion_03_primer_Forte_Paint(
            self.ctx,
            self.order_number,
            [1, 2, 3]
        )
        e.draw_page()
        e.draw_model_name()
        e.draw_positions_number()
        e.draw_door_size()
        e.draw_finish_cut()
        e.draw_carcase_size()
        e.draw_frame_size()
        e.draw_casing_size()
        e.draw_expander_size()
        e.draw_position_casing_count()

        self.destr()


if __name__ == "__main__":
    i = Pdf_Generator("170001")
    i.run()
