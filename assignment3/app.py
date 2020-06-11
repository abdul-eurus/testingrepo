import requests
import urllib.request
import re
import string
import sys

pass0= str(sys.argv[1])

x=urllib.request.urlopen(pass0)
#m=re.compile('<p>(.*?)</p>', re.DOTALL).findall(str(clearx))
data = x.read()
f= open("Linux1.txt","w+")
ne=1
para=re.findall(r'<body (.*?)</body>',str(data))

for eachP in para:
    para=eachP

    clean = re.compile('<.*?>')

    xim= re.sub(clean, '', str(para))

    clean1 = re.compile('{.*?}')

    xim= re.sub(clean1, '', str(xim))

    regex = re.compile(r'[\n\r\t\\]')

    alp = re.sub(regex,' ', xim)
        
    f.write(alp)
    f.write("\t\n\n")
    print(alp)
f.close()
