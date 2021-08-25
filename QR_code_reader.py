# إضافة المكاتب اللازمة
from PIL import Image
from pyzbar import pyzbar
import re
# نقوم بتحديد مسار الصورة
img = Image.open('test.png')
# String هذا الأمر لفك تشفير الرمز وتحويل المعطيات إلى
output = str(pyzbar.decode(img)[0])
# نقوم بالبحث بين النتائج عن اي رابط
url = re.findall(
    'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|)+', output)
print(url)
