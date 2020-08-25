import math

import cairo

from app_dir.sketch.sketch_config import CM
from app_dir.sketch.sketch_elem import ww_external_points

from app_dir.sketch.sketch_config import perymetr
from app_dir.sketch.sketch_config import draw_carcase, draw_table,\
    draw_finishing_cutting, razmer_h, razmer_v, thin_rectangle,\
    centered_text, black, g8, Base_line_width, Small_line_width,\
    base_rectangle, centered_vertical_text


class Cw_evolushion_03_primer_ww_external():
    def __init__(self, ctx, order, positions_list, sketch_dir):
        self.ctx = ctx
        self.order = order
        self.positions_list = positions_list[2]
        self.door_h = positions_list[0]
        self.door_w = positions_list[1]
        self.sketch_dir = sketch_dir

        self.surface_name = "cw_evolushion_03_pr_ww_external_2.png"
        # Толщина бруса
        self.TIMBER_THICKNESS = 28
        # Толщина лутки
        self.FRAME_THICKNESS = 33
        # боковой зазор
        self.SIDE_CLEARANCES = 6
        # Вертикальные зазоры
        self.VERTICAL_CLEARANCES = 12

        self.mdf = []
        self.brus_40 = []
        self.brus_18 = []

    def create_from_png(self):

        img_path = str(self.sketch_dir.joinpath(
            "surface",
            self.surface_name
        ))

        self.ims = cairo.ImageSurface.create_from_png(img_path)

    def draw_model_name(self):

        self.ctx.set_font_size(12)
        # Модель
        thin_rectangle(self.ctx, 11, 2, 5, 0.5, text="Evolushion 03 primer")
        # self.ctx.set_font_size(10)
        thin_rectangle(self.ctx, 7, 3, 4, 1, text="Светлый грунт")

    def draw_positions_number(self):
        self.ctx.set_font_size(42)
        # Номер позиции
        (x, y, width, height, dx, dy) = self.ctx.text_extents(
            str(self.positions_list)
        )
        self.ctx.move_to(29 * CM - dx, 2 * CM)
        self.ctx.show_text(str(self.positions_list))

    def draw_door_size(self):
        self.ctx.set_font_size(14)
        # Висота полотна
        thin_rectangle(self.ctx, 2, 3, 2, 1, text=str(self.door_h))
        # Ширина полотна
        thin_rectangle(self.ctx, 4, 3, 2, 1, text=str(self.door_w))

    def draw_finish_cut(self):
        self.ctx.set_font_size(12)
        centered_text(
            self.ctx, 8.5, 17, 4, 0.5,
            text="Размер полотна"
        )
        centered_text(
            self.ctx, 8.5, 17.5, 4, 0.5,
            text="БЕЗ кромки"
        )
        self.ctx.set_font_size(16)
        # Висота полотна без кромки
        thin_rectangle(
            self.ctx, 8.5, 18.5, 2, 1,
            text=str(self.door_h - 1)
        )
        # Ширина полотна без кромки
        thin_rectangle(
            self.ctx, 10.5, 18.5, 2, 1,
            text=str(self.door_w - 1)
        )

    def draw_carcase_thickness(self):
        # Толщина бруса
        self.ctx.set_font_size(18)
        thin_rectangle(
            self.ctx, 4.5, 4.5, 2, 1,
            text="40х" + str(self.TIMBER_THICKNESS)
        )

    def draw_carcase_size(self):
        self.ctx.set_font_size(10)
        thin_rectangle(
            self.ctx, 2, 17, 3, 0.5,
            text="Брус 40*" + str(self.TIMBER_THICKNESS)
        )
        thin_rectangle(
            self.ctx, 5, 17, 3, 0.5,
            text="Брус 18*" + str(self.TIMBER_THICKNESS)
        )
        # Высота черновая Стойка бруса
        draft_size_h = str(self.door_h + 9 * 2)
        razmer_v(
            self.ctx, 3 * CM, 7.5 * CM, 9 * CM,
            -1, d=0.5,
            text=draft_size_h
        )
        thin_rectangle(
            self.ctx, 2, 17.5, 1.5, 0.5,
            text=draft_size_h
        )
        thin_rectangle(
            self.ctx, 3.5, 17.5, 1.5, 0.5,
            text="2 шт."
        )
        # Высота черновая МДФ 6
        razmer_v(
            self.ctx, 8.5 * CM, 7.5 * CM, 9 * CM,
            -1, d=0.5,
            text=draft_size_h
        )

        # Ширина черновая и МДФ 6
        draft_size_w = str(self.door_w + 9 * 2)
        # каркас
        razmer_h(
            self.ctx, 3 * CM, 7.5 * CM, 4 * CM, -1, d=1, text=draft_size_w
        )
        # полотно
        razmer_h(
            self.ctx, 8.5 * CM, 7.5 * CM, 4 * CM, -1, d=1, text=draft_size_w
        )

        # Поперечка бруса
        razmer_h(
            self.ctx, 3 * CM + 0.2 * CM, 7.5 * CM, 4 * CM - 0.2 * CM * 2,
            -1, d=0.5,
            text=str(self.door_w + 9 * 2 - 40 * 2)
        )
        thin_rectangle(
            self.ctx, 2, 18, 1.5, 0.5,
            text=str(self.door_w + 9 * 2 - 40 * 2)
        )
        thin_rectangle(
            self.ctx, 3.5, 18, 1.5, 0.5,
            text="2 шт."
        )

        # Замочний брус размер
        razmer_v(
            self.ctx, (3 + 0.5) * CM, 7.5 * CM, 3.5 * CM,
            1, d=0.7,
            text="800"
        )
        razmer_v(
            self.ctx, (3 + 0.5) * CM, 11 * CM, 2 * CM,
            1, d=0.7,
            text=str(int(draft_size_h) - 800 * 2)
        )
        razmer_v(
            self.ctx, (3 + 0.5) * CM, 13 * CM, 3.5 * CM,
            1, d=0.7,
            text="800"
        )
        # Замочний брус таблица 40x
        thin_rectangle(
            self.ctx, 2, 18.5, 1.5, 0.5,
            text=str(int(draft_size_h) - 800 * 2)
        )
        thin_rectangle(
            self.ctx, 3.5, 18.5, 1.5, 0.5,
            text="2 шт."
        )
        # Замочний брус таблица 18x
        thin_rectangle(
            self.ctx, 5, 17.5, 1.5, 0.5,
            text=str(int(draft_size_h) - 800 * 2)
        )
        thin_rectangle(
            self.ctx, 6.5, 17.5, 1.5, 0.5,
            text="2 шт."
        )

        # Петлевой брус размер
        start_x = (3 + 4 - 0.4) * CM
        razmer_v(
            self.ctx, start_x, 7.5 * CM, 1 * CM,
            -1, d=0.5,
            text="140"
        )
        razmer_v(
            self.ctx, start_x, 8.5 * CM, 1.5 * CM,
            -1, d=0.5,
            text="210"
        )
        razmer_v(
            self.ctx, start_x, 14 * CM, 1.5 * CM,
            -1, d=0.5,
            text="210"
        )
        razmer_v(
            self.ctx, start_x, 15.5 * CM, 1 * CM,
            -1, d=0.5,
            text="140"
        )
        # Петлевой брус таблица
        thin_rectangle(
            self.ctx, 2, 19, 1.5, 0.5,
            text="210"
        )
        thin_rectangle(
            self.ctx, 3.5, 19, 1.5, 0.5,
            text="4 шт."
        )

    def draw_rough_table(self, sx=23, sy=16.5):
        # Таблица для чернового
        self.ctx.set_font_size(10)
        thin_rectangle(self.ctx, sx + 1, sy, 1.5, 0.5, text="Длина")
        thin_rectangle(self.ctx, sx + 2.5, sy, 1.5, 0.5, text="Ширина")
        thin_rectangle(self.ctx, sx + 4, sy, 1, 0.5, text="Кол.")

        thin_rectangle(
            self.ctx, sx + 1, sy + 0.5, 4, 0.5,
            text="МДФ 16 (карточка)"
        )

        thin_rectangle(
            self.ctx, sx + 1, sy + 1, 1.5, 0.5,
            text=str(self.door_h + 9 * 2)
        )
        thin_rectangle(
            self.ctx, sx + 2.5, sy + 1, 1.5, 0.5,
            text=str(self.door_w + 9 * 2)
        )
        thin_rectangle(
            self.ctx, sx + 4, sy + 1, 1, 0.5,
            text="2"
        )

        base_rectangle(self.ctx, sx, sy, 1, 3.5)
        self.ctx.set_font_size(16)
        centered_vertical_text(self.ctx, sx, sy, 1, 3.5, text="Раскрой")
        base_rectangle(self.ctx, sx + 1, sy, 4, 3.5)

    def draw_frame_ww_external(self, sx=17.5 * CM, sy=7 * CM):
        # sx и sy - стартовые координаты относительно которых рисуется ескиз

        self.ctx.move_to(sx, sy)
        self.ctx.line_to(sx + 4 * CM, sy)
        self.ctx.line_to(sx + 4 * CM, sy + 9.5 * CM)
        self.ctx.line_to(sx + 4 * CM - 0.5 * CM, sy + 9.5 * CM)
        self.ctx.line_to(sx + 4 * CM - 0.5 * CM, sy + 0.5 * CM)
        self.ctx.line_to(sx + 0.5 * CM, sy + 0.5 * CM)
        self.ctx.line_to(sx + 0.5 * CM, sy + 9.5 * CM)
        self.ctx.line_to(sx, sy + 9.5 * CM)
        self.ctx.close_path()
        self.ctx.set_source_rgb(*g8)
        self.ctx.fill_preserve()
        self.ctx.set_line_width(Base_line_width)
        self.ctx.set_source_rgb(*black)
        self.ctx.stroke()
        self.ctx.move_to(sx, sy)
        self.ctx.line_to(sx + 0.5 * CM, sy + 0.5 * CM)
        self.ctx.stroke()
        self.ctx.move_to(sx + 4 * CM, sy)
        self.ctx.line_to(sx + 4 * CM - 0.5 * CM, sy + 0.5 * CM)
        self.ctx.stroke()
        self.ctx.set_line_width(Small_line_width)
        self.ctx.move_to(sx + 0.3 * CM, sy + 9.5 * CM)
        self.ctx.line_to(sx + 0.3 * CM, sy + 0.3 * CM)
        self.ctx.line_to(sx + (4 - 0.3) * CM, sy + 0.3 * CM)
        self.ctx.line_to(sx + (4 - 0.3) * CM, sy + 9.5 * CM)
        self.ctx.stroke()

    def draw_frame_size(self, sx=17.5 * CM, sy=7 * CM):

        self.frame_w = (
            self.door_w + self.SIDE_CLEARANCES + 2 * self.FRAME_THICKNESS
        )
        self.frame_h = (
            self.door_h + self.VERTICAL_CLEARANCES + self.FRAME_THICKNESS
        )

        self.ctx.set_line_width(Small_line_width)
        self.ctx.set_source_rgb(*black)
        self.ctx.set_font_size(10)
        centered_text(
            self.ctx, 18.5, 8.5, 2, 0.5,
            text="Проём"
        )
        centered_text(
            self.ctx, 18.5, 9, 2, 0.5,
            text="полотна"
        )

        # Поперечка лутки

        # Габаритный размер поперечки лутки
        razmer_h(
            self.ctx, sx, sy, 4 * CM,
            -1, d=0.5,
            text=str(self.frame_w)
        )
        # Проёмный размер поперечки лутки
        razmer_h(
            self.ctx,
            sx + (0.5 - 0.2) * CM,
            sy + 0.5 * CM,
            (4 - (0.5 - 0.2) * 2) * CM,
            1,
            d=1,
            text=str(self.door_w + self.SIDE_CLEARANCES)
        )

        # Стоевая лутки

        # Габаритный размер стоевой лутки
        razmer_v(
            self.ctx, sx, sy, 9.5 * CM,
            -1, d=0.5,
            text=str(self.frame_h)
        )
        # Проёмный размер стоевой лутки
        razmer_v(
            self.ctx,
            sx + 0.5 * CM,
            sy + (0.5 - 0.2) * CM,
            (9.5 - 0.5 + 0.2) * CM,
            0.7,
            d=1,
            text=str(self.door_h + self.VERTICAL_CLEARANCES)
        )

    def draw_frame_section(self, sx=18.5 * CM, sy=10 * CM):
        # Сечение лутки

        self.ctx.move_to(sx + CM, sy + 6 * CM)

        for point in ww_external_points:
            self.ctx.rel_line_to(*point)

        self.ctx.close_path()
        self.ctx.set_source_rgb(*g8)
        self.ctx.fill_preserve()
        self.ctx.set_line_width(Small_line_width)
        self.ctx.set_source_rgb(*black)
        self.ctx.stroke()
        self.ctx.set_font_size(8)
        centered_text(
            self.ctx, 18.5, 13, 2.5, 0.5,
            text="Сечение лутки"
        )

    def draw_casing_size(self):
        pass
        # Наличник
        # self.ctx.set_font_size(12)
        # self.ctx.move_to(25.4 * CM, 7 * CM)
        # self.ctx.show_text(str(self.frame_w - 16 * 2))
        # self.ctx.move_to(25.4 * CM, 6.5 * CM)
        # self.ctx.show_text(str(self.frame_w - 16 * 2 + 70 * 2))
        # self.ctx.save()
        # self.ctx.move_to(28.3 * CM, 12 * CM)
        # self.ctx.rotate(3 * math.pi / 2)
        # self.ctx.show_text(str(self.frame_h - 16 + 70))
        # self.ctx.restore()

    def draw_expander_size(self):
        pass
        # Доборы
        # self.ctx.set_font_size(12)
        # expander_h = (
        #     self.door_h + self.VERTICAL_CLEARANCES + self.FRAME_THICKNESS - 23
        # )
        # expander_w = self.frame_w
        # self.ctx.move_to(17.7 * CM, 3.7 * CM)
        # self.ctx.show_text(str(expander_h))
        # self.ctx.move_to(17.9 * CM, 4.3 * CM)
        # self.ctx.show_text(str(expander_w))

    def draw_position_casing_count(self):
        pass
        # Количество комплектов и наличников
        # self.ctx.set_font_size(16)
        # kol = len(self.positions_list)
        # if kol > 1:
        #     msg = "Изготовить {} компл.".format(kol)
        #     self.ctx.move_to(8 * CM, 1.3 * CM)
        #     self.ctx.show_text(msg)
        # msg = "{} компл. наличников".format('1')
        # self.ctx.move_to(8 * CM, 1.9 * CM)
        # self.ctx.show_text(msg)
        # self.ctx.move_to(13.3 * CM, 4 * CM)
        # self.ctx.show_text("1")

    def draw_page(self):
        # размер изображения 1522x1080 точок

        self.ctx.save()

        self.create_from_png()

        self.ctx.scale(0.55, 0.55)
        self.ctx.set_source_surface(self.ims, 0, 0)
        self.ctx.paint()
        self.ctx.restore()

        # Сетка сантиметровая(приблизительно)
        # perymetr(self.ctx)
        draw_carcase(self.ctx)
        draw_finishing_cutting(self.ctx)
        draw_table(self.ctx)

        self.draw_model_name()
        self.draw_positions_number()
        self.draw_door_size()
        self.draw_finish_cut()
        self.draw_carcase_thickness()
        self.draw_carcase_size()

        self.draw_casing_size()
        self.draw_expander_size()
        self.draw_position_casing_count()
        self.draw_frame_ww_external()
        self.draw_frame_size()
        self.draw_frame_section()
        self.draw_rough_table()


