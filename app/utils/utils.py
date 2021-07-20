import math


def tile2long(x: int, z: int):
    return x / (float)(1 << z) * 360.0 - 180


def tile2lat(y: int, z: int):
    n = math.pi - 2.0 * math.pi * y / (float)(1 << z)
    return 180.0 / math.pi * math.atan(0.5 * (math.exp(n) - math.exp(-n)))


def tile2bbox(z: int, x: int, y: int):
    SW_long = str(tile2long(x, z))

    SW_lat = str(tile2lat(y + 1, z))

    NE_long = str(tile2long(x + 1, z))

    NE_lat = str(tile2lat(y, z))

    bbox = SW_long + ',' + SW_lat + ',' + NE_long + ',' + NE_lat

    return bbox
