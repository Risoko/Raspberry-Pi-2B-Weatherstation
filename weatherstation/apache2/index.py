#!/usr/bin/python3
from weatherstation.apache2.settings import titles


print("Content-Type: text/html")
print()

for img in title:
    print('''<img src="{}.png">'''.format(img))


