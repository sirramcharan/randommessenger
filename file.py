import streamlit as st
import random
import time

MESSAGES = [
    "Why fear when I am here? Surrender your worries to Me.",
    "The crisis will pass. Keep your mind steady and pray.",
    "Your tears have reached Me. Relief is coming very soon.",
    "Do not lose courage. This trial is testing your faith.",
    "Trust My timing. What you seek is being prepared for you.",
    "Leave the outcome to Me and perform your daily duties.",
    "You are never alone. I walk beside you always.",
    "Silence your mind. The answer you seek is within you.",
    "Your prayers are answered. Have patience for a little longer.",
    "Give Me your burdens. I will carry them for you.",
    "Shift your focus from the problem to the Divine.",
    "This obstacle is a blessing in disguise. Trust My plan.",
    "Speak less, pray more. The storm will soon calm down.",
    "Your faith is your shield. Do not let doubt enter.",
    "What seems lost will be returned in a better form.",
    "I am watching over your family. Do not be anxious.",
    "True surrender means accepting whatever comes as My grace.",
    "Your devotion has pleased Me. Stay on the righteous path.",
    "Do not rush. The fruit ripens only when the time is right.",
    "Hold fast to Truth. Victory will ultimately be yours.",
    "Do your duty out of love, not for the reward.",
    "Rectify your own mistakes before pointing out others' flaws.",
    "Help ever, hurt never. This is the highest spiritual practice.",
    "Clear your past karma through selfless service to humanity.",
    "Do not react in anger. Silence is your best weapon now.",
    "Speak softly and sweetly. Your words can heal wounds.",
    "The work you are doing is holy. Complete it honestly.",
    "Success will come when you eliminate your ego completely.",
    "Do not gossip or listen to slander. Protect your peace.",
    "Forgive those who hurt you. It frees your own soul.",
    "Greed brings misery. Be content with what you have.",
    "Serve the poor and needy. I reside in their hearts.",
    "Do not seek validation from the world. Seek My approval.",
    "Your current suffering is burning away your past negative karma.",
    "Pure intentions matter more than grand rituals or displays.",
    "Be honest in your business. Wealth earned wrongly never lasts.",
    "Control your senses. They are pulling you away from peace.",
    "Do not hesitate to do good, even if you stand alone.",
    "Treat everyone you meet today as a form of the Divine.",
    "Dedicate every action you perform this day to Me.",
    "Chant My name constantly. It will purify your mind.",
    "Happiness is an internal state, not an external possession.",
    "Meditate on the light within your heart every morning.",
    "Fill your heart with love, and hatred will vanish instantly.",
    "The world is a mirror. What you see reflects your mind.",
    "Spend time in silence today to recharge your spiritual energy.",
    "Do not let external chaos disturb your inner sanctuary.",
    "See the good in everything. Every event teaches a lesson.",
    "Your mind is like a restless monkey. Calm it with prayer.",
    "Detach yourself from worldly expectations to avoid grief.",
    "The body is a temple. Keep it clean and healthy.",
    "Cultivate humility. A proud heart cannot receive divine grace.",
    "True wisdom is seeing unity in all worldly diversity.",
    "Let go of the past. Live fully in the present moment.",
    "Do not worry about the future. It is safe in My hands.",
    "Your spiritual progress is steady. Keep moving forward.",
    "Read sacred books to elevate your thoughts today.",
    "Contentment is the greatest wealth you can ever possess.",
    "Be like a lotus flower—live in water but remain untouched.",
    "Cleanse your heart so that I may make it My home.",
    "Your health will improve. Take your medicine and pray.",
    "Divine grace is the best medicine. Have complete faith.",
    "I am curing your deep-seated illness. Be patient.",
    "Eat pure food and keep your thoughts completely positive.",
    "The danger has been averted by My protective grace.",
    "Do not fear disease. The soul is forever free from sickness.",
    "Your loved one is under My direct care and protection.",
    "Peace of mind is the foundation of physical health.",
    "I have shortened the duration of your current suffering.",
    "Relax your nerves. Surrender your physical pain to Me.",
    "You are being shielded from a major hidden calamity.",
    "Sleep peacefully tonight. My angels are guarding you.",
    "A positive attitude will accelerate your physical recovery.",
    "Avoid stressful thoughts; they harm your physical body.",
    "Your prayers for another person's health are accepted.",
    "I am the Divine Physician. Trust in My healing touch.",
    "Fill your mind with cheerful thoughts to heal yourself.",
    "No harm can touch you while My grace shields you.",
    "Your strength will return. Do not give up hope now.",
    "This body is temporary, but your spirit is eternal.",
    "I know your innermost thoughts. Nothing is hidden from Me.",
    "You have My full blessings for this new venture.",
    "The path ahead is clear. Move forward with confidence.",
    "An unexpected help will arrive at the exact right moment.",
    "Your financial worries will ease up in a short time.",
    "Make the decision with a calm mind; I will guide you.",
    "The confusion will clear up by tomorrow morning. Stay calm.",
    "You are on the right track. Do not look back now.",
    "A joyful celebration awaits your family very soon.",
    "Good news is on the way. Keep a hopeful heart.",
    "The dark night of the soul is ending. Dawn is near.",
    "I have heard your silent cry in the dead of night.",
    "Your long-standing wish will be fulfilled in My way.",
    "Do not doubt My love for you. It is unconditional.",
    "You are closer to your spiritual goal than you realize.",
    "This meeting or journey will yield very good results.",
    "Be a source of joy to everyone around you today.",
    "Your sacrifice has not gone unnoticed by the Divine.",
    "True transformation takes time. Do not be discouraged.",
    "I am testing you only to bring out your maximum strength.",
    "The answer you want is 'Yes', but proceed with caution.",
    "Wait for a few days before taking any major step.",
    "Change your perspective, and the problem will disappear.",
    "You are an instrument in My hands. Let Me play the tune.",
    "Great peace is coming to your troubled heart today.",
    "Walk the path of love, and you will find Me everywhere.",
    "Your life is a gift. Use it to spread divine light.",
    "I bless you. Go forward with a brave and happy heart."
]

