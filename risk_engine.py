class RiskEngine:
    def __init__(self):
        pass
    
    def calculate_adaptability_score(self, face_score, voice_score, text_score, attendance_score=85):
        """Calculate overall adaptability score"""
        # Weighted average: Face 30%, Voice 30%, Text 30%, Attendance 10%
        adaptability = (face_score * 0.3) + (voice_score * 0.3) + (text_score * 0.3) + (attendance_score * 0.1)
        return round(adaptability, 2)
    
    def predict_retention_risk(self, face_emotion, voice_sentiment, text_sentiment, 
                               stress_level, resign_risk, adaptation_issue, adaptability_score):
        """Predict retention risk based on multiple factors"""
        
        risk_score = 0
        
        # Face emotion contribution
        if face_emotion in ['Sad', 'Angry', 'Fear']:
            risk_score += 30
        elif face_emotion == 'Neutral':
            risk_score += 15
        
        # Voice sentiment contribution
        if voice_sentiment == 'Negative':
            risk_score += 30
        elif voice_sentiment == 'Neutral':
            risk_score += 15
        
        # Text sentiment contribution
        if text_sentiment == 'Negative':
            risk_score += 30
        elif text_sentiment == 'Neutral':
            risk_score += 15
        
        # Stress level contribution
        if stress_level == 'Very High':
            risk_score += 20
        elif stress_level == 'High':
            risk_score += 15
        elif stress_level == 'Medium':
            risk_score += 8
        
        # Resign risk contribution
        if resign_risk:
            risk_score += 30
        
        # Adaptation issue contribution
        if adaptation_issue:
            risk_score += 15
        
        # Adaptability score contribution (lower adaptability = higher risk)
        if adaptability_score < 40:
            risk_score += 25
        elif adaptability_score < 60:
            risk_score += 15
        elif adaptability_score < 75:
            risk_score += 8
        
        # Determine risk level
        if risk_score >= 70:
            risk_level = "High"
            recommendation = self.get_high_risk_recommendations()
        elif risk_score >= 40:
            risk_level = "Medium"
            recommendation = self.get_medium_risk_recommendations()
        else:
            risk_level = "Low"
            recommendation = self.get_low_risk_recommendations()
        
        return risk_level, min(risk_score, 100), recommendation
    
    def get_high_risk_recommendations(self):
        """Get recommendations for high risk employees"""
        return [
            "🚨 Schedule immediate HR meeting within 48 hours",
            "👥 Assign a dedicated mentor for onboarding support",
            "📉 Reduce current workload and adjust deadlines",
            "💆‍♂️ Recommend wellness program and mental health support",
            "🗣️ Conduct one-on-one feedback session to understand concerns",
            "📅 Review and adjust onboarding plan for next 30 days"
        ]
    
    def get_medium_risk_recommendations(self):
        """Get recommendations for medium risk employees"""
        return [
            "📅 Schedule weekly check-in meeting",
            "🤝 Encourage team collaboration and peer support",
            "📚 Provide additional training resources",
            "🎯 Set clear short-term goals and milestones",
            "💬 Regular feedback collection and addressing concerns"
        ]
    
    def get_low_risk_recommendations(self):
        """Get recommendations for low risk employees"""
        return [
            "✅ Continue current support structure",
            "🎉 Recognize and appreciate good work",
            "📈 Provide growth and development opportunities",
            "🤗 Maintain regular check-ins for continuous engagement",
            "🏆 Encourage participation in team activities"
        ]
    
    def generate_hr_alert(self, risk_level, employee_name):
        """Generate HR alert based on risk level"""
        if risk_level == "High":
            return f"⚠️ CRITICAL: {employee_name} is at HIGH retention risk. Immediate intervention required!"
        elif risk_level == "Medium":
            return f"📌 ALERT: {employee_name} shows MEDIUM retention risk. Schedule follow-up meeting."
        else:
            return f"✅ {employee_name} is at LOW retention risk. Continue regular monitoring."