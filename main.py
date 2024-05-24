import speech_recognition as sr   # voice recognition library
import random                     # to choose random words from list
import pyttsx3                    # offline Text to Speech
import datetime                   # to get date and time
import webbrowser                 # to open and perform web tasks
import serial                     # for serial communication
import pywhatkit                  # for more web automation

# Declare robot name (Wake-Up word)
robot_name = 'john'

# random words list
hi_words = ['hi', 'hello', 'yo', 'welcome']
bye_words = ['bye', 'see ya', 'goodbye']
r_u_there = ['are you there', 'you there']

# initialization
engine = pyttsx3.init()                    # init text to speech engine
#voices = engine.getProperty('voices')      #check for voices
#engine.setProperty('voice', voices[1].id)  # female voice
listener = sr.Recognizer()                 # initialize speech recognition API

# connect with NiNi motor driver board over serial communication
try:
    port = serial.Serial("COM3", 9600)
    print("Phycial body, connected.")
except:
    print("Unable to connect to my physical body")


def listen():
	""" listen to what user says"""
	try:
		with sr.Microphone() as source:                         # get input from mic
			print("Talk>>")
			voice = listener.listen(source)                     # listen from microphone
			command = listener.recognize_google(voice).lower()  # use google API
			# all words lowercase- so that we can process easily
			#command = command.lower()         
			print(command)

			# look for wake up word in the beginning
			if (command.split(' ')[0] == robot_name):
				# if wake up word found....
				print("[wake-up word found]")
				process(command)                 # call process funtion to take action
	except:
		pass

def process(words):
	""" process what user says and take actions """
	print(words) # check if it received any command

	# break words in
	word_list = words.split(' ')[1:]   # split by space and ignore the wake-up word

	if (len(word_list)==1):
		if (word_list[0] == robot_name):
		    talk("How Can I help you?")
		    #.write(b'l')
		    return

	if (len(word_list)==1):
		if (word_list[0] == robot_name):
		    talk("How Can I help you?")
		    #.write(b'l')
		    return

	if word_list[0] == 'play':
		"""if command for playing things, play from youtube"""
		talk("Okay boss, playing")
		extension = ' '.join(word_list[1:])                    # search without the command word
		port.write(b'u')
		pywhatkit.playonyt(extension)   
		port.write(b'l')          
		return
