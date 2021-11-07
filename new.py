import re

start=re.compile(r'\d+$')
test= start.search("120 119")
print(test)
