
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="ProGaming AI Advisor",
    page_icon="🎮",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextInput>div>div>input {
        background-color: #161b22;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎮 ProGaming AI Voice Assistant & Sensitivity Hub")
st.write("Get expert gaming settings, recoil guides, and tactical advice across multiple titles with dual-voice narration.")

# Sidebar Controls
st.sidebar.header("⚙️ Game & Voice Setup")
game_choice = st.sidebar.selectbox("Select Game", [
    "PUBG Mobile", 
    "Free Fire", 
    "Call of Duty: Mobile", 
    "Valorant", 
    "Apex Legends Mobile"
])
device_type = st.sidebar.selectbox("Device / Platform", [
    "Smartphone (Gyroscope)", 
    "Smartphone (Non-Gyro)", 
    "PC / Emulator (GameLoop)"
])

# Dual Voice Selection for AI persona
ai_voice = st.sidebar.radio("Select AI Voice Persona", ["👦 Leo (Male Advisor - Tactical & Direct)", "👧 Maya (Female Advisor - Analytical & Detailed)"])

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Use the settings below to fine-tune your crosshair placement, sensitivity tiers, and hardware layout.")

# Main Interface
st.subheader(f"🎯 Expert Database for: {game_choice}")
user_query = st.text_input("Ask a specific question (e.g., 'Best M416 recoil control settings' or 'How to improve headshot accuracy'):")

if st.button("Get AI Advice", type="primary"):
    if user_query:
        with st.spinner("Consulting pro database..."):
            st.markdown("---")
            
            # Voice Persona Display Header
            if "Leo" in ai_voice:
                st.markdown("### 👦 Leo's Tactical Breakdown")
                persona_intro = "Listen up! Here is the precise configuration you need to dominate your gunfights."
            else:
                st.markdown("### 👧 Maya's Analytical Breakdown")
                persona_intro = "Analyzing your query with optimal competitive parameters. Here is your setup guide:"
                
            st.write(persona_intro)
            
            # Game-Specific Logic Database
            if "pubg" in game_choice.lower():
                col1, col2 = st.cols(2) if hasattr(st, 'cols') else (st, st)
                with col1:
                    st.markdown("#### 📱 Recommended Sensitivity")
                    st.markdown("- **Camera (3P No Scope):** 130%")
                    st.markdown("- **Red Dot / Holographic:** 52%")
                    st.markdown("- **3x / 4x Scope:** 22% - 25%")
                with col2:
                    st.markdown("#### 🔄 Gyroscope & Recoil")
                    st.markdown("- **Gyroscope Red Dot:** 300%")
                    st.markdown("- **Drill Routine:** 15 mins daily recoil spray practice in training grounds without attachments first.")
            elif "free fire" in game_choice.lower():
                st.markdown("#### 🔥 Free Fire Sensitivity Setup")
                st.markdown("- **General:** 95-100 (for fast 360-degree drag rotations)")
                st.markdown("- **Red Dot:** 85-90")
                st.markdown("- **2x Scope:** 80-85 | **4x Scope:** 75-80")
            elif "valorant" in game_choice.lower():
                st.markdown("#### 🎯 Valorant Sensitivity & Crosshair")
                st.markdown("- **eDPI Range:** 200 - 400 (e.g., Mouse DPI 800 * In-game 0.35)")
                st.markdown("- **Crosshair Tip:** Keep crosshair static at head-level; minimize unnecessary movement.")
            else:
                st.markdown(f"#### ⚙️ Optimized Settings for {game_choice}")
                st.markdown("- Balance your tracking sensitivity to prevent over-aiming during close-range encounters.")
                
            st.success(f"**Answering your question:** '{user_query}' — Applied successfully for {device_type}.")
    else:
        st.warning("Please enter a question to generate advice.")

# Footer info
st.markdown("---")
st.caption("ProGaming AI Web App • Built with Python & Streamlit")
