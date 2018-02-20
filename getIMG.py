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

def getImg(index, name_en, prepath='test'):
  name_en = name_en.replace(' ', '_')
  if not os.path.isdir(prepath):
    os.makedirs(prepath)
  for i in "ABCD":
    #imgurl="http://img.fgowiki.com/fgo/card/servant/" +  '200' + i + '.png'
    imgname = "{1:03d}{0}.{2}.png".format(i, index, name_en)
    imgname = os.path.join(prepath, imgname)
    imgurl="http://img.fgowiki.com/fgo/card/servant/{:03d}{}.png".format(index, i)
    #print("Downloading {} from {}".format(imgname, imgurl))
    urllib.request.urlretrieve(imgurl, imgname)
    print("Downloaded {} from {}".format(imgname, imgurl))

name_index = open("name_index.txt", 'w')
for index in range(1, 201):
  name = getName(index)
  name_index.write("{:03d} {}\n".format(index, name))
  ns = name.split(',')
  name_en = ns[2]
  getImg(index, name_en, prepath='img')
#print(getName(200))
#print(getName(1))
#for name in nameRe:
#    urllib.request.urlretrieve(imgurl,'{}{}.png'.format(name,x))
#    x=x+1
#  return name
#html=gethtml("http://img.fgowiki.com/fgo/card/servant/200D.png)
#print(getImg(html))

