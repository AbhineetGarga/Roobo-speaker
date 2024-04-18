  ####these code os for mac user####
# import os
#
#
# if __name__ == '__main__':
#     print("Welcome to Robo Speaker! 1.1 created by Abhineet")
#
#     while True:
#         x = input("Enter a Cammand: ")
#         if x == '1':
#             break
#         command= f"say {x}"
#         os.system(command)


# import winsound
#
# if __name__ == '__main__':
#     print("Welcome to Robo Speaker! 1.1 created by Abhineet")
#     x = input("Enter a Command: ")
#
#     # Replace say command with winsound library for Windows compatibility
#     winsound.Speak(x)


#First install gtts
from gtts import gTTS
from playsound import playsound

language = "en"

while True:
    text = input("Enter some text (type '1' to exit): ")

    if text == "1":
        break

    speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
    speech.save("textToSpeech.mp3")
    playsound("textToSpeech.mp3")
