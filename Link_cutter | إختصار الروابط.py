# cmd تثبيت المكتبة من ال
# pip install pyshorteners
# إضافة المكتبة اللازمة
import pyshorteners
# نضع الرابط الذي نريد إختصاره
url = input("Link")
# نقوم لإختصار الروابط
ShLink = pyshorteners.Shortener().tinyurl.short(url)
# نطبع الرابط المختصر
print(ShLink)
