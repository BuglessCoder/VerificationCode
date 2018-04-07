#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 11:24:09 2018

@author: lidawei
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 生成随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 生成随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 生成随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 设置尺寸为240 x 60:
width = 240
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 设置模糊效果:
image = image.filter(ImageFilter.BLUR)
image.save('/Users/lidawei/code.jpg', 'jpeg')