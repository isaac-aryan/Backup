import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
	print("Talk now.")

	audio=r.listen(source)

	try:
		text=r.recognize_google(audio)
		print("You just said: ",str(text))
	except:
		print("I did not understand what you spoke.")