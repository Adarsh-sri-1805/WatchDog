import streamlit as st
from PIL import Image

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Customer Sentiment Watchdog", 
    layout="wide",
    
)

# ---------- INLINE STYLING ----------
st.markdown("""
    <style>
        :root {
            --primary: #4361ee;
            --secondary: #3f37c9;
            --accent: #4895ef;
            --dark: #1f4068;
            --light: #f8f9fa;
        }
        
        .main-title {
            font-size: 56px;
            font-weight: 900;
            color: var(--dark);
            text-align: center;
            padding: 20px 0 10px;
            background: linear-gradient(to right, #4361ee, #3a0ca3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0;
        }
        .subtitle {
            font-size: 24px;
            color: #555;
            text-align: center;
            margin-bottom: 40px;
            font-weight: 400;
        }
        .feature-title {
            font-size: 32px;
            font-weight: 700;
            margin: 50px 0 30px;
            color: var(--dark);
            text-align: center;
        }
        .section {
            padding: 60px 20px;
            margin: auto;
            max-width: 1200px;
        }
        .image-box {
            border-radius: 16px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.12);
            border: 1px solid rgba(255,255,255,0.2);
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        .image-box:hover {
            transform: translateY(-5px);
        }
        .feature-card {
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.08);
            height: 100%;
            transition: all 0.3s ease;
            border: 1px solid rgba(0,0,0,0.05);
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0,0,0,0.12);
        }
        .feature-icon {
            width: 80px;
            height: 80px;
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #4361ee, #3a0ca3);
            border-radius: 50%;
            color: white;
            font-size: 36px;
        }
        .cta-section {
            background: linear-gradient(135deg, #4361ee, #3a0ca3);
            color: white;
            padding: 60px 20px;
            border-radius: 16px;
            text-align: center;
            margin: 60px 0;
        }
        .cta-button {
            background: white;
            color: var(--primary);
            border: none;
            padding: 12px 30px;
            font-size: 18px;
            border-radius: 50px;
            font-weight: 600;
            margin-top: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        .divider {
            height: 3px;
            background: linear-gradient(to right, transparent, rgba(67, 97, 238, 0.5), transparent);
            margin: 40px auto;
            width: 60%;
            border: none;
        }
        .stats-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin: 40px 0;
        }
        .stat-item {
            text-align: center;
            padding: 20px;
        }
        .stat-value {
            font-size: 42px;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 5px;
        }
        .stat-label {
            font-size: 16px;
            color: #666;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown('<div class="main-title">Customer Sentiment Watchdog(SIA)</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-powered customer sentiment analysis to transform support operations and boost satisfaction</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 30px;">
        <a href='/Sign-in' target='_self'>
            <button class="cta-button" style="margin-right: 110px;">Get Started</button>
        </a>
        <a href='/SIA_Bot' target='_self'>
            <button class="cta-button">Try SIA bot</button>
        </a>
    </div>
""", unsafe_allow_html=True)


with col2:
    image_path = "Gemini_Generated_Image_3kaw693kaw693kaw.png"
    if os.path.exists(image_path):
        hero_img = Image.open(image_path)
    else:
        hero_img = Image.new('RGB', (600, 400), color='#f0f2f6') 

