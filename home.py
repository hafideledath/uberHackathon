import streamlit as st
from layout import get_layout, get_shortest_path, graph, locations, get_route_impact, get_route_distance

def main():
    get_layout()

    options = [
        'Choose a location', # making a list of all the locations
        *locations
    ]

    if 'location_response' not in st.session_state: #initializing the session state variable for location response
        st.session_state.location_response = ''

    def location(): #function to check for location chosen and display it 
        if st.session_state.location == "Choose a location": 
            st.session_state.location_response = ""
        else:
            st.session_state.location_response = f'You selected: {st.session_state.location}'

    st.selectbox('Where would you like to be picked up?', options, on_change=location, key='location')

    st.empty() #create an empty line similar to <br> tag in HTML
    st.write(st.session_state.location_response) #displaying the location to be picked up from

    if 'destination_response' not in st.session_state: #initializing the session state variable for destination response
        st.session_state.destination_response = ''

    def destination(): #function to check for destination chosen and display it 
        if st.session_state.destination == "Choose a location": 
            st.session_state.destination_response = ""
        else:
            st.session_state.destination_response = f'You selected: {st.session_state.destination}'

    st.selectbox('Where would you like to be dropped off?', options, on_change=destination, key='destination')

    st.write(st.session_state.destination_response) #displaying the destination to be dropped to

    def wait(): #checks that both destination and location are different values
        if st.session_state.location == st.session_state.destination or "Choose a location" in [st.session_state.location, st.session_state.destination]:
            return
        shortest_path = get_shortest_path(graph, st.session_state.location, st.session_state.destination) #inputs values into shortest path function to get the shortest path between nodes
        st.session_state.shortest_route = " -> ".join(shortest_path) # style the shortest path
        st.session_state.route_impact = get_route_impact(st.session_state.location, st.session_state.destination) #getting carbon emitted by each ride option for this journey
        st.session_state.route_distance = get_route_distance(st.session_state.location, st.session_state.destination) #getting total distance of journey
        st.session_state.button_click1 = True # on setting true user gets redirected to route page due to code in app.py

    st.button("Request a Ride", on_click=wait) # submit button calling wait function


if __name__ == '__main__':
    main()