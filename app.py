import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game")
st.title("🎲 Number Guessing Game")
st.write("Guess the hidden number between 1 and 20.")

# Keep secret number and tries between button clicks
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 20)
    st.session_state.tries = 0

guess = st.number_input("Enter a number between 1 and 20:", min_value=1, max_value=20, step=1)

col1, col2 = st.columns(2)

if col1.button("Guess"):
    st.session_state.tries += 1
    if guess < st.session_state.secret:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.secret:
        st.warning("Too high! Try again.")
    else:
        st.success(f"🎉 Correct! The number was {st.session_state.secret}")
        st.balloons()

if col2.button("Play again"):
    st.session_state.secret = random.randint(1, 20)
    st.session_state.tries = 0
    st.experimental_rerun()

st.write(f"Attempts: **{st.session_state.tries}**")