# ---------- STATS BAR ----------
st.markdown("""
    <div class="stats-container">
        <div class="stat-item">
            <div class="stat-value">85%</div>
            <div class="stat-label">Faster Response Time</div>
        </div>
         <div class="stat-item">
            <div class="stat-value">24/7</div>
            <div class="stat-label">Sentiment Monitoring</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">50+</div>
            <div class="stat-label">Hours of testing</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------- DIVIDER ----------
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ---------- SIA INTRODUCTION ----------
st.markdown('<div class="feature-title">Meet SIA – Your Sentiment Intelligence Assistant</div>', unsafe_allow_html=True)

col3, col4 = st.columns([1, 1])

with col3:
    st.markdown("""
    SIA is your AI-powered teammate that analyzes customer communications in real-time, 
    classifies tickets by sentiment and urgency, and delivers actionable insights through natural conversation.
    """)
    
    st.markdown("**Ask SIA anything:**")
    st.markdown("""
    - "What are today's most urgent complaints?"
    - "Show negative sentiment trends from last week"
    - "Which product has the most complaints this month?"
    """)
    
    st.markdown("""
    Our AI learns from your historical ticket data to provide increasingly accurate predictions and recommendations, 
    helping you reduce response times and improve customer satisfaction.
    """)

with col4:
    # Placeholder for SIA demo image/gif

    real_img = Image.open("ss.png")  # Update path as needed
    st.image(real_img, use_container_width=True, caption="SIA in action - Real-time sentiment analysis dashboard")


# ---------- FEATURES SECTION ----------
st.markdown('<div class="feature-title">Powerful Features</div>', unsafe_allow_html=True)

col5, col6, col7 = st.columns(3)

with col5:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3 style="text-align: center; margin-bottom: 15px;">Real-time Analytics</h3>
            <p style="text-align: center; color: #555;">
                Track sentiment trends with beautiful visualizations. Spot emerging issues before they escalate with anomaly detection.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🚨</div>
            <h3 style="text-align: center; margin-bottom: 15px;">Smart Alerts</h3>
            <p style="text-align: center; color: #555;">
                Get instant notifications when sentiment drops or urgent tickets come in. Configure alerts by team, product, or priority.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col7:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3 style="text-align: center; margin-bottom: 15px;">AI Assistant</h3>
            <p style="text-align: center; color: #555;">
                Natural language interface to query your data. Ask questions, get insights, and automate reporting.
            </p>
        </div>
    """, unsafe_allow_html=True)

# Add second row of feature cards
st.write("")  # Spacer
col8, col9, col10 = st.columns(3)

with col8:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📂</div>
            <h3 style="text-align: center; margin-bottom: 15px;">Seamless Integration</h3>
            <p style="text-align: center; color: #555;">
                Connect with Zendesk, Salesforce, Intercom, or upload CSVs. Works with your existing tools.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col9:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <h3 style="text-align: center; margin-bottom: 15px;">Deep Analysis</h3>
            <p style="text-align: center; color: #555;">
                Understand not just sentiment but also topics, intent, and emotion behind customer messages.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col10:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <h3 style="text-align: center; margin-bottom: 15px;">Performance Tracking</h3>
            <p style="text-align: center; color: #555;">
                Measure how sentiment changes over time and correlate with support improvements.
            </p>
        </div>
    """, unsafe_allow_html=True)

# ---------- CTA SECTION ----------
st.markdown("""
    <div class="cta-section">
        <h2 style="color: white; font-size: 36px; margin-bottom: 20px;">Ready to transform your customer support?</h2>
        <p style="color: rgba(255,255,255,0.9); font-size: 18px; margin-bottom: 10px;">
            Join leading companies who use Sentiment Watchdog to improve customer satisfaction and reduce response times.
        </p>
        <button class="cta-button" style="background: white; color: var(--primary); margin-top: 30px;">
            Request a Demo
        </button>
    </div>
""", unsafe_allow_html=True)

# ---------- TESTIMONIALS ----------
st.markdown('<div class="feature-title">Trusted by Support Teams Worldwide</div>', unsafe_allow_html=True)

testimonial_col1, testimonial_col2 = st.columns(2)

with testimonial_col1:
    st.markdown("""
        <div style="background: white; border-radius: 12px; padding: 30px; margin: 15px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="width: 60px; height: 60px; background: #ddd; border-radius: 50%; margin-right: 15px;"></div>
                <div>
                    <h4 style="margin: 0;">Sarah Johnson</h4>
                    <p style="margin: 0; color: #666;">Customer Support Director, TechCorp</p>
                </div>
            </div>
            <p style="font-style: italic; color: #444; line-height: 1.6;">
                "Sentiment Watchdog helped us reduce our response time to negative feedback by 65%. The AI alerts ensure we never miss an angry customer."
            </p>
        </div>
    """, unsafe_allow_html=True)

with testimonial_col2:
    st.markdown("""
        <div style="background: white; border-radius: 12px; padding: 30px; margin: 15px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="width: 60px; height: 60px; background: #ddd; border-radius: 50%; margin-right: 15px;"></div>
                <div>
                    <h4 style="margin: 0;">Michael Chen</h4>
                    <p style="margin: 0; color: #666;">VP Customer Experience, GlobalBank</p>
                </div>
            </div>
            <p style="font-style: italic; color: #444; line-height: 1.6;">
                "The dashboard gives us visibility we never had before. We can now proactively address issues before they become complaints."
            </p>
        </div>
    """, unsafe_allow_html=True)