st.set_page_config(page_title="Glassmorphism Sanctuary", page_icon="🔮", layout="centered")

# Theme selection interaction
bg_theme = st.sidebar.selectbox(
    "Choose Aesthetic",
    ["Midnight Nebula", "Cyber Sunset", "Emerald Aurora"]
)

# Interactive custom countdown duration adjustment
countdown_duration = st.sidebar.slider("Countdown Duration (Seconds)", 3, 10, 5)

# Interactive category filters
category_filter = st.sidebar.radio(
    "Filter Guidance Category",
    ["All Messages", "Inner Peace & Mind", "Health & Healing", "Future & Blessings"]
)

# Apply dynamic background styles based on interaction
bg_gradients = {
    "Midnight Nebula": "linear-gradient(135deg, #0f2027, #203a43, #2c5364)",
    "Cyber Sunset": "linear-gradient(135deg, #111111, #190a1e, #3a1c3b)",
    "Emerald Aurora": "linear-gradient(135deg, #051911, #0d3421, #162529)"
}

selected_bg = bg_gradients[bg_theme]

# Glassmorphism Global Injector
st.markdown(f"""
    <style>
    .stApp {{
        background: {selected_bg} !important;
        color: #ffffff !important;
    }}
    .glass-box {{
        background: rgba(255, 255, 255, 0.04) !important;
        backdrop-filter: blur(12px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(12px) saturate(180%) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 20px !important;
        padding: 25px !important;
        margin-top: 15px !important;
        margin-bottom: 25px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
    }}
    h1, h2, h3, p, label, .stWidgetLabel {{
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }}
    div.stButton > button {{
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(5px) !important;
        border-radius: 12px !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }}
    div.stButton > button:hover {{
        background: rgba(255, 255, 255, 0.2) !important;
        border-solid: 1px solid rgba(255, 255, 255, 0.4) !important;
        transform: scale(1.02);
    }}
    </style>
""", unsafe_allow_html=True)

# Main glass container setup
st.markdown("<div class='glass-box'><h1>🔮 Glassmorphism Divine Portal</h1><p>Set configurations in the sidebar menu and pull deep cosmic insights.</p></div>", unsafe_allow_html=True)

# Filter implementation based on interaction selection
if category_filter == "Inner Peace & Mind":
    pool = MESSAGES[24:60]
elif category_filter == "Health & Healing":
    pool = MESSAGES[60:80]
elif category_filter == "Future & Blessings":
    pool = MESSAGES[80:108]
else:
    pool = MESSAGES

if "running" not in st.session_state:
    st.session_state.running = False
if "chosen" not in st.session_state:
    st.session_state.chosen = []

def start_cycle():
    st.session_state.running = True

# Main call to action trigger
st.button("Manifest Selected Array", on_click=start_cycle, disabled=st.session_state.running)

if st.session_state.running:
    status_holder = st.empty()
    bar_holder = st.progress(0)
    
    for passed in range(countdown_duration, 0, -1):
        status_holder.markdown(f"<div style='text-align: center; font-size: 1.2rem; margin: 10px;'>⚡ Aligning timelines... ({passed}s remaining)</div>", unsafe_allow_html=True)
        percent = int(((countdown_duration - passed + 1) / countdown_duration) * 100)
        bar_holder.progress(percent)
        time.sleep(1)
        
    status_holder.empty()
    bar_holder.empty()
    
    st.session_state.chosen = random.sample(pool, min(3, len(pool)))
    st.session_state.running = False
    st.rerun()

# Output styling wrapped inside sleek transparent container objects
if st.session_state.chosen and not st.session_state.running:
    st.markdown("### 🌌 Received Manifestations")
    for rank, insight in enumerate(st.session_state.chosen, 1):
        st.markdown(f"""
            <div class='glass-box' style='margin-bottom:15px;'>
                <span style='color: #a3e635; font-weight: bold; font-size:0.9rem;'>INSIGHT 0{rank}</span>
                <p style='font-size: 1.15rem; margin-top: 5px; line-height:1.5;'>"{insight}"</p>
            </div>
        """, unsafe_allow_html=True)

    # Interactive reset state feature
    if st.button("Clear Dynamic Cache"):
        st.session_state.chosen = []
        st.rerun()
