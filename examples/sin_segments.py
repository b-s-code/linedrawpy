import math

# Parameters.
amplitude = 100
horiz = 100
colour = "00ff00"
colours = ["43B023", "57FC26", "0DFCF0", "00B0A6", "FC2519"]
for x in range(0, int(horiz * 2 * math.pi)):
    print(x, ',', amplitude * math.sin(x / horiz), ',', x + 1, ',', amplitude * math.sin((x + 1) / horiz), ',', colours[(x // 20) % len(colours)])
