import urllib
import urllib.request
import re
import sys, os

def getHTML(url):
  page = urllib.request.urlopen(url)
  html = page.read()
  return html.decode('utf-8')

def getName(index):
  url='https://fgowiki.com/guide/petdetail/'+str(index)
  html = getHTML(url)
  reg = r'<meta name="keywords" content="(.+?),Fate/Grand Order,Fate全系列英灵,角色详细,fategrandorder,Servant About">'
  nameRe = re.compile(reg)
  name = nameRe.findall(html)
  name = name[0]
  return name

print(getName(200))
print(getName(1))
