# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2016/10/19
Description:
    main.py
----------------------------------------------------------------------------"""

from PyTexturePacker import Packer


def pack_test(list):
    # create a MaxRectsPacker
    packer = Packer.create(max_width=1024, max_height=256, enable_rotated = False,bg_color=0xffffff00)
    # pack texture images under the directory "test_case/" and name the output images as "test_case".
    # "%d" in output file name "test_case%d" is a placeholder,  = Fakswhich is a multipack index, starting with 0.
    packer.pack(list, "PyTexturePacker/list/vram%d", "")


def main():
    pack_test()


if __name__ == '__main__':
    main()
