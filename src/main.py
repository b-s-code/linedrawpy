#!/usr/bin/python3
import re
import sys
import fileinput
import linedrawpy

# Params.
padding = 10 # pixels
bgcolour = "ffffff" # hex rep

def compile_lines(input_lines):
    # Strip trailing newlines.  Strip all spaces. 
    # TODO : consider supporting parentheses in input, stripping them here.
    lines = [line.replace(' ', '').rstrip() for line in input_lines]

    # Check validity of input.    
    # Here we support colours represented as 6 hex digits.
    # E.g. the line
    #     5 , 25, 400 , 400 , ff0077
    # defines a purple-red line from (5, 25) to (400, 400).
    valid_edge_regex = re.compile("[-\d]{1,}\.{0,1}\d*,[-\d]{1,}\.{0,1}\d*,[-\d]{1,}\.{0,1}\d*,[-\d]{1,}\.{0,1}\d*,[0-9A-Fa-f]{6}")
    line_is_valid_edge = lambda line : valid_edge_regex.fullmatch(line) != None
    for i, line in enumerate(lines):
        if not line_is_valid_edge(line):
            raise Exception("^^^ Bad input on line " + str(i))

    # Decode input.
    edge_parts = [line.split(',') for line in lines]  
    x_1_arr = [int(float(line[0])) for line in edge_parts]
    y_1_arr = [int(float(line[1])) for line in edge_parts]
    x_2_arr = [int(float(line[2])) for line in edge_parts]
    y_2_arr = [int(float(line[3])) for line in edge_parts]
    colour_arr = [line[4] for line in edge_parts]
    
    # Compile decoded input to an image.
    x_min = min(x_1_arr + x_2_arr)
    y_min = min(y_1_arr + y_2_arr)
    x_max = max(x_1_arr + x_2_arr)
    y_max = max(y_1_arr + y_2_arr)

    translation_x = padding - x_min
    translation_y = padding - y_min
    canvas_width = x_max - x_min + 2 * padding
    canvas_height = y_max - y_min + 2 * padding

    img = linedrawpy.create_image(canvas_width, canvas_height, bgcolour)
    for edge in edge_parts:
        img = linedrawpy.add_edge(img, edge, translation_x, translation_y)
    
    # Output the image.
    linedrawpy.print_image(img, canvas_width, canvas_height)

if __name__ == "__main__":
    # Check validity of params.
    # TODO : only need to check bgcolour.
    input_lines = fileinput.input()
    # Get input from file or standard input
    compile_lines(input_lines)
