import streamlit as st
st.title("Hello World")
st.header("My first streamlit app")
name =st.text_input("Enter Your Name")
st.write("Hello", name)
if st.button("Submit"):
    st.write("This button was clicked")
num=st.number_input("Enter your age:",min_value=0,max_value=100,step=1)
num1=st.slider("Select your age:",min_value=0,max_value=70,step=1)
course=st.selectbox("Choose your courses",["Select your course","B.tech","M.tech","BCA","MCA"])
check=st.checkbox("I'm not a robot")
set=st.radio("Choose your gender",["Male","Female"])
text=st.text_area("Write Something")
store=st.file_uploader("Select your File",type=["jpg","raw","zip","jpeg","pdf"])
sidebar=st.sidebar.title("Hello")
sidebar1=st.sidebar.selectbox("select your country",["Select","india","japan","pakistan"])
col1,col2=st.columns(2)
with col1:
    st.header("input")
with col2:
    st.header("output")
prompt=st.chat_input("Ask Something...")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
            st.write("hello, I'm here to help you")