class Evolushion_03_primer_Forte_Paint():
    def __init__(self, ctx, order, positions_list, sketch_dir):
        self.ctx = ctx
        self.order = order
        self.positions_list = positions_list[2]
        self.door_h = positions_list[0]
        self.door_w = positions_list[1]
        self.sketch_dir = sketch_dir

        self.surface_name = "Evolshion_03_primer.png"
        # Толщина бруса
        self.TIMBER_THICKNESS = 28
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

    def create_from_png(self):

        img_path = str(self.sketch_dir.joinpath(
            "surface",
            self.surface_name
        ))

        self.ims = cairo.ImageSurface.create_from_png(img_path)

    def draw_model_name(self):
        self.ctx.set_font_size(11)
        # Модель
        self.ctx.move_to(11.5 * CM, 2.4 * CM)
        self.ctx.show_text('Evolushion 03 primer')

    def draw_positions_number(self):
        self.ctx.set_font_size(42)
        # Номер позиции
        (x, y, width, height, dx, dy) = self.ctx.text_extents(
            str(self.positions_list)
        )
        self.ctx.move_to(28 * CM - dx, 2 * CM)
        self.ctx.show_text(str(self.positions_list))

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

    def draw_carcase_thickness(self):
        self.ctx.set_font_size(17)
        # Толщина бруса
        self.ctx.move_to(7.8 * CM, 5.4 * CM)
        self.ctx.show_text(str(self.TIMBER_THICKNESS))

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
        # kol = len(self.positions_list)
        # if kol > 1:
        #     msg = "Изготовить {} компл.".format(kol)
        #     self.ctx.move_to(8 * CM, 1.3 * CM)
        #     self.ctx.show_text(msg)
        msg = "{} компл. наличников".format('1')
        self.ctx.move_to(8 * CM, 1.9 * CM)
        self.ctx.show_text(msg)
        self.ctx.move_to(13.3 * CM, 4 * CM)
        self.ctx.show_text("1")

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

        self.draw_model_name()
        self.draw_positions_number()
        self.draw_door_size()
        self.draw_finish_cut()
        self.draw_carcase_thickness()
        self.draw_carcase_size()
        self.draw_frame_size()
        self.draw_casing_size()
        self.draw_expander_size()
        self.draw_position_casing_count()

        # Сетка сантиметровая(приблизительно)
        # perymetr(self.ctx)
