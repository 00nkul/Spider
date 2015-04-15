#-*- coding:utf-8 -*-
import urllib2
import re

url = raw_input()
html = urllib2.urlopen(url)
pattern = re.compile('<td>.*?href="(.*?)".*?target.*?title=(.*?)>.*?</a></td>',re.S)
items = re.findall(pattern,html.read())
for item in items:
	print item[1]
	html2 = urllib2.urlopen(item[0])
	pattern2 = re.compile('</span><em>.*?</span><em>(.*?)</em></li>.*?src="(.*?)".*?align=".*?/>',re.S)
	items2 = re.findall(pattern2,html2.read())
	for item2 in items2:
		print item2[0].strip(),'<img src="http://www.ganji.com'+item2[1],'">'
	print '<br/>'

