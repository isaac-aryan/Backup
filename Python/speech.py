import speech_recognition as sr
import webbrowser as wb

r=sr.Recognizer()

with sr.Microphone() as source:
	print("Choose between Google and Youtube.\nTalk now.")

	audio=r.listen(source)

	try:
		text=r.recognize_google(audio)
		text=text.lower()
		print("You said: ",str(text))

		
	except:
		print("I did not understand what you spoke.")

	if 'google' in text:
		url='https://www.google.com/search?q='

		with sr.Microphone() as source:
			print("What do you want to search in Google?")

			audio=r.listen(source)

			try:
				text=r.recognize_google(audio)
				print("You are trying to search: ",text)
				query=url+text
				wb.get().open_new(query)
			except:
				print("Could not open page.")

	elif 'youtube' in text:
		url='https://www.youtube.com/results?search_query='

		with sr.Microphone() as source:
			print("What do you want to search in YouTube?")

			audio=r.listen(source)

			try:
				text=r.recognize_google(audio)
				print("You are trying to search ",text," in YouTube.")
				query=url+text
				wb.get().open_new(query)
			except:
				print("Could not open page.")

	else:
		print("Not a valid option")


		

		

		