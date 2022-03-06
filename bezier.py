import math

STEPS = 256
ACTORS = [
    {
        'radius': 300,
        'freq': 1,
        'offset': 0
    },
    {
        'radius': 350,
        'freq': 2,
        'offset': 0
    },
    {
        'radius': 300,
        'freq': -2,
        'offset': math.pi
    },
]

MM = 3.543307

WIDTH = 210 * MM
HEIGHT = 290 * MM

header = '<svg width="%dmm" height="%dmm" xmlns="http://www.w3.org/2000/svg">\n' % (WIDTH / MM, HEIGHT / MM)
footer = '</svg>\n'

path_template = '<path d="%s" stroke="black" fill-opacity="0" stroke-width="0.2"/>\n'

lines = []

f = open('output.svg', 'w')

f.write(header)

path = ""

for idx in range(0, STEPS):
    coords = []
    for (i, a) in enumerate(ACTORS):
        t = (idx / STEPS) * math.pi * 2 * a['freq'] + a['offset']
        coords.append([math.cos(t) * a['radius'] + (WIDTH / 2), math.sin(t) * a['radius'] + (HEIGHT / 2)])

    path = "M %d %d" % (coords[0][0], coords[0][1])
    path += " Q %d %d %d %d" % (coords[1][0], coords[1][1], coords[2][0], coords[2][1])

    for coord in coords[3:]:
        path += " T %d %d" % (coord[0], coord[1])

    f.write(path_template % path)

f.write(footer)
f.close()
