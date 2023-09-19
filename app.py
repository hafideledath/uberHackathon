import streamlit as st
from home import main as home, st
from route import main as route
from layout import connections, Ride_options, Ride_options

if 'model_response' not in st.session_state:
        st.session_state.model_response = ''

def ride():
    if st.session_state.model == "Choose a model": 
        st.session_state.model_response = ""
    else:
        st.session_state.model_response = f'You selected: {st.session_state.model}'

        
if 'button_click' not in st.session_state:
    st.session_state.button_click = False

if 'shortest_route' not in st.session_state:
    st.session_state.shortest_route = ""

if 'route_impact' not in st.session_state:
    st.session_state.route_impact = ""

if 'route_distance' not in st.session_state:
    st.session_state.route_distance = ""
    
print(st.session_state.button_click)

if (st.session_state.button_click):
    route()
    st.write(st.session_state.shortest_route)
    st.write(f"{st.session_state.route_impact}g of Carbon emissions")
    st.write(f"{st.session_state.route_distance} kilometers for your journey")
    st.selectbox('Choose a model', [ride_option.name for ride_option in Ride_options], on_change=ride, key='model')
else:
    home()