import ImageChops
import math
import operator


def rmsdiff(im1, im2):
    "Calculate the root-mean-square difference between two images"

    h = ImageChops.difference(im1, im2).histogram()

    # calculate rms
    return math.sqrt(reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))) / (float(im1.size[0]) * im1.size[1]))


import ImageChops

def equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None