#Chatbot in Python
#using fuzzywuzzy

#this FIRST attempt will try to implement Q&A
#by means of matching list element and key in dict

inputList=["Hello", "Hi", "What's up?","How are you doing?","What you up to?",
			"What are you doing?","How's it going?","What's your name?","How old are you?",
			"What's your age?","Where are you from?", "Goodbye","Bye bye","See you later"]
			
outputDict={"Hello":["Hi there", "Hi"],
			"Hi":["Hello", "Hi", "What's up?"],
			"What's up?":["Chilling out bro", "Here ready to chat"],
			"What you up to?":["Chillig out","Just relaxing"],
			"What are you doing?":["I was sleeping","I just woke up"],
			"How's it going?":["So far so good","Everything's fine, if you know what I mean..."],
			"What's your name?":["I have no name yet :)","I'm chatBotX"],
			"How old are you?":["Don't know","I was born june 29th 2019, do the math :)"],
			"What's your age?":["Don't know","I was born june 29th 2019, do the math :)"],
			"Where are you from?":["I'm from Argentina"],
			"Goodbye":["See ya","Bye, hope to see you soon"],
			"Bye bye":["See you later","Adios amigo"],
			"See you later":["'til next time","Nice talking to you"]}


