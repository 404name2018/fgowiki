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
    try:
      urllib.request.urlretrieve(imgurl, imgname)
      print("Downloaded {} from {}".format(imgname, imgurl))
    except urllib.error.HTTPError:
      print("404 {}".format(imgurl))

name_index = open("name_index_mp.txt", 'w')
def job(index):
  name = getName(index)
  name_index.write("{:03d} {}\n".format(index, name))
  ns = name.split(',')
  name_en = ns[2]
  getImg(index, name_en, prepath='img')

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(16)
indexes = list(range(1, 201))
pool.map(job, indexes)
pool.close()
