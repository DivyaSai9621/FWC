#!/rbin/bash
cd /sdcard/fwc/codes
pio run
texfot pdflatex divyasai.tex
termux-open divyasai.pdf
