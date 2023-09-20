import streamlit as st
from home import main as home, st
from final import main as final
from route import main as route
from layout import connections, Ride_options
import streamlit.components.v1 as components

if 'model_response' not in st.session_state:
        st.session_state.model_response = ''
option_chosen = ""

def ride():
    if st.session_state.model == "Choose a model": 
        st.session_state.model_response = ""
    else:
        st.session_state.model_response = st.session_state.model
        st.session_state.button_click1 = False
        st.session_state.button_click2 = True
        
        

        
if 'button_click1' not in st.session_state:
    st.session_state.button_click1 = False
    
if 'button_click2' not in st.session_state:
    st.session_state.button_click2 = False
    
if 'shortest_route' not in st.session_state:
    st.session_state.shortest_route = ""

if 'route_impact' not in st.session_state:
    st.session_state.route_impact = ""

if 'route_distance' not in st.session_state:
    st.session_state.route_distance = ""
    
    
def route_impact_model():
  for i in range(len(Ride_options)):
    if Ride_options[i][0] == st.session_state.model_response:
          return i
  

if (st.session_state.button_click1):
    route()
    Dog=[]
    for i in range(len(Ride_options)):
        Dog.append(Ride_options[i][0])
        
    st.write(f"Shortest route: {st.session_state.shortest_route}")

    for impact in range(len(st.session_state.route_impact)):
      
      components.html(
        f"""
            <div style="background-color: #fff; font-family: sans-serif; padding: 10px 20px; border-radius: 5px; height: 100%; margin: 0;">
              <h1>{Dog[impact].replace("_", " ")}</h1>
              <div style="opacity: 0.8; line-height: 0.4;">
                  <p>{st.session_state.route_impact[impact]}g of Carbon emissions</p>
                  <p>{st.session_state.route_distance} kilometers for your journey</p>
                  <p>The price for your journey: {st.session_state.route_distance * 0.5}$</p>
              </div>
            </div>
        """, height=212)
    st.selectbox('Choose a model', Dog, on_change=ride, key='model')
elif(st.session_state.button_click2):
    final()
    
    def reset():
      st.experimental_rerun()
    
    components.html(
        f"""
            <div style="background-color: #90EE90;">
              <h2>{st.session_state.model_response}</h2>
              <p>{st.session_state.route_impact[route_impact_model()]}g of Carbon emissions</p>
              <p>{st.session_state.route_distance} kilometers for your journey</p>
              <p>The price for your journey: {st.session_state.route_distance * 0.5}$</p>
            </div>
        """)
    st.button("Re-request a ride!", on_click=reset)
else: 
    home()