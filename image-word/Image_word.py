#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    处理图片变成-文字的一个转变,需要PIL
    pip install PIL
    from PIL import Image
"""


from PIL import Image
import os
  
serarr = '''@#$%&?*aeoc=<{[(/l|!-_:;,."'^~` '''
#serarr  = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''
count  = len(serarr)
  
def toText(image_file):#此函数不能输入 gif 文件
   image_file = image_file.convert("L")#转灰度
   strs       = ''#储存字符串
   for h in range(0, image_file.size[1]):#h
      for w in range(0, image_file.size[0]):#w
         gray = image_file.getpixel((w,h))
         strs  = strs + serarr[int(gray/(256/(count)))]
      strs = strs + '\r\n'
   return strs
  
def toText2(image_file):
   strs =''#储存字符串
   for h in range(0,  image_file.size[1]):#h
      for w in range(0, image_file.size[0]):#w
         r,g,b = image_file.getpixel((w,h))
         gray  = int(r* 0.299 + g* 0.587 + b* 0.114)
         strs  = strs + serarr[int(gray/(256/(count)))]
      strs = strs + '\r\n'
   return strs
  
fi = open('11.jpg', 'rb')
image_file = Image.open(fi) # 打开图片
image_file = image_file.resize((int(image_file.size[0]*0.2), int(image_file.size[1]*0.05)))#调整图片大小
print u'Info:',image_file.size[0],' ',image_file.size[1],' ',count
fi.close()
  
     
tmp = open('tmp.txt','w')
tmp.write(toText(image_file))
tmp.close()
