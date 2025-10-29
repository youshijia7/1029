import streamlit as st

st.title("Jacky's app")
st.write("Hellow World")

name = st.text_input("name:")
if st.button("yyds"):
    st.success(f"hello,mr.{name},yyds!")

