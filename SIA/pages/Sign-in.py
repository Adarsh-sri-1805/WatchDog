import streamlit as st
from streamlit.components.v1 import html
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="SIA - Partner Portal",
    layout="centered",
    page_icon="✨"
)

# --- CSS & ANIMATIONS ---
st.markdown("""
    <style>
        /* REMOVE DEFAULT PADDING */
        .stApp {
            padding-top: 0 !important;
            margin-top: -30px !important;
        }
        div.block-container {
            padding-top: 0;
        }
        
        /* ANIMATIONS */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .fade-in {
            animation: fadeIn 0.5s ease-out;
        }
        
        /* WELCOME CARD STYLING */
        .card {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            margin: 1rem 0;
        }
        .title {
            color: #2B2D42;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .logo {
            text-align: center;
            margin: 0 0 0.5rem 0;
        }
        .btn-primary {
            background: #4361ee;
            color: white;
            border: none;
            padding: 0.75rem;
            border-radius: 8px;
            width: 100%;
            font-weight: 600;
            transition: all 0.3s;
        }
        .btn-primary:hover {
            background: #3a0ca3;
            transform: translateY(-2px);
        }
    </style>
""", unsafe_allow_html=True)

# --- JS FOR ANIMATIONS ---
def animate():
    js = """
    <script>
        function observeElements() {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('fade-in');
                    }
                });
            }, {threshold: 0.1});
            
            document.querySelectorAll('.card').forEach(el => {
                observer.observe(el);
            });
        }
        observeElements();
    </script>
    """
    html(js)

# --- APP LOGIC ---
def show_welcome():
    st.markdown('<div class="logo"><h1>SIA</h1></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="title">Partner Portal</h2>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("Welcome to SIA's Partner Network. Please select an option:")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("New Partner Sign Up", key="signup", help="Join our network for the first time"):
                st.session_state.stage = "signup"
                st.rerun()
        with col2:
            if st.button("Existing Partner Login", key="login", help="Access your partner dashboard"):
                st.session_state.stage = "login"
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

def show_signup():
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="title">New Partner Registration</h3>', unsafe_allow_html=True)
        
        current_step = st.session_state.get("signup_step", 0)
        st.progress((current_step + 1) * 33)
        
        if current_step == 0:
            company = st.text_input("Company Name*", placeholder="Your official business name")
            email = st.text_input("Business Email*", placeholder="contact@yourcompany.com")
            country = st.selectbox("Country*", ["Select", "India","USA", "UK", "Canada", "Australia", "Other"])
            
            if st.button("Continue →", key="step1"):
                if company and email and country != "Select":
                    st.session_state.signup_data = {"company": company, "email": email, "country": country}
                    st.session_state.signup_step = 1
                    st.rerun()
                else:
                    st.warning("Please fill all required fields")
        
        elif current_step == 1:
            st.markdown(f"**{st.session_state.signup_data['company']}**, tell us about your operations:")
            
            biz_type = st.selectbox("Business Type*", ["Service","Manufacturer", "Retailer", "Wholesaler", "E-commerce", "Boutique", "Other"])
            products = st.multiselect("Product Categories", ["All","Men's", "Women's", "Children's", "Accessories", "Sportswear"])
            
            if st.button("← Back", key="back1"):
                st.session_state.signup_step = 0
                st.rerun()
            if st.button("Continue →", key="step2"):
                st.session_state.signup_data.update({
                    "biz_type": biz_type,
                    "products": products
                })
                st.session_state.signup_step = 2
                st.rerun()
                
        elif current_step == 2:
            st.markdown(f"Almost done, **{st.session_state.signup_data['company']}**!")
            
            st.write("How did you hear about us?")
            referral = st.selectbox("Referral Source", ["Search Engine", "Trade Show", "Existing Partner", "Social Media", "Other"])
            
            agree = st.checkbox("I agree to Partner Terms*")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("← Back", key="back2"):
                    st.session_state.signup_step = 1
                    st.rerun()
            with col2:
                if st.button("Submit Application", type="primary", disabled=not agree):
                    st.session_state.signup_data["referral"] = referral
                    st.success("✅ Application submitted successfully!")
                    st.balloons()
                    time.sleep(2)
                    del st.session_state.signup_step
                    del st.session_state.signup_data
                    st.session_state.stage = None
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

def show_login():
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="title">Partner Login</h3>', unsafe_allow_html=True)
        
        email = st.text_input("Email Address", placeholder="your@email.com")
        password = st.text_input("Password", type="password")
        
        if st.button("Login", type="primary"):
            st.success("Login successful!")
            time.sleep(1)
            st.session_state.stage = None
            st.rerun()
            
        st.markdown("Forgot password? [Reset here](#)")
        st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN APP FLOW ---
if "stage" not in st.session_state:
    st.session_state.stage = None

animate()  # Activate animations

if st.session_state.stage == "signup":
    show_signup()
elif st.session_state.stage == "login":
    show_login()
else:
    show_welcome()

# Hide Streamlit menu and footer
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
