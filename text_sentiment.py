from textblob import TextBlob
import re

class TextSentimentAnalyzer:
    def __init__(self):
        self.stress_keywords = [
            'stressed', 'overwhelmed', 'burnout', 'tired', 'exhausted',
            'pressure', 'anxious', 'worried', 'unhappy', 'frustrated',
            'difficult', 'hard', 'struggling', 'suffering'
        ]
        
    def analyze_feedback(self, feedback_text):
        """Analyze employee feedback for sentiment and stress"""
        
        # Sentiment analysis
        blob = TextBlob(feedback_text)
        sentiment_score = blob.sentiment.polarity  # -1 to 1
        subjectivity = blob.sentiment.subjectivity  # 0 to 1
        
        # Determine sentiment category
        if sentiment_score > 0.2:
            sentiment = "Positive"
            text_score = 80 + (sentiment_score * 20)
        elif sentiment_score < -0.1:
            sentiment = "Negative"
            text_score = 30 + ((sentiment_score + 1) * 30)
        else:
            sentiment = "Neutral"
            text_score = 60
        
        # Stress detection
        text_lower = feedback_text.lower()
        stress_count = sum(1 for keyword in self.stress_keywords if keyword in text_lower)
        
        if stress_count >= 3:
            stress_level = "Very High"
            text_score = max(text_score - 30, 10)
        elif stress_count >= 2:
            stress_level = "High"
            text_score = max(text_score - 20, 20)
        elif stress_count == 1:
            stress_level = "Medium"
            text_score = max(text_score - 10, 35)
        else:
            stress_level = "Low"
        
        # Check for resignation indicators
        resignation_indicators = [
            'resign', 'quit', 'leave', 'new job', 'looking for', 'opportunity',
            'notice period', 'career change', 'move on'
        ]
        
        resign_risk = any(indicator in text_lower for indicator in resignation_indicators)
        
        # Check for adaptation issues
        adaptation_indicators = [
            'difficult to adapt', 'hard to learn', 'not fitting', 'culture',
            'team not supportive', 'training needed', 'unclear role'
        ]
        
        adaptation_issue = any(indicator in text_lower for indicator in adaptation_indicators)
        
        text_score = min(max(text_score, 0), 100)
        
        return {
            "sentiment": sentiment,
            "sentiment_score": sentiment_score,
            "subjectivity": subjectivity,
            "stress_level": stress_level,
            "resign_risk": resign_risk,
            "adaptation_issue": adaptation_issue,
            "text_score": text_score
        }