# Script to get stock price from google finance
import re
import urllib.request
url="https://www.google.com/finance?q="
stock= input("Enter your stock")
url = url + stock
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
m = re.search('meta itemprop="price"',data1)
start=m.start()

"""print(data1[start:m.end()])
print("______________________________")
print(data1[start:start+50])
print("______________________________")"""

end=start + 50
newstr=data1[start:end]
m=re.search('content="',newstr)
start=m.end()
newstr1=newstr[start:]
m=re.search("/",newstr1)
start=0
end=m.end()-3
final=newstr1[0:end]
print("Value of stock=" + final)
