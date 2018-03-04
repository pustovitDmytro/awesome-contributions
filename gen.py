#!/usr/bin/python
import sys
import imp
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta

imgDir = 'images/'
scriptDir = 'scripts/'
gitfile = '.blob'
# GitHub uses Sunday-starting weeks, so add 1
offset = (datetime.today().weekday() + 1) % 7
rows = 7
cols = 52
size = (cols, rows)
numdays = rows * cols


def commit(file, stamp, msg, author='pustovitDmytro <dipustovit@gmail.com>'):
    # file.write("\nsleep 1")
    file.write("\necho '" + stamp + '#' + msg + "' >> " + gitfile)
    # file.write("\nsleep 1")
    file.write('\ngit commit -a -m "' + msg + '" --date ' + stamp + ' --author="' + author + '"')


def write_px(file, x, y, intensity, prefix="", author=''):
    days_ago = numdays + offset - (x * rows + y)
    for i in range(0, intensity):
        d = datetime.today() - timedelta(days=days_ago, seconds=i)
        stamp = d.isoformat()
        msg = str(days_ago) + '_' + str(i)
        commit(file, stamp, msg)


def rgb2gray(rgb):
    r, g, b = rgb[0:3]  # ignore alpha for now
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray


def process_image(path, count = 20, saveAs='', author=''):
    img = Image.open(path)
    imap = path + '.map'
    imgName = path.split('/')[-1].split('.')[0]
    file = open(imap, "w")
    savePath = saveAs if saveAs else 'scripts/' + imgName + '.git.sh'
    fileSh = open(savePath, "w")
    fileSh.write('#!/bin/sh\nset -e\n')
    fileSh.write('git fsck --unreachable\n')
    fileSh.write('git reflog expire --expire=0 --all\n')
    fileSh.write('git repack -a -d -l\n')
    fileSh.write('git prune\n')
    fileSh.write('git gc --aggressive\n')
    px = img.load()
    size = img.size
    if (52, 7) != size:
        raise Exception("Image should be 52x7, got " + size)
    for y in range(size[1]):
        file.write('\n')
        for x in range(size[0]):
            val = 255 - int(rgb2gray(px[x, y]))
            val //= 16
            if(val > 0):
                file.write("#")
            else:
                file.write(' ')
    for x in range(size[0]):
        for y in range(size[1]):
            val = 255 - int(rgb2gray(px[x, y]))
            val //= 255
            val *= count
            write_px(fileSh, x, y, val, prefix="ign-", author=author)
    file.close()
    fileSh.close()


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
    elif sys.argv[1] == "--config":
        module = imp.load_source('module', sys.argv[2])
        from module import variants, name, count, author
        variant = variants[0]
        process_text(variant)
        process_image(imgDir + variant + ".bmp", count, name, author)
    else:
        process_image(sys.argv[1])


if __name__ == "__main__":
    main()
