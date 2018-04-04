import pandas as pd
import os
import re
import requests

url = 'http://www.360doc.com/content/07/0310/18/17841_392130.shtml'
content = requests.get(url).text
# with open('content.txt', 'w', encoding = 'utf-8-sig') as txtfile:
# 	txtfile.write(content)

# with open('content.txt', 'r', encoding = 'utf-8-sig') as txtfile:
# 	contents = txtfile.read().replace('\n', '').replace(' ', '')

contents = content.replace('\n', '').replace(' ', '')
bookPatterns = re.compile(r'(《.*?》.*?)<br>')
urlPatterns = re.compile(r'<ahref="(http://www.swdyj.com.*?\.(exe|rar|zip|RAR|chm))"')
bookResult = re.findall(bookPatterns, contents)
bookName = bookResult[1:]
print(re.findall(urlPatterns, contents))
urls = [url[0] for url in re.findall(urlPatterns, contents)]
df = pd.DataFrame(columns = ['Book', 'url'])
df['Book'] = bookName
df['url'] = urls
with open('results.csv', 'w', encoding = 'utf-8-sig') as csvfile:
	df.to_csv(csvfile, index = False)

