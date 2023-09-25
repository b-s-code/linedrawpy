import math

radius_0 = 100 

line_colour = "ff0000"
num_flakes_per_belt = 8 

# Essentially number of onion layers.
num_belts = 9

# This is the Golden Ratio.
phi = (1 + 5 ** 0.5) / 2

# i is belt number
def get_flake_radius(radius_0, i):
    flake_radius = int(radius_0 * (1 / phi ** (i))) 
    return flake_radius

# i is belt number
def get_belt_radius(radius_0, i):
    if i == 0:
        return 0;
    if i == 1:
        return get_flake_radius(radius_0, 0) + get_flake_radius(radius_0, 1)
    return get_flake_radius(radius_0, 0) + 2 * sum([get_flake_radius(radius_0, j) for j in range(1, i)]) + get_flake_radius(radius_0, i)

def get_snowflakes(num_flakes: int, flake_radius: float, belt_radius: float, line_colour: str):
    """
        Return a paragraph of LineDrawPy input representing num_flakes,
        flakes, each with radius flake_radius.  The resulting flakes
        will be spaced equally around the circle, centered at the origin,
        with radius belt_radius.
    """
    
    # Angle between flake centers.
    delta_radians = (2 * math.pi) / num_flakes
    
    # Principal arguments of flakes' centers.
    princ_args = [0 + delta_radians * k for k in range(num_flakes)]

    # Determine encoded coloured edges required to draw all flakes in the belt.
    belt_total_edges = []
    for i, theta_belt in enumerate(princ_args):
        center_x = int(belt_radius * math.cos(theta_belt))
        center_y = int(belt_radius * math.sin(theta_belt))
        
        flake_edges = []
        for i, theta_flake in enumerate(princ_args):
        
            edge_outer_pt_x = center_x + int(flake_radius * math.cos(theta_flake))
            edge_outer_pt_y = center_y + int(flake_radius * math.sin(theta_flake))
            parts = [str(center_x), str(center_y), str(edge_outer_pt_x), str(edge_outer_pt_y), line_colour + '\n']
            edge = ','.join(parts)
            flake_edges.append(edge)
        belt_total_edges.append(''.join(flake_edges))
    return ''.join(belt_total_edges)

print(''.join([get_snowflakes(num_flakes_per_belt, get_flake_radius(radius_0, i), get_belt_radius(radius_0, i), line_colour) for i in range(num_belts)]).rstrip())