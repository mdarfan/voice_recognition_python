from gtts import gTTS
import pyglet
import time ,os
def tts(text,lang):
    file =gTTS(text =text, lang =lang)
    filename ='temp.mp3'
    file.save(filename)
    print "happening"
    player = pyglet.media.Player()
    music =pyglet.media.load(filename)
    music.play()
    pyglet.app.run()
    time.sleep(music.duration)
    os.remove(filename)
##    player.queue(music)
##    player.play()
##    pyglet.app.run()
