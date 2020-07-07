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
        self.result_dir = Path(app.root_path) / "static" / "pdf"

        self.filename = "{}_sketch.pdf".format(self.order.order_number)

        self.filename_path = str(self.result_dir.joinpath(
            self.result_dir,
            self.filename
        ))

        surface = cairo.PDFSurface(self.filename_path, 842, 595)
        self.ctx = cairo.Context(surface)
        self.ctx.select_font_face("Times New Roman")
        self.ctx.set_source_rgb(*black)

    def get_combined_positions(self):
        self.base_page_list = \
            [(p.doors_height, p.doors_width, p.serial_number)
             for p in self.order.positions]

        self.base_page_list

    def destr(self):
        # surface.show_page()
        self.ctx.save()
        self.ctx.restore()

    def run(self):

        self.set_output_file()
        self.get_combined_positions()

        for i in self.base_page_list:
            e = Evolushion_03_primer_Forte_Paint(
                self.ctx,
                self.order,
                i,
                self.sketch_dir
            )

            e.draw_page()

            self.ctx.show_page()

        self.destr()
