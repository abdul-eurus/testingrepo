import requests
import urllib.request
import re
import string
import sys

url= str(sys.argv[1])

urlrequest=urllib.request.urlopen(url)
urlread = urlrequest.read()
f= open("Linux1.txt","w+")
para=re.findall(r'<body (.*?)</body>',str(urlread))

clean = re.compile(r'(<.*?>)|({.*?})|([\n\r\t\\])')

data= re.sub(clean, '', str(para))
        
f.write(data)
f.write("\t\n\n")
print(data)
f.close() 