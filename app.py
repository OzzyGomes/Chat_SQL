from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
import streamlit as st


def init_database(user: str, password: str, host: str, port: int, database: str) -> SQLDatabase:
    db_srt = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_srt)



load_dotenv()

st.set_page_config(page_title= "Chat com MySQL", page_icon=":speech_balloon:")

st.title("Chat com MySQL")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a simple chat application using MySQL. Connect to the database and start chatting.")

    st.text_input("Host", value="localhost")
    st.text_input("Port", value="3306")
    st.text_input("User", value="root")
    st.text_input("Password", type="password", value="admin")
    st.text_input("Database", value="")

    st.button("Connect")

st.chat_input("escreva algo aqui... ")
    