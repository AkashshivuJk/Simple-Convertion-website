import os
import sys
import moviepy.editor as mp
import speech_recognition as sr
from google.cloud import translate_v2 as translate
from gtts import gTTS
import langid
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, AudioFileClip
import numpy as np

def convert_audio_to_text(audio_path):

    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    return text
def translate_text(input_text, target_language, credentials_path):
      os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
      client = translate.Client()
      translation = client.translate(input_text, target_language=target_language)
      return translation['translatedText']
def convert_text_to_speech(file_path):

    with open(file_path, 'r') as file:
        text = file.read()


    language = langid.classify(text)[0]


    tts = gTTS(text, lang=language)


    audio_path = os.path.splitext(file_path)[0] + '.mp3'
    tts.save(audio_path)

    print("Audio file generated successfully.")
def add_audio_overlay(background_file, overlay_file, output_file):

    background_audio = AudioSegment.from_file(background_file)


    overlay_audio = AudioSegment.from_file(overlay_file)


    combined_audio = background_audio.overlay(overlay_audio)


    combined_audio.export(output_file, format="wav")

    print("Audio overlay completed successfully.")
def combine_audio_video(audio_file, video_file, output_file):




    audio = AudioFileClip(audio_file)


    video = VideoFileClip(video_file)


    video_with_audio = video.set_audio(audio)


    video_with_audio.write_videofile(output_file, codec="libx264", audio_codec="aac")

    print("Audio and video combined successfully.")