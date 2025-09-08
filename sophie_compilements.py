# Save as: sophie_compliments.py
import streamlit as st
import random

st.set_page_config(page_title="Sophie’s Compliment Generator", page_icon="💖")

st.title("💖 Sophie’s Compliment Generator 💖")
st.write("Click the button and get a random cute/funny compliment just for you, Sophie! ✨")

# List of compliments
compliments = [
    "Sophie, you light up every room you enter! 🌟",
    "You have the best smile 😄💖",
    "Your sense of humor is top-tier 😂🔥",
    "You’re basically a legend, Sophie 👑✨",
    "Brains + beauty = Sophie 😎💫",
    "You make Mondays feel like Fridays 😏🎉",
    "Your energy is contagious! ⚡💖",
    "Lowkey, you could rule the world 👀🌍",
    "You’re like sunshine on a rainy day 🌞🌧️",
    "Sophie, you’re unstoppable 💪💖"
]

# Button to generate compliment
if st.button("✨ Generate Compliment ✨"):
    st.success(random.choice(compliments))

# Optional styling
st.markdown(
    """
    <style>
    body { background-color: #fff0f5; }
    .stButton>button { background-color: #ff69b4; color: white; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True
)
