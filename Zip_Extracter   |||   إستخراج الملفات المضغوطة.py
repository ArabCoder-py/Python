# نقوم بإضافة المكتبة المطلوبة
from zipfile import ZipFile
# تحديد مسار الملف الذي نريد استخراجه
path1 = r"C:\Users\talal\Desktop\test.zip"
# استخدام المكتبة لاستخراج الملف
with ZipFile(path1, 'r')as zip:
    zip.extractall()

    # لاستخراج ملف محدد
    zip.extract(member="Name.jpg",
                path=None, pwd=None)
    # pwd إذا كان للملف كلمة مرور نضعها في خانة
    # member نضع اسم الملف في خانة
