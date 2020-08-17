from pathlib import Path

import cairo

from flask import current_app

from app_dir.models import CW_order

from app_dir.sketch.evolushion_03 import \
    Cw_evolushion_03_primer_ww_external

from app_dir.sketch.sketch_config import black


class Pdf_Generator():

    def __init__(self, order_number):
        self.order = CW_order.query.filter_by(
            order_number=order_number
        ).first()

    def set_output_file(self):

        self.sketch_dir = Path(current_app.root_path) / "sketch"
        self.result_dir = Path(current_app.root_path) / "static" / "pdf"

        self.filename = "{}_sketch.pdf".format(self.order.order_number)

        self.filename_path = str(self.result_dir.joinpath(
            self.filename
        ))

        surface = cairo.PDFSurface(self.filename_path, 842, 595)
        self.ctx = cairo.Context(surface)
        self.ctx.select_font_face("Times New Roman")
        self.ctx.set_source_rgb(*black)

    def get_combined_positions(self):
        self.base_page_list = [
            (2000, 600, p.doors_quantity)
            for p in self.order.cw_positions
        ]

        self.base_page_list

    def destr(self):
        # surface.show_page()
        self.ctx.save()
        self.ctx.restore()

    def run(self):

        self.set_output_file()
        self.get_combined_positions()

        for i in self.base_page_list:
            e = Cw_evolushion_03_primer_ww_external(
                self.ctx,
                self.order,
                i,
                self.sketch_dir
            )

            e.draw_page()

            self.ctx.show_page()

        self.destr()
