import streamlit as st

st.title("Welcome to Python App")
st.subheader("using streamlit")

st.header('This is a heading')
st.text('this is normal text')
st.write('this is also a normal text but better')
st.info('this is a information text')
st.success('this should be shown when successfull')
st.error('this is text area for showing error')
st.warning('this is text area for showing warning')
st.markdown('''
- [x] this is markdown
- [x] for adding html to code
- [x] if u want something like this
''')

name = st.text_input("What's your name?")
email = st.text_input("What's your email?")
age = st.number_input("What's your age?",step=1,value=12)
comment = st.text_area("What's your comment?")
date  = st.date_input("When is your birthday?")

st.write(name)
st.write(email)
st.write(age)
st.write(comment)
st.write(date)