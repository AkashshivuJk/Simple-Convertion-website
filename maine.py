import speech_recognition as sr
from pydub import AudioSegment
from moviepy.editor import VideoFileClip
import os





def MP3_text():
    folder_path = r'boool'
    items = os.listdir(folder_path)
    first_item = os.path.join(folder_path, items[0])


    recognizer = sr.Recognizer()
    mp3_file = first_item
    audio = AudioSegment.from_mp3(mp3_file)
    wav_file = "converted_audio.wav"
    audio.export(wav_file, format="wav")
    with sr.AudioFile(wav_file) as source:
        audio = recognizer.record(source) 
    try:
        text = recognizer.recognize_google(audio)
        print("Recognized text:", text)
        with open("data/result.txt", "w") as text_file:
            text_file.write(text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
    os.remove(first_item)

def convert_mp4_to_mp3():
    folder_path = r'boool'
    items = os.listdir(folder_path)
    first_item = os.path.join(folder_path, items[0])


    input_video = first_item
    output_audio = "data/Final_audio.mp3"  
    try:
        video_clip = VideoFileClip(input_video)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_audio, codec="mp3")
        audio_clip.close()
        video_clip.close()
        print("Conversion successful!")
    except Exception as e:
        print("Error:", e)
    os.remove(first_item)

def remove():
    folder_path = 'data'
    items = os.listdir(folder_path)
    first_item = os.path.join(folder_path, items[0])
    os.remove(first_item)
    