# cmd تثبيت المكتبة من ال
# pip install pyautogui
# إذا لم تعمل المكتبة الرئيسية مباشرة, قم بتثبيت هذه المكتبة الإضافية
# pip install pillow
# إضافة المكتبة اللازمة
import pyautogui
# لأخذ لقطة الشاشة
image = pyautogui.screenshot()
# لحفظ لقطة الشاشة
image.save("ScreenShot.jpg")
