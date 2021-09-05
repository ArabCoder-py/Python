# pip install fpdf لتثبيت المكتبة
# نضيق المكتبة
from fpdf import FPDF
import os
# إنشاء ملف pdf جديد
pdf = FPDF()
# لوضع كل صورة في صفحة جديدة
pdf.set_auto_page_break(0)
img_list = []
# imgs هو الملف الذي يحتوي على الصور
images = [x for x in os.listdir('imgs')]
for i in images:
    i = "imgs/" + i
    img_list.append(i)
# لوضع الصور في الملف
for img in img_list:
    pdf.add_page()
    pdf.image(img)
# حفظ ملف ال pdf
pdf.output("Images.pdf")
