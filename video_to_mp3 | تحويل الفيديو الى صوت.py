# pip install moviepy
# إضافة المكتبه اللازمة وإختصارها
import moviepy.editor as mp
# تحديد ملف الفيديو
video = mp.VideoFileClip(r"test.mp4")
# تحويل الفيديو الى ملف صوتي وحفظه
video.audio.write_audiofile(r"test.mp3")
