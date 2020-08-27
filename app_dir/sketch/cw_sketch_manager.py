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

        self.base_page_list = []

        base_list = [
            [
                p.cw_vendor_code.doors_height,
                p.cw_vendor_code.doors_width,
                p.doors_quantity
            ]
            for p in self.order.cw_positions
        ]

        rough_list = []
        for i in base_list:
            rough_list.extend([[i[0], i[1]]] * i[2])

        unique_list = []
        for item in rough_list:
            if item not in unique_list:
                unique_list.append(item)

        for i in unique_list:
            self.base_page_list.append([
                i[0],
                i[1],
                rough_list.count(i)
            ])
        self.base_page_list.sort(key=lambda i: (i[1], i[0]), reverse=True)

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

        self.ctx.save()
        self.ctx.restore()
