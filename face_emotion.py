import cv2
from deepface import DeepFace
import streamlit as st
from PIL import Image
import numpy as np

class FaceEmotionAnalyzer:
    def __init__(self):
        self.emotions = ["Happy", "Sad", "Neutral", "Angry", "Fear", "Disgust", "Surprise"]
        
    def analyze_webcam(self):
        """Analyze face emotion using webcam"""
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            st.error("Cannot access webcam. Please check your camera.")
            return None
        
        # Placeholder for displaying frames
        frame_placeholder = st.empty()
        emotion_placeholder = st.empty()
        
        ret, frame = cap.read()
        
        if ret:
            # Convert BGR to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Display frame
            frame_placeholder.image(rgb_frame, caption="Live Webcam Feed", use_column_width=True)
            
            # Analyze emotion
            try:
                result = DeepFace.analyze(rgb_frame, actions=['emotion'], enforce_detection=False)
                
                if result:
                    dominant_emotion = result[0]['dominant_emotion']
                    emotion_scores = result[0]['emotion']
                    
                    # Map to our emotion categories
                    emotion_map = {
                        'happy': 'Happy',
                        'sad': 'Sad',
                        'neutral': 'Neutral',
                        'angry': 'Angry',
                        'fear': 'Fear',
                        'disgust': 'Disgust',
                        'surprise': 'Surprise'
                    }
                    
                    mapped_emotion = emotion_map.get(dominant_emotion.lower(), dominant_emotion)
                    
                    # Calculate face score (based on happiness - higher is better)
                    if mapped_emotion == 'Happy':
                        face_score = 90
                    elif mapped_emotion == 'Neutral':
                        face_score = 60
                    elif mapped_emotion == 'Surprise':
                        face_score = 50
                    else:
                        face_score = 30
                    
                    emotion_placeholder.info(f"**Detected Emotion:** {mapped_emotion} 😊" if mapped_emotion == 'Happy' else f"**Detected Emotion:** {mapped_emotion}")
                    
                    cap.release()
                    cv2.destroyAllWindows()
                    return mapped_emotion, face_score
                    
            except Exception as e:
                st.warning(f"Face detection error: {str(e)}")
                cap.release()
                return "Neutral", 60
        
        cap.release()
        cv2.destroyAllWindows()
        return "Neutral", 60
    
    def analyze_image(self, uploaded_image):
        """Analyze face emotion from uploaded image"""
        try:
            # Convert PIL Image to numpy array
            image = np.array(uploaded_image)
            
            # Analyze emotion
            result = DeepFace.analyze(image, actions=['emotion'], enforce_detection=False)
            
            if result:
                dominant_emotion = result[0]['dominant_emotion']
                
                emotion_map = {
                    'happy': 'Happy',
                    'sad': 'Sad',
                    'neutral': 'Neutral',
                    'angry': 'Angry',
                    'fear': 'Fear',
                    'disgust': 'Disgust',
                    'surprise': 'Surprise'
                }
                
                mapped_emotion = emotion_map.get(dominant_emotion.lower(), dominant_emotion)
                
                # Calculate face score
                if mapped_emotion == 'Happy':
                    face_score = 90
                elif mapped_emotion == 'Neutral':
                    face_score = 60
                elif mapped_emotion == 'Surprise':
                    face_score = 50
                else:
                    face_score = 30
                
                return mapped_emotion, face_score
                
        except Exception as e:
            st.error(f"Error analyzing image: {str(e)}")
            return "Neutral", 60