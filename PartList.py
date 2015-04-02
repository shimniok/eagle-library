#!/usr/bin/python

# list parts in the bt_*.lbr files

import os.path
from lxml import etree

for f in os.listdir(os.getcwd()):
	if f.endswith(".lbr") and f.startswith("bt_"):
		print " *", f
		try:
			tree = etree.parse(f)
			root = tree.getroot()
			for device in root.findall("./drawing/library/devicesets/deviceset"):
				print "   *", device.get("name")
		except:
			print "   * not xml"
