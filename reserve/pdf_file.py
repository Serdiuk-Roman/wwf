#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cairo
# from math import pi
import color
from setting import Base_line_width
import forte_10


def main():

    pdf = cairo.PDFSurface("pdffile.pdf", 842, 595)
    ctx = cairo.Context(pdf)
    ctx.set_line_width(Base_line_width)
    # ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    # ctx.set_line_join(cairo.LINE_JOIN_ROUND)

    color.perymetr(ctx)

    forte_10.carcase(ctx)

    # forte_10.finish_cut(ctx)
    forte_10.finishing_cutting(ctx)
    forte_10.lutka(ctx)
    forte_10.se4enie_lutky(ctx)
    forte_10.lyshtva(ctx)

    forte_10.razmer(ctx)

    ctx.save()
    ctx.restore()


if __name__ == "__main__":
    main()
