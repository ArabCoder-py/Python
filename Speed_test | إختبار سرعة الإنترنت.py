# cdm تثبيت المكاتب المستخدمة في ال
# pip install speedtest
# pip install speedtest_cli
# إضافة المكتبة المستخدمة
import speedtest
# نظام إختيارات بسيط
option = int(input('''Chose an optio:
                    1) Download Speed 
                    2) Upload Speed
                    Your Choice: '''))
# الختيار الأول لمعرفة سرعة التنزيل
if option == 1:
    sp = speedtest.Speedtest().download()
# الخيار الثاني  لسرعة التحميل(الرفع)
elif option == 2:
    sp = speedtest.Speedtest().upload()
# تحويل النتيجة إلى صيغة مقروءة (ميغا بِت)
roundedspeed = round(sp)
finalspeed = roundedspeed / 1e+6
# طباعة النتيجة
print(finalspeed)
