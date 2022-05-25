#!/usr/bin/env python3

# from xml.dom import minidom

file='bt.xml' # name of library file
name='BTLOGOM' # name of package

# mydoc = minidom.parse(file)
# items = mydoc.getElementsByTagName('package')
#

# scale certain drawing elements in Eagle library

import xml.etree.ElementTree as ET

tree = ET.parse(file)
root = tree.getroot()
scale = 0.6

packages = root.findall(".//package[@name='{}']".format(name))

def do_scale(item, attrs, s):
    for a in attrs:
        v = float(item.attrib[a]) * s
        item.attrib[a] = "{}".format(v)
    return item

for p in packages:
    items = p.findall(".//")
    for i in items:
        if i.tag == "circle":
            i = do_scale(i, ['x','y','radius','width'], scale)
        if i.tag == "wire":
            i = do_scale(i, ['x1','y1','x2','y2','width'], scale)
        if i.tag == "polygon":
            i = do_scale(i, ['width'], scale)
        if (i.tag == "vertex"):
            i = do_scale(i, ['x','y'], scale)

    ET.dump(p)

# circle
# polygon
# vertex
# wire
