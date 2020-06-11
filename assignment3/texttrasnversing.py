import requests
import urllib.request
import re
import string
import sys

url= str(sys.argv[1])

urlrequest=urllib.request.urlopen(url)
urlread = urlrequest.read()
f= open("Linux1.txt","w+")
para=re.findall(r'<p>(.*?)</p>',str(urlread))

for eachPara in para:

    clean = re.compile(r'(<.*?>)|({.*?})|([\n\r\t\\])')

    paragraph= re.sub(clean, '', str(eachPara))
        
    f.write(paragraph)
    f.write("\t\n\n")
    print(paragraph)
f.close() 
