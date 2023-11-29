#!/bin/bash

# TODO : consider whether there's an appealling option
# for obsoleting this with Makefile.

python3 examples/$1.py> examples/edges_$1.txt
python3 src/main.py examples/edges_$1.txt > examples/output/$1.ppm
convert examples/output/$1.ppm examples/output/$1.png
feh examples/output/$1.png
