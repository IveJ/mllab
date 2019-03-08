import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as s:
    print("pls say command: ")
    p = r.listen(s)

    try:
        word = r.recognize_google(p)
        print('U want : {}'.format(text))
    except:
        print('Unknow Ur command!')
