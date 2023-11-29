def is_hex_colour_str_valid(bgcolour: str) -> bool:
    """
    Returns True if bgcolour is a valid hex
    representation of a colour.
    """
    # TODO : Use in main.
    # TODO : Consider making bgcolour a command line option,
    # s.t. "ffffff" is used if option not specified.
    if len(bgcolour) != 6:
        return False
    valid_chars = "abcdefABCDEF0123456789"
    for char in bgcolour:
        if char not in valid_chars:
            return False
    return True

def hex_str_colour_to_dec_str_colour(hex_str: str) -> str:
    """
    Takes 6 hex digits.
    Returns space joined string representations of
    colour components.
    E.g. "E2f973" maps to "226 249 115"
    """
    red = int("0x" + hex_str[0:2], 16)
    green = int("0x" + hex_str[2:4], 16)
    blue = int("0x" + hex_str[4:6], 16)
    return str(red) + ' ' + str(green) + ' ' + str(blue)

def create_image(width: int, height: int, bgcolour_hex_str: str) -> list[list[int]]:
    """
    Returns a 2x2 matrix. Each element is
    a colour component, belonging to a subpixel,
    represented in base 10.
    I.e. 0, 1, ... , 256 are possible element values.
    """
    colour_decimal_str = hex_str_colour_to_dec_str_colour(bgcolour_hex_str)
    return [[colour_decimal_str for col_num in range(width)] for row_num in range(height)]

def add_edge(image: list[list[str]], edge: list[str], translation_x, translation_y) -> list[list[int]]:
    """
    Takes in a 2x2 matrix of colour components and a coloured line
    segment, encoded as ["<x_1>", "<y_1>", "<x_2>", "<y_2> ", "<colour>"].
    Returns a 2x2 matrix of colour components,
    with the line segment from (x_1, y_1) to (x_2, y_2)
    added to the image, in the given colour.
    """
    x_1 = int(float(edge[0])) + translation_x
    x_2 = int(float(edge[2])) + translation_x
    
    # Mulitply by -1 to orient output for humans, not machines.
    y_1 = -1 * int(float(edge[1])) - translation_y
    y_2 = -1 * int(float(edge[3])) - translation_y
    
    colour = hex_str_colour_to_dec_str_colour(edge[4])

    # Use digital differential analyzer algorithm.

    dx = x_2 - x_1
    dy = y_2 - y_1

    step = abs(dy) if abs(dy) > abs(dx) else abs(dx)
    if step == 0:
        return image
    dx /= step
    dy /= step
    x = x_1
    y = y_1
    i = 0
    while i <= step:
        image[int(y)][int(x)] = colour
        x += dx
        y += dy
        i += 1

    return image

def print_image(image: list[list[str]], width: int, height: int) -> None:
    """
    Prints image, formatted appropriately with Portable PixMap header,
    to standard output.
    """
    print("P3") 
    print(str(width) + " " + str(height))
    print("255")
    for row in image:
        for elt in row:
            print(elt)
