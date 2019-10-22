#!/bin/bash

convert -size 1000x15000 xc:white -font "Liberation-Serif" -pointsize 30 -fill black +antialias -annotate +15+15 "@pg345.txt" +repage image-in.png

convert -size 1000x15000 xc:white -font "Liberation-Serif" -pointsize 30 -fill black -antialias -annotate +15+15 "@pg345.txt" +repage image-out.png
