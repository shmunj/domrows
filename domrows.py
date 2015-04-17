#!/usr/bin/python
from PIL import Image
import sys

def avgColor(pixels):
    most = max(pixels.values())
    for key, value in pixels.iteritems():
        if value == most:
            color = key
            break
    return color

def getBg(pic):
    edges = {}
    for y in range(pic.size[1]): #best for portraits
        for x in [1, pic.size[0]]:
            pixel = pic.getpixel((1, y))
            try:
                edges[pixel] += 1
            except:
                edges[pixel] = 1
    return avgColor(edges) 

old = Image.open(sys.argv[1])
img = Image.new('RGB', old.size)

saveas = None
if len(sys.argv) == 3:
    saveas = sys.argv[2]

bg = getBg(old)

for y in range(old.size[1]):
    pixels = {}
    for x in range(old.size[0]):
        pixel = old.getpixel((x, y))
        if pixel != bg:
            try:
                pixels[pixel] += 1
            except:
                pixels[pixel] = 1

    try:
        newpixel = avgColor(pixels)
    except:
        newpixel = bg

    for x in range(old.size[0]):
        img.putpixel((x, y), newpixel)

if saveas:
    img.save(saveas)
else:
    old.show()
    img.show()
