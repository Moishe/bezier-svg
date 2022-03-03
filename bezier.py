import math

STEPS = 100
ACTORS = [
    {
        'radius': 150,
        'freq': 1,
        'offset': 0
    },
    {
        'radius': 100,
        'freq': 1,
        'offset': math.pi / 8
    },
    {
        'radius': 280,
        'freq': 2,
        'offset': math.pi
    },
]

MM = 3.543307

WIDTH = 210 * MM
HEIGHT = 290 * MM

header = '<svg width="%dmm" height="%dmm" xmlns="http://www.w3.org/2000/svg">\n' % (WIDTH / MM, HEIGHT / MM) + '<rect width="100%" height="100%" fill="white"/>\n'
footer = '</svg>\n'

path_template = '<path d="%s" stroke="black" fill-opacity="0" stroke-width="0.1"/>\n'

lines = []

f = open('output.svg', 'w')

f.write(header)

path = ""

prev_coords = None
for idx in range(0, STEPS):
    coords = []
    for (i, a) in enumerate(ACTORS):
        t = (idx / STEPS + (i / STEPS) / len(ACTORS) + a['offset']) * math.pi * 2 * a['freq']
        coords.append([math.cos(t) * a['radius'] + (WIDTH / 2), math.sin(t) * a['radius'] + (HEIGHT / 2)])

    path = "M %d %d" % (coords[0][0], coords[0][1])
    path += " Q %d %d %d %d" % (coords[1][0], coords[1][1], coords[2][0], coords[2][1])

    for coord in coords[3:]:
        path += " T %d %d" % (coord[0], coord[1])
    """
    else:
        path += " T %d %d" % (coords[0][0], coords[0][1])
        #for coord in coords:
        #    path += " T %d %d" % (coord[0], coord[1])

        lines.append([coords[0], coords[1]])
    """
    prev_coords = coords

    f.write(path_template % path)

#for line in lines:
#    f.write('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="black" />' % (line[0][0], line[0][1], line[1][0], line[1][1]))

f.write(footer)
f.close()
