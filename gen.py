#!/usr/bin/python

import os
import sys
from PIL import Image, ImageDraw, ImageFont
from datetime import date, timedelta
from subprocess import call

imgDir = 'images/'
scriptDir = 'scripts/'
gitfile = '.blob'
# GitHub uses Sunday-starting weeks, so add 1
offset = (date.today().weekday() + 1) % 7
rows = 7
cols = 52
size = (cols, rows)
numdays = rows * cols


def commit(days_ago, msg):
    d = date.today() - timedelta(days=days_ago)
    t = str(d) + " 00:00:00"
    os.system("echo " + msg + " > .tmpfile")
    os.system("git add .tmpfile")
    os.system('GIT_COMMITTER_DATE="' + t + '"' + ' GIT_AUTHOR_DATE="' +
              t + '"' + ' git commit -m "' + msg + '" 2>&1 >/dev/null')


def write_px(x, y, intensity, prefix=""):
    days_ago = numdays + offset - (x * rows + y)
    # d = date.today() - timedelta(days=days_ago)
    # t = str(d) + " 00:00:00"
    # print "val=",intensity, "x",x,"y",y,"date:",d
    print(x, y)
    print(intensity)
    # print(days_ago)
    print('-------------')
    # for i in range(0, intensity):
    # msg = prefix + os.urandom(8).encode("hex")
    # commit(days_ago, msg)


def rgb2gray(rgb):
    r, g, b = rgb[0:3]  # ignore alpha for now
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray


def process_image(path):
    img = Image.open(path)
    imap = path + '.map'
    file = open(imap, "w")
    px = img.load()
    size = img.size
    if (52, 7) != size:
        raise Exception("Image should be 52x7, got " + size)
    for y in range(size[1]):
        file.write('\n')
        for x in range(size[0]):
            val = 255 - int(rgb2gray(px[x, y]))
            val //= 16
            if(val>0):
                file.write("#")
            else: file.write(' ')
    for x in range(size[0]):
        for y in range(size[1]):
            val = 255 - int(rgb2gray(px[x, y]))
            val //= 16
            print(val)
            # write_px(x, y, val, prefix="ign-")
    file.close()


def process_text(txt, offset=2):
    f = 1
    image = Image.new("RGB", [x * f for x in size], (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.fontmode = "1"
    font = ImageFont.truetype("font/5x5_pixel.ttf", 8)
    draw.text((offset, 1), txt, (0, 0, 0), font=font)

    image.save(imgDir + txt + ".bmp")


def main():
    if sys.argv[1] == "--text":
        process_text(sys.argv[2])
    else:
        process_image(sys.argv[1])


if __name__ == "__main__":
    main()
