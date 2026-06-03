import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from PIL import Image

# Import modules
from database import *
from face_emotion import FaceEmotionAnalyzer
from voice_emotion import VoiceEmotionAnalyzer
from text_sentiment import TextSentimentAnalyzer
from risk_engine import RiskEngine

# Page configuration
st.set_page_config(
    page_title="AI Employee Retention Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
init_database()

# Initialize analyzers
face_analyzer = FaceEmotionAnalyzer()
voice_analyzer = VoiceEmotionAnalyzer()
text_analyzer = TextSentimentAnalyzer()
risk_engine = RiskEngine()

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .risk-high {
        background-color: #ffebee;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #f44336;
    }
    .risk-medium {
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #ff9800;
    }
    .risk-low {
        background-color: #e8f5e9;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #4caf50;
    }
    .metric-card {
        background-color: #f5f5f5;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'current_employee_id' not in st.session_state:
    st.session_state.current_employee_id = None
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False

# Sidebar navigation
st.sidebar.image("https://www.vdart.com/wp-content/uploads/2021/02/Image20210206041010-1024x518.png", width=100)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["🏠 Employee Dashboard", "📊 HR Dashboard", "👥 Employee Management", "📈 Analytics"])

# Employee Management Page
if page == "👥 Employee Management":
    st.markdown("<div class='main-header'>👥 Employee Management</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("➕ Add New Employee")
        with st.form("add_employee_form"):
            name = st.text_input("Full Name")
            department = st.selectbox("Department", ["Engineering", "Sales", "Marketing", "HR", "Product", "Operations"])
            joining_date = st.date_input("Joining Date", datetime.now())
            email = st.text_input("Email")
            
            submitted = st.form_submit_button("Add Employee")
            if submitted and name and email:
                employee_id = add_employee(name, department, joining_date.strftime("%Y-%m-%d"), email)
                st.success(f"✅ Employee {name} added successfully! ID: {employee_id}")
    
    with col2:
        st.subheader("📋 Current Employees")
        employees = get_employees()
        if employees:
            emp_df = pd.DataFrame(employees, columns=["ID", "Name", "Department", "Joining Date", "Email"])
            st.dataframe(emp_df, use_container_width=True)
            
            # Select employee for analysis
            st.subheader("🔍 Select Employee for Analysis")
            selected_emp = st.selectbox("Choose Employee", employees, format_func=lambda x: f"{x[1]} ({x[2]})")
            if selected_emp:
                st.session_state.current_employee_id = selected_emp[0]
                st.success(f"Selected: {selected_emp[1]}")
        else:
            st.info("No employees added yet. Please add employees first.")

# Employee Dashboard
elif page == "🏠 Employee Dashboard":
    st.markdown("<div class='main-header'>🏠 Employee Well-being Dashboard</div>", unsafe_allow_html=True)
    
    if st.session_state.current_employee_id is None:
        st.warning("⚠️ Please go to 'Employee Management' and select an employee first!")
        st.stop()
    
    employee = get_employee_by_id(st.session_state.current_employee_id)
    if employee:
        st.success(f"Welcome, {employee[1]}! 👋")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 😊 Face Emotion Check")
            if st.button("🎥 Start Face Analysis", use_container_width=True):
                with st.spinner("Analyzing face emotion..."):
                    emotion, face_score = face_analyzer.analyze_webcam()
                    st.session_state.face_emotion = emotion
                    st.session_state.face_score = face_score
                    st.success(f"Emotion: {emotion}")
        
        with col2:
            st.markdown("### 🎙️ Voice Check-in")
            voice_method = st.radio("Choose method", ["Record Voice", "Type Text"], horizontal=True)
            
            if voice_method == "Record Voice":
                if st.button("🎤 Start Recording", use_container_width=True):
                    with st.spinner("Recording and analyzing..."):
                        audio_file = voice_analyzer.record_audio(duration=5)
                        result = voice_analyzer.analyze_voice(audio_file)
                        if result:
                            st.session_state.voice_sentiment = result['sentiment']
                            st.session_state.voice_score = result['voice_score']
                            st.session_state.voice_text = result['text']
                            st.success(f"Sentiment: {result['sentiment']}")
                            st.info(f"Transcribed: {result['text']}")
            else:
                text_input = st.text_area("How are you feeling today?")
                if st.button("Analyze Text", use_container_width=True) and text_input:
                    result = voice_analyzer.analyze_text_input(text_input)
                    st.session_state.voice_sentiment = result['sentiment']
                    st.session_state.voice_score = result['voice_score']
                    st.session_state.voice_text = result['text']
                    st.success(f"Sentiment: {result['sentiment']}")
        
        with col3:
            st.markdown("### 📝 Daily Feedback")
            feedback_text = st.text_area("Share your feedback or concerns")
            if st.button("Submit Feedback", use_container_width=True) and feedback_text:
                result = text_analyzer.analyze_feedback(feedback_text)
                st.session_state.text_sentiment = result['sentiment']
                st.session_state.text_score = result['text_score']
                st.session_state.stress_level = result['stress_level']
                st.session_state.resign_risk = result['resign_risk']
                st.session_state.adaptation_issue = result['adaptation_issue']
                
                # Save feedback to database
                save_feedback(st.session_state.current_employee_id, feedback_text, 
                             result['sentiment'], result['sentiment_score'], result['stress_level'])
                
                st.success(f"Sentiment: {result['sentiment']} | Stress Level: {result['stress_level']}")
        
        # Risk Analysis Section
        st.markdown("---")
        st.subheader("📊 Risk Analysis & Recommendations")
        
        if st.button("🚀 Generate Complete Analysis", use_container_width=True, type="primary"):
            if all(k in st.session_state for k in ['face_score', 'voice_score', 'text_score']):
                
                # Calculate adaptability score
                adaptability = risk_engine.calculate_adaptability_score(
                    st.session_state.face_score,
                    st.session_state.voice_score,
                    st.session_state.text_score,
                    attendance_score=85  # Default attendance score
                )
                
                # Predict retention risk
                risk_level, risk_score, recommendations = risk_engine.predict_retention_risk(
                    st.session_state.get('face_emotion', 'Neutral'),
                    st.session_state.get('voice_sentiment', 'Neutral'),
                    st.session_state.get('text_sentiment', 'Neutral'),
                    st.session_state.get('stress_level', 'Low'),
                    st.session_state.get('resign_risk', False),
                    st.session_state.get('adaptation_issue', False),
                    adaptability
                )
                
                # Save to database
                save_emotion_log(
                    st.session_state.current_employee_id,
                    st.session_state.get('face_emotion', 'Neutral'),
                    st.session_state.face_score,
                    st.session_state.voice_score,
                    st.session_state.text_score,
                    adaptability,
                    risk_level
                )
                
                # Save recommendations
                for rec in recommendations[:3]:  # Top 3 recommendations
                    save_recommendation(st.session_state.current_employee_id, rec, risk_level)
                
                # Display results
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Adaptability Score", f"{adaptability}/100", 
                             delta="Good" if adaptability > 70 else "Needs Improvement" if adaptability > 40 else "Critical")
                
                with col2:
                    st.metric("Retention Risk", risk_level, 
                             delta=f"Risk Score: {risk_score}%")
                
                with col3:
                    st.metric("Overall Assessment", 
                             "Stable" if risk_level == "Low" else "Monitor" if risk_level == "Medium" else "Immediate Action")
                
                # Recommendations
                st.subheader("💡 AI Recommendations")
                risk_class = "risk-high" if risk_level == "High" else "risk-medium" if risk_level == "Medium" else "risk-low"
                st.markdown(f"<div class='{risk_class}'>", unsafe_allow_html=True)
                for rec in recommendations:
                    st.write(f"• {rec}")
                st.markdown("</div>", unsafe_allow_html=True)
                
                # HR Alert
                alert = risk_engine.generate_hr_alert(risk_level, employee[1])
                if risk_level == "High":
                    st.error(alert)
                elif risk_level == "Medium":
                    st.warning(alert)
                else:
                    st.success(alert)
                
                st.session_state.analysis_complete = True
            else:
                st.warning("Please complete all three analyses first (Face, Voice, and Feedback)!")
        
        # Display previous analyses
        st.subheader("📜 Previous Analyses")
        emotion_history, feedback_history, recommendations = get_employee_analytics(st.session_state.current_employee_id)
        
        if emotion_history:
            df_history = pd.DataFrame(emotion_history, columns=["Timestamp", "Emotion", "Adaptability", "Risk"])
            st.dataframe(df_history, use_container_width=True)

# HR Dashboard
elif page == "📊 HR Dashboard":
    st.markdown("<div class='main-header'>📊 HR Analytics Dashboard</div>", unsafe_allow_html=True)
    
    employees = get_employees()
    if not employees:
        st.info("No employee data available. Please add employees and run analyses.")
        st.stop()
    
    # Get analytics
    latest_status, risk_distribution = get_all_employees_analytics()
    
    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Employees", len(employees))
    
    high_risk = sum(1 for emp in latest_status if emp[5] == "High")
    medium_risk = sum(1 for emp in latest_status if emp[5] == "Medium")
    low_risk = sum(1 for emp in latest_status if emp[5] == "Low")
    
    with col2:
        st.metric("High Risk", high_risk, delta="Needs Attention" if high_risk > 0 else "Good")
    
    with col3:
        st.metric("Medium Risk", medium_risk)
    
    with col4:
        st.metric("Low Risk", low_risk)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Risk Distribution")
        risk_df = pd.DataFrame(list(risk_distribution), columns=["Risk Level", "Count"])
        if not risk_df.empty:
            fig = px.pie(risk_df, values="Count", names="Risk Level", 
                        color="Risk Level", color_discrete_map={"High": "#f44336", "Medium": "#ff9800", "Low": "#4caf50"})
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Employee Status Overview")
        status_df = pd.DataFrame(latest_status, columns=["ID", "Name", "Department", "Emotion", "Adaptability", "Risk", "Last Update"])
        fig = px.bar(status_df, x="Name", y="Adaptability", color="Risk", 
                    title="Adaptability Score by Employee")
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed Employee Table
    st.subheader("Employee Details")
    display_df = status_df[["Name", "Department", "Emotion", "Adaptability", "Risk"]].copy()
    st.dataframe(display_df, use_container_width=True)
    
    # High Risk Employees Section
    st.subheader("🚨 High Risk Employees - Immediate Attention Required")
    high_risk_employees = status_df[status_df["Risk"] == "High"]
    if not high_risk_employees.empty:
        for _, emp in high_risk_employees.iterrows():
            with st.expander(f"⚠️ {emp['Name']} - {emp['Department']}"):
                st.write(f"**Current Emotion:** {emp['Emotion']}")
                st.write(f"**Adaptability Score:** {emp['Adaptability']}/100")
                st.write(f"**Risk Level:** {emp['Risk']}")
                
                # Get recommendations for this employee
                _, _, recommendations = get_employee_analytics(emp['ID'])
                if recommendations:
                    st.write("**Pending Recommendations:**")
                    for rec in recommendations[:3]:
                        st.write(f"• {rec[0]}")
                
                if st.button(f"Send Alert to {emp['Name']}", key=f"alert_{emp['ID']}"):
                    st.success(f"Alert sent to HR team for {emp['Name']}")
    else:
        st.info("No high-risk employees at the moment. Keep up the good work! 🎉")

# Analytics Page
elif page == "📈 Analytics":
    st.markdown("<div class='main-header'>📈 Advanced Analytics</div>", unsafe_allow_html=True)
    
    conn = sqlite3.connect(DB_PATH)
    
    # Emotion Trends
    st.subheader("Emotion Trends Over Time")
    query = """
        SELECT DATE(timestamp) as date, emotion, COUNT(*) as count
        FROM emotion_logs
        GROUP BY DATE(timestamp), emotion
        ORDER BY date DESC
        LIMIT 30
    """
    trend_df = pd.read_sql_query(query, conn)
    if not trend_df.empty:
        fig = px.line(trend_df, x="date", y="count", color="emotion", 
                     title="Emotion Distribution Trends")
        st.plotly_chart(fig, use_container_width=True)
    
    # Adaptability Distribution
    st.subheader("Adaptability Score Distribution")
    query = """
        SELECT adaptability_score, retention_risk
        FROM emotion_logs
        WHERE timestamp = (SELECT MAX(timestamp) FROM emotion_logs)
    """
    adapt_df = pd.read_sql_query(query, conn)
    if not adapt_df.empty:
        fig = px.histogram(adapt_df, x="adaptability_score", color="retention_risk",
                          nbins=20, title="Adaptability Score Distribution by Risk Level")
        st.plotly_chart(fig, use_container_width=True)
    
    # Department-wise Analysis
    st.subheader("Department-wise Analysis")
    query = """
        SELECT e.department, 
               AVG(el.adaptability_score) as avg_adaptability,
               COUNT(CASE WHEN el.retention_risk = 'High' THEN 1 END) as high_risk_count
        FROM employees e
        LEFT JOIN emotion_logs el ON e.id = el.employee_id
        WHERE el.timestamp = (SELECT MAX(timestamp) FROM emotion_logs)
        GROUP BY e.department
    """
    dept_df = pd.read_sql_query(query, conn)
    if not dept_df.empty:
        fig = px.bar(dept_df, x="department", y="avg_adaptability", 
                    color="high_risk_count", title="Average Adaptability by Department")
        st.plotly_chart(fig, use_container_width=True)
    
    conn.close()

# Footer
st.sidebar.markdown("---")
st.sidebar.info(
    """
    **AI Employee Retention Platform v1.0**
    
    Multimodal AI for:
    - Face Emotion Recognition
    - Voice Sentiment Analysis  
    - Text Feedback Analysis
    - Retention Risk Prediction
    """
)

# Run the app
if __name__ == "__main__":
    pass