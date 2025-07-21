import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import numpy as np
from io import StringIO 

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Dashboard", 
    layout="wide"
)

# --- STYLES ---
st.markdown("""
    <style>
        .company-header {
            font-size: 28px;
            font-weight: 700;
            color: #2B2D42;
            margin-bottom: 5px;
        }
        .dashboard-title {
            font-size: 36px;
            font-weight: 800;
            background: linear-gradient(to right, #4361ee, #3a0ca3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0;
        }
        .metric-card {
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin-bottom: 20px;
            border-left: 4px solid #4361ee;
        }
        .metric-value {
            font-size: 32px;
            font-weight: 700;
            color: #4361ee;
        }
        .metric-label {
            font-size: 14px;
            color: #666;
            margin-top: 5px;
        }
        .positive { color: #4CAF50 !important; }
        .negative { color: #F44336 !important; }
        .neutral { color: #FFC107 !important; }
    </style>
""", unsafe_allow_html=True)

data = """ticket_id,feature,message,sentiment,timestamp
1,login,"I can't log in even after resetting the password!",negative,2025-07-19 08:23:00
2,delivery,"My order arrived early, great service!",positive,2025-07-19 09:45:00
3,payment,"The payment gateway crashed again!",negative,2025-07-18 18:12:00
[...rest of your CSV data...]"""

@st.cache_data
def load_data():
    # Using StringIO from io module instead of pandas.compat
    df = pd.read_csv(StringIO(data))  
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    df['hour'] = df['timestamp'].dt.hour
    df['day_name'] = df['timestamp'].dt.day_name()
    return df
df = load_data()

# --- DASHBOARD HEADER ---
st.markdown('<p class="company-header">XYZ Cloths Co.</p>', unsafe_allow_html=True)
st.markdown('<p class="dashboard-title">Customer Sentiment Dashboard</p>', unsafe_allow_html=True)

# --- TOP METRICS ROW ---
col1, col2, col3, col4 = st.columns(4)
sentiment_counts = df['sentiment'].value_counts()

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{len(df)}</div>
            <div class="metric-label">Total Tickets</div>
        </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{sentiment_counts.get('positive', 0)}</div>
            <div class="metric-label">Positive Feedback</div>
        </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value negative">{sentiment_counts.get('negative', 0)}</div>
            <div class="metric-label">Critical Issues</div>
        </div>
    """, unsafe_allow_html=True)
    
with col4:
    avg_response = df.groupby('sentiment')['ticket_id'].count().mean()
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{round(avg_response,1)}h</div>
            <div class="metric-label">Avg. Resolution Time</div>
        </div>
    """, unsafe_allow_html=True)

# --- MAIN DASHBOARD ---
tab1, tab2, tab3 = st.tabs(["📈 Trends", "🔍 Feature Analysis", "📋 Ticket Details"])

with tab1:
    # SENTIMENT TREND CHART
    st.subheader("Customer Sentiment Over Time")
    trend_df = df.groupby(['date', 'sentiment']).size().reset_index(name='count')
    fig = px.area(trend_df, x='date', y='count', color='sentiment',
                 color_discrete_map={
                     'positive': '#4CAF50',
                     'neutral': '#FFC107',
                     'negative': '#F44336'
                 })
    st.plotly_chart(fig, use_container_width=True)
    
    # DAY/HOUR ANALYSIS
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Sentiment by Day of Week")
        day_df = df.groupby(['day_name', 'sentiment']).size().reset_index(name='count')
        fig = px.bar(day_df, x='day_name', y='count', color='sentiment',
                    category_orders={"day_name": ["Monday", "Tuesday", "Wednesday", 
                                                "Thursday", "Friday", "Saturday", "Sunday"]})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Hourly Distribution")
        hour_df = df.groupby(['hour', 'sentiment']).size().reset_index(name='count')
        fig = px.line(hour_df, x='hour', y='count', color='sentiment')
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    # FEATURE ANALYSIS
    st.subheader("Feature Performance")
    feature_df = df.groupby(['feature', 'sentiment']).size().reset_index(name='count')
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Sentiment by Feature**")
        fig = px.sunburst(feature_df, path=['feature', 'sentiment'], values='count')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("**Negative Feedback Breakdown**")
        neg_df = df[df['sentiment'] == 'negative']
        fig = px.pie(neg_df, names='feature', hole=0.3)
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    # DATA TABLE WITH FILTERS - FIXED VERSION
    # Ensure date is in datetime.date format
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # convert and set invalid to NaT
df = df.dropna(subset=['date'])  # drop rows where 'date' couldn't be parsed
df['date'] = df['date'].dt.date  # convert to date only (not datetime)

st.subheader("Customer Feedback Details")

col1, col2, col3 = st.columns(3)
with col1:
    feature_filter = st.multiselect("Filter by Feature", df['feature'].unique())
with col2:
    sentiment_filter = st.multiselect("Filter by Sentiment", df['sentiment'].unique())
with col3:
    min_date = df['date'].min()
    max_date = df['date'].max()

    date_range = st.date_input(
        "Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

filtered_df = df.copy()
if feature_filter:
    filtered_df = filtered_df[filtered_df['feature'].isin(feature_filter)]
if sentiment_filter:
    filtered_df = filtered_df[filtered_df['sentiment'].isin(sentiment_filter)]

# Filter by selected date range
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = filtered_df[
        (filtered_df['date'] >= start_date) & 
        (filtered_df['date'] <= end_date)
    ]

st.dataframe(
    filtered_df[['ticket_id', 'feature', 'message', 'sentiment', 'timestamp']],
    use_container_width=True,
    hide_index=True
)
# --- FOOTER ---
st.markdown("""
    <div style="text-align: center; margin-top: 40px; color: #666; font-size: 12px;">
        XYZ Cloths Co. Customer Experience Dashboard • Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
    </div>
""", unsafe_allow_html=True)
