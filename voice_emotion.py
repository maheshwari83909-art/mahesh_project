import speech_recognition as sr
from textblob import TextBlob
import streamlit as st
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile
import os

class VoiceEmotionAnalyzer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        
    def record_audio(self, duration=5):
        """Record audio from microphone"""
        st.info(f"🎙️ Recording for {duration} seconds... Please speak clearly.")
        
        # Record audio
        sample_rate = 16000
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
        sd.wait()
        
        # Convert to int16
        recording_int16 = (recording * 32767).astype(np.int16)
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmpfile:
            wav.write(tmpfile.name, sample_rate, recording_int16)
            tmpfile_path = tmpfile.name
        
        return tmpfile_path
    
    def analyze_voice(self, audio_file_path):
        """Analyze voice for emotion through text sentiment"""
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio = self.recognizer.record(source)
                
            # Convert speech to text
            text = self.recognizer.recognize_google(audio)
            
            if text:
                # Analyze sentiment of the transcribed text
                blob = TextBlob(text)
                sentiment_score = blob.sentiment.polarity  # -1 to 1
                
                # Determine sentiment category
                if sentiment_score > 0.1:
                    sentiment = "Positive"
                    voice_score = 80 + (sentiment_score * 20)
                elif sentiment_score < -0.1:
                    sentiment = "Negative"
                    voice_score = 30 + ((sentiment_score + 1) * 30)
                else:
                    sentiment = "Neutral"
                    voice_score = 60
                
                voice_score = min(max(voice_score, 0), 100)
                
                return {
                    "text": text,
                    "sentiment": sentiment,
                    "sentiment_score": sentiment_score,
                    "voice_score": voice_score
                }
            else:
                return None
                
        except sr.UnknownValueError:
            st.warning("Could not understand audio. Please speak clearly.")
            return None
        except sr.RequestError as e:
            st.error(f"Speech recognition service error: {e}")
            return None
        except Exception as e:
            st.error(f"Error analyzing voice: {e}")
            return None
    
    def analyze_text_input(self, text):
        """Analyze text directly for sentiment"""
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        
        if sentiment_score > 0.1:
            sentiment = "Positive"
            voice_score = 80 + (sentiment_score * 20)
        elif sentiment_score < -0.1:
            sentiment = "Negative"
            voice_score = 30 + ((sentiment_score + 1) * 30)
        else:
            sentiment = "Neutral"
            voice_score = 60
        
        voice_score = min(max(voice_score, 0), 100)
        
        return {
            "text": text,
            "sentiment": sentiment,
            "sentiment_score": sentiment_score,
            "voice_score": voice_score
        }