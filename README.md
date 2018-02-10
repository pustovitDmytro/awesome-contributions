# awesome-contributions
This is fork of another [repository](https://github.com/twinone/awesome-contributions) made by twinone.

# Content

# Requirements
python3
pip
Pillow (PIL)
# Usage

1. Clone this repository:
```bash
git clone https://github.com/pustovitDmytro/awesome-contributions
cd awesome-contributions
```

2. Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```

3. Generate image from text:

*You may skip this step if you already have 52x7 image to show in you profile.*

```bash
python3 gen.py --text "SOME TEXT"
```
and check results at ```images/SOME TEXT.bmp```

4. Generate bash script from image:
**NOTE** For correct work 
* Replace the test.png image by the 52x7 image you want as background (can be other formats too)

* Run the generator:

```
# In the awesome-contributions directory:
python gen.py test.png
```
* Push the changes to **your** GitHub repository:
```
git push github master
```

# Usage (Text)
You can also generate an image containing whatever text you want:
```
python gen.py --text "AWESOME"
```
Will generate AWESOME.bmp for you:

![screenshot from 2016-05-18 22 43 41](https://cloud.githubusercontent.com/assets/4309591/15374320/fadf26ec-1d49-11e6-82c6-72dc8d6183f1.png)

Then you just run the program the normal way:
```
python gen.py AWESOME.bmp
```
## Improvements
* python3
* generating bash file instead running git commands directly
* bitmap .txt images added

## TODO
* add autoupdating of image each 2 weeks
* add more fonts with instant preview

## Notes
* Each week the image will be shifted to the left, so if you leave some padding you can update once every two months or so.
* Make sure to leave at least a few weeks of space at the right so you don't spam the people who follow you.
