import azure.cognitiveservices.speech as speechsdk
import time
import pyttsx3
import sort
import sys

azure_speech_key = 'API_KEY'
azure_region = 'centralindia'
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_recognition_continuous():
    speech_config = speechsdk.SpeechConfig(subscription=azure_speech_key, region=azure_region)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    def recognized(evt):
        if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            command = evt.result.text
            print(command)
            command = str.lower(command)
            sort.reply(command)
            speech_recognizer.stop_continuous_recognition()
            sys.exit()

        elif evt.result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized")
        elif evt.result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = evt.result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))

    speech_recognizer.recognized.connect(recognized)
    print("Listening for speech. Press Ctrl+C to stop.")
    speech_recognizer.start_continuous_recognition()
    
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt: 
        print("Stopping...")
        speech_recognizer.stop_continuous_recognition()

if __name__ == "__main__":
    speech_recognition_continuous()
