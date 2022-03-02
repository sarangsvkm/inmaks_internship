from gtts import gTTS
import os
text=open('deno.txt','r',encoding='utf-8').read()
language='hi'
output=gTTS(text=text,lang=language,slow=False)
output.save('fileout.mp4')
os.system('start fileout.mp4')