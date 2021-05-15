#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 15:14:55 2021

@author: kivancaykac
removes every 24th frame in an exported image sequence file

!!! becareful before running. Make sure you backup first!!!
"""
import os

images = int(input("how many still images want to get at the end? "))
fps = int(input("what is the fps?\nanswer: "))
directory_path = input("input directory path?\nanswer: ")
zfill_size = int(input("what is zfill size?\n(eg: zfill=4==>0000)\nanswer: "))

file_naming = "frame-"
ext = ".png"
wanted_frame_count = 0

for i in range(images*fps):
    if i == fps*wanted_frame_count:
        wanted_frame_count += 1
    else:
        os.remove(directory_path+file_naming+f"{i}".zfill(zfill_size)+ext)
