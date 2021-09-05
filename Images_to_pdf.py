# pip install fpdf لتثبيت المكتبة
# نضيف المكتبة
from fpdf import FPDF
import os
# جديد pdf إنشاء ملف
pdf = FPDF()
# لوضع كل صورة في صفحة جديدة
pdf.set_auto_page_break(0)
img_list = []
# هو الملف الذي يحتوي على الصور imgs 
images = [x for x in os.listdir('imgs')]
for i in images:
    i = "imgs/" + i
    img_list.append(i)
# لوضع الصور في الملف
for img in img_list:
    pdf.add_page()
    pdf.image(img)
# pdf حفظ ملف ال
pdf.output("Images.pdf")
