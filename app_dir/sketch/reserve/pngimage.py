#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cairo


def main():

    f_weight = 640
    f_height = 480

    ims = cairo.ImageSurface(
        cairo.FORMAT_ARGB32,
        f_weight,
        f_height
    )
    cr = cairo.Context(ims)

    cr.set_source_rgb(0, 200, 32)
    cr.select_font_face(
        "Sans",
        cairo.FONT_SLANT_NORMAL,
        cairo.FONT_WEIGHT_NORMAL
    )
    cr.set_font_size(128)

    cr.move_to(10, f_height / 2)
    cr.show_text("Disziplin ist Macht.")

    ims.write_to_png("image.png")


if __name__ == "__main__":
    main()
