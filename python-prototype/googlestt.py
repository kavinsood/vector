from google.cloud import speech
import pyaudio
import pyttsx3
import sort

# Set up Text-to-Speech engine
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_recognition_continuous():
    client = speech.SpeechClient()

    # Set up microphone input
    RATE = 16000
    CHUNK = int(RATE / 10)  # 100ms

    def listen():
        """Generates audio chunks from the microphone."""
        with pyaudio.PyAudio() as p:
            stream = p.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)
            while True:
                yield stream.read(CHUNK)

    # Set up streaming recognition config
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code="en-US"
    )
    streaming_config = speech.StreamingRecognitionConfig(config=config, interim_results=False)

    # Callback to process responses from Google Cloud
    def process_responses(responses):
        for response in responses:
            if not response.results:
                continue
            result = response.results[0]
            if not result.alternatives:
                continue

            # Recognized text from the microphone
            command = result.alternatives[0].transcript
            print(command)
            command = command.lower()
            sort.reply(command)

    print("Listening for speech. Press Ctrl+C to stop.")

    # Perform the continuous streaming recognition
    with client.streaming_recognize(streaming_config, listen()) as responses:
        try:
            process_responses(responses)
        except KeyboardInterrupt:
            print("Stopping...")

if __name__ == "__main__":
    speech_recognition_continuous()
