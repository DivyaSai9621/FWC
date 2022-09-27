#!/rbin/bash
cd /sdcard/Download/aasith/assembly
avra hello.asm
texfot pdflatex assembly.tex
termux-open assembly.pdf
