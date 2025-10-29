import streamlit as st

st.title("Streamlit 테스트 앱")
st.write("Hellow World")

name = st.text_input("name:")
if st.button("인사"):
    st.success(f"hello,mr.{name}!")
