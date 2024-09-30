import streamlit as st
import pyautogui
import socket

pyautogui.FAILSAFE = False
hostname = socket.gethostname()

st.set_page_config(page_title=f"Connected to: {hostname}")

button_css = """
    <style>
    .stButton > button {
        font-size: 20px !important;
        padding: 15px 30px !important;
        width: 100% !important;
    }
    </style>
"""
st.markdown(button_css, unsafe_allow_html=True)

# volume controls
st.sidebar.subheader("Volume Control")
if st.sidebar.button("🔊"):
    pyautogui.press("volumeup")
if st.sidebar.button("🔉"):
    pyautogui.press("volumedown")
if st.sidebar.button("🔇"):
    pyautogui.press("volumemute")

# media controls
st.sidebar.subheader("Media Control")
if st.sidebar.button("⏯️"):
    pyautogui.press("space")
if st.sidebar.button("⏪"):
    pyautogui.press("left")
if st.sidebar.button("⏩"):
    pyautogui.press("right")

# mouse controls
st.subheader("Mouse Control")
st.write("Use the buttons below to control the mouse pointer. Tap to move and click.")

if st.button("⬆️"):
    pyautogui.moveRel(0, -40)
if st.button("⬅️"):
    pyautogui.moveRel(-40, 0)
if st.button("➡️"):
    pyautogui.moveRel(40, 0)
if st.button("⬇️"):
    pyautogui.moveRel(0, 40)

if st.button("Click"):
    pyautogui.click()

if st.button("Enter"):
    pyautogui.press("enter")
