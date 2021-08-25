# إضافة المكتبة اللازمة
import pyqrcode

# إنشاء متغير يحتوي على الرابط المطلوب
link = "https://www.instagram.com/arabcoder.py/"

# QRنقوم بإنشاء رمز ال
QR_Code = pyqrcode.create(link)

# نختار حجم الرمز ونقوم بحفظه
QR_Code.png('test.png', scale=8,  module_color=(0x66, 0x33, 0x0),  # Dark brown
            background=(0xff, 0xff, 0xff, 0))  # 50% transparent white)
