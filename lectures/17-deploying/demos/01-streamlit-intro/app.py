import streamlit as st

# display some text
st.title("Number Doubler")
st.write("Enter a number and I'll double it for you.")

# ask for input
number = st.number_input("Enter a number", value=0)

# this is just standard Python
doubled = number * 2

# display the result
st.write(f"{number} doubled is {doubled}.")
