import pyttsx
file1=open("b.txt")
engine = pyttsx.init()
voices = engine.getProperty('voices')
rate1 = engine.getProperty('rate')
engine.setProperty('rate',120)
#print rate1
#print voices[11].gender
engine.setProperty('voice', voices[11].id)
engine.setProperty('voice', voices[2].gender)
image_text=file1.read()

print image_text
engine.say(image_text)
engine.runAndWait()
