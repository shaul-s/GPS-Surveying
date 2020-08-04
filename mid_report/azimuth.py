from numpy import pi, arctan


def azimuth(dx, dy):
    # calculate azimuth from two 2d points
    # dx = x2 - x1
    # dy = y2 - y1

    if (dx == 0) and (dy == 0):
        az = 0
        return az

    if dx == 0:
        if dy < 0:
            az = (3 / 2) * pi
            return az
        else:
            az = (pi / 2)
            return az

    preaz = arctan(abs(dy / dx))

    if dx > 0:
        if dy < 0:
            az = 2 * pi - preaz
            return az

    if dx < 0:
        if dy < 0:
            az = pi + preaz
            return az
        else:
            az = pi - preaz
            return az

    return preaz
