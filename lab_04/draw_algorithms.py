
def standard_oval(canvas, xc, yc, ra, rb, colour, mode=True):
    canvas.create_oval(xc - ra, yc - rb, xc + ra, yc + rb, outline=colour)


def standard_circle(canvas, xc, yc, r, colour, mode = True):
    canvas.create_oval(xc - r, yc - r, xc + r, yc + r, outline=colour)


def spectrumBy_standart(canvas, xc, yc, ra, rb, step, count, colour):
    for e in range(0, count):
        standard_oval(canvas, xc, yc, ra, rb, colour)
        ra += step
        rb += step


def spectrumCircleBy_algorith(canvas, alg, xc, yc, rs, step, count, colour):
    for e in range(0, count):
        alg(canvas, xc, yc, rs, colour, True)
        rs += step


def spectrumEllipseBy_algorith(canvas, alg, xc, yc, ra, rb, step, count, colour):
    constant = ra / rb
    for e in range(0, count):
        alg(canvas, xc, yc, ra, rb, colour, True)
        ra += step
        rb = round(ra / constant)

def circle_by_algotithm(canvas, alg, xc, yc, radius, colour):
    alg(canvas, xc, yc, radius, colour, True)

def ellipse_by_algotithm(canvas, alg, xc, yc, ra, rb, colour):
    alg(canvas, xc, yc, ra, rb, colour, True)
