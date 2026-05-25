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

st.set_page_config(page_title="Divine Messages", page_icon="✨", layout="centered")

# Custom Glassmorphism CSS styling layout
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%) !important;
        color: #ffffff !important;
    }
    h1, h2, h3, p, span, label {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }
    .glass-container {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 35px;
        margin-top: 20px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        text-align: center;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 20px;
        margin-top: 15px;
        box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease, border 0.3s ease, box-shadow 0.3s ease;
        text-align: left;
    }
    .glass-card:hover {
        transform: translateY(-4px);
        border: 1px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(255, 255, 255, 0.08);
    }
    div.stButton > button {
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: #ffffff !important;
        border-radius: 50px !important;
        padding: 14px 40px !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
        margin-top: 10px;
    }
    div.stButton > button:hover {
        background: rgba(255, 255, 255, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        box-shadow: 0 8px 25px rgba(255,255,255,0.15) !important;
        transform: scale(1.02);
    }
    div.stButton > button:active {
        transform: scale(0.98);
    }
    .stProgress > div > div > div > div {
        background-color: rgba(255, 255, 255, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

if "running" not in st.session_state:
    st.session_state.running = False
if "chosen_messages" not in st.session_state:
    st.session_state.chosen_messages = []

st.markdown('<div class="glass-container"><h1>✨ Divine Revelations</h1><p>Experience personalized interactive spiritual insights</p></div>', unsafe_allow_html=True)

def trigger_countdown():
    st.session_state.running = True

st.button(
    "Generate", 
    on_click=trigger_countdown, 
    disabled=st.session_state.running
)

if st.session_state.running:
    countdown_text = st.empty()
    progress_bar = st.progress(0)
    
    for remaining in range(5, 0, -1):
        countdown_text.markdown(f'<div style="text-align:center; margin:15px 0; font-size:1.2rem; font-weight:500;">⏳ Aligning energy... {remaining}s</div>', unsafe_allow_html=True)
        progress_bar.progress((6 - remaining) * 20)
        time.sleep(1)
        
    countdown_text.empty()
    progress_bar.empty()
    
    st.session_state.chosen_messages = random.sample(MESSAGES, 3)
    st.session_state.running = False
    st.rerun()

if st.session_state.chosen_messages and not st.session_state.running:
    for i, msg in enumerate(st.session_state.chosen_messages, 1):
        card_html = f"""
        <div class="glass-card">
            <span style="font-size:0.85rem; text-transform:uppercase; letter-spacing:2px; opacity:0.6; display:block; margin-bottom:5px;">Insight {i}</span>
            <span style="font-size:1.15rem; line-height:1.5; font-weight:400; display:block;">{msg}</span>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
