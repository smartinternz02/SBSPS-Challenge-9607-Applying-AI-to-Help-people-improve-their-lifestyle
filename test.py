import pyttsx3

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()
voice = engine.getProperty('voices') #get the available voices

engine.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice
engine. setProperty("rate", 150)
# say method on the engine that passing input text to be spoken
def say(st):
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    
    engine.say(str(st))
    print(st+"Said ")
    engine.runAndWait()

say(''*4)