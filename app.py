from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


def get_response(question):
    chat = ChatGroq(model="llama-3.1-8b-instant")
    response = chat.invoke(question)
    return response.content

st.set_page_config(page_title="Chatbot", page_icon=":robot_face:", layout="wide")


st.sidebar.title("About")
st.sidebar.write("This is a Chatbot application using Langchain and Streamlit.")
st.sidebar.write("Enter your prompt in the input box and click 'Generate Response' to get a response.")


st.header("Langchain Application")
st.markdown("### Welcome to the Chatbot!")
st.write("Enter your prompt below and get an instant response.")


input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Generate Response")


if submit_button:
    with st.spinner("Processing your question..."):
        response = get_response(input_text)
    st.subheader("The Response is")
    st.text_area("", response, height=200)

st.success("Thank you for using our Chatbot!")

st.markdown("---")
st.write("### Additional Information")
st.info("This application uses the ChatGroq model from Langchain.")


# Footer
st.markdown("---")
st.markdown("#### Contact Us")
st.write("For any queries, please contact us at [kanhaiya.yadav7375@gmail.com](mailto:kanhaiya.yadav7375@gmail.com).")
