import streamlit as st
from home import main as home, st
from final import main as final
from route import main as route
from layout import connections, Ride_options
import streamlit.components.v1 as components

if 'model_response' not in st.session_state:
        st.session_state.model_response = ''

def ride():                                         # function to redirect user to final page from route page.
    if st.session_state.model == "Choose a model": 
        st.session_state.model_response = ""
    else:
        st.session_state.model_response = st.session_state.model
        st.session_state.button_click1 = False
        st.session_state.button_click2 = True
        
        
#initializing session state variables
        
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
    
    
def route_impact_model():   # looping through ride options to find the ride option chosen and getting the index of it.
  for i in range(len(Ride_options)):
    if Ride_options[i][0] == st.session_state.model_response:
          return i
  

if (st.session_state.button_click1):
    route()
    Ride_options_only=[]
    for i in range(len(Ride_options)):
        Ride_options_only.append(Ride_options[i][0]) #using a for loop to make a list of ride options only since the original list contains the weight values as well
        
    st.write(f"Shortest route: {st.session_state.shortest_route}")

    for impact in range(len(st.session_state.route_impact)):
      
      components.html( # displaying the carbon emissions, route distance and price for each ride option.
        f"""
            <div style="background-color: #fff; font-family: sans-serif; padding: 10px 20px; border-radius: 5px; height: 100%; margin: 0;">
              <h1>{Ride_options_only[impact].replace("_", " ")}</h1>
              <div style="opacity: 0.8; line-height: 0.4;">
                  <p>{st.session_state.route_impact[impact]}g of Carbon emissions</p>
                  <p>{st.session_state.route_distance} kilometers for your journey</p>
                  <p>The price for your journey: {st.session_state.route_distance * 0.5}$</p>
              </div>
            </div>
        """, height=212)
    Ride_options_only.insert(0, "Choose a model")
    st.selectbox(' ', Ride_options_only, key='model')
    st.button("Book ride!", on_click=ride) #on click calls ride function that redirects user to final page
elif(st.session_state.button_click2):
    final()
    
    components.html( #displays the user final journey details based on the option they chose
        f"""
            <div style="background-color: #fff; font-family: sans-serif; padding: 10px 20px; border-radius: 5px; height: 100%; margin: 0;">
              <h1>{st.session_state.model_response.replace("_", " ")}</h1>
              <div style="opacity: 0.8; line-height: 0.4;">
                  <p>{st.session_state.route_impact[route_impact_model()]}g of Carbon emissions</p>
                  <p>{st.session_state.route_distance} kilometers for your journey</p>
                  <p>The price for your journey: {st.session_state.route_distance * 0.5}$</p>
              </div>
            </div>
        """, height=212)
else: 
    home() #displaying home page at the start if both session state buttons are set as false.