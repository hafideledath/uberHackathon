import streamlit as st
from home import main as home
from route import main as route

if 'button_click' not in st.session_state:
    st.session_state.button_click = False

if 'shortest_route' not in st.session_state:
    st.session_state.shortest_route = ""

print(st.session_state.button_click)

if (st.session_state.button_click):
    route()
    st.write(st.session_state.shortest_route)
else:
    home()