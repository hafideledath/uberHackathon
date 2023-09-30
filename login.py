import streamlit as st
import hashlib
def main():
    username = "example@gmail.com"
    password = "d9e6762dd1c8eaf6d61b3c6192fc408d4d6d5f1176d0c29169bc24e71c3f274ad27fcd5811b313d681f7e55ec02d73d499c95455b6b5bb503acf574fba8ffe85"

    def passkey(input):
        return hashlib.sha512(input.encode('utf-8')).hexdigest()

    def login():
        if st.session_state.username.lower() == username and passkey(st.session_state.password) == password:
            st.session_state.button_click3 = False

    st.text_input("Username", placeholder="Enter your username", key="username")
    st.text_input("Password", placeholder="Enter your password", key="password", type="password")


    st.button("login", on_click=login)

if __name__ == '__main__':
    main()