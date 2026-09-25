import streamlit as st
import random

# إعدادات الصفحة
st.set_page_config(page_title="Poker Star", page_icon="♠️", layout="centered")

st.title("♠️ Poker Star - بوكر ستار ♣️")
st.write("مرحباً بك في لعبة Poker Star! اضغط على الزر لسحب الكروت وتجربة حظك.")

# تعريف كروت اللعب
SUITS = ['♠️', '♥️', '♦️', '♣️']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    return [f"{rank}{suit}" for suit in SUITS for rank in RANKS]

# إدارة حالة اللعبة
if 'deck' not in st.session_state or st.button("إعادة توزيع / لعبة جديدة 🔄"):
    st.session_state.deck = create_deck()
    random.shuffle(st.session_state.deck)
    st.session_state.player_hand = [st.session_state.deck.pop(), st.session_state.deck.pop()]
    st.session_state.community_cards = [st.session_state.deck.pop() for _ in range(5)]

st.divider()

# عرض كروت اللاعب
st.subheader("🃏 كروتك (Player Hand):")
col1, col2 = st.columns(2)
with col1:
    st.info(f"### {st.session_state.player_hand[0]}")
with col2:
    st.info(f"### {st.session_state.player_hand[1]}")

# عرض كروت الطاولة
st.subheader("🌐 كروت الطاولة (Community Cards):")
cols = st.columns(5)
for i in range(5):
    with cols[i]:
        st.success(f"### {st.session_state.community_cards[i]}")

st.divider()
st.success("🎉 نتمنى لك حظاً سعيداً في اللعبة!")
