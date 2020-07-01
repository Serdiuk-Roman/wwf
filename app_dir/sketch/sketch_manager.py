from pathlib import Path

import cairo

from app_dir import app

from app_dir.models import Order

from app_dir.sketch.evolushion_03_primer_forte_paint import \
    Evolushion_03_primer_Forte_Paint

from app_dir.sketch.sketch_config import *


class Pdf_Generator():

    def __init__(self, order_number):
        self.order = Order.query.filter_by(order_number=order_number).first()

    def set_output_file(self):

        self.sketch_dir = Path(app.root_path) / "sketch"

        filename = str(self.sketch_dir.joinpath(
            "resume",
            "{}.pdf".format(self.order.order_number)
        ))

        surface = cairo.PDFSurface(filename, 842, 595)
        self.ctx = cairo.Context(surface)
        self.ctx.select_font_face("Times New Roman")
        self.ctx.set_source_rgb(*black)

    def get_combined_positions(self):
        door_size = \
            [(p.doors_height, p.doors_width, p.serial_number)
             for p in self.order.positions]

        print(door_size)
        return door_size

    def destr(self):
        # surface.show_page()
        self.ctx.save()
        self.ctx.restore()

    def run(self):
        self.set_output_file()

        base_page_list = self.get_combined_positions()

        for i in base_page_list:
            e = Evolushion_03_primer_Forte_Paint(
                self.ctx,
                self.order,
                i,
                self.sketch_dir
            )

            e.draw_page()
            e.draw_model_name()
            e.draw_positions_number()
            e.draw_door_size()
            e.draw_finish_cut()
            e.draw_carcase_thickness()
            e.draw_carcase_size()
            e.draw_frame_size()
            e.draw_casing_size()
            e.draw_expander_size()
            e.draw_position_casing_count()
            self.ctx.show_page()

        self.destr()
