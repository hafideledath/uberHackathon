import streamlit as st
from layout import get_layout, get_shortest_path, graph, locations, get_route_impact, get_route_distance

def main():
    get_layout()

    options = [
        'Choose a location',
        *locations
    ]

    if 'location_response' not in st.session_state:
        st.session_state.location_response = ''

    def location():
        if st.session_state.location == "Choose a location": 
            st.session_state.location_response = ""
        else:
            st.session_state.location_response = f'You selected: {st.session_state.location}'

    st.selectbox('Where would you like to be picked up?', options, on_change=location, key='location')

    st.empty()
    st.write(st.session_state.location_response)

    if 'destination_response' not in st.session_state:
        st.session_state.destination_response = ''

    def destination():
        if st.session_state.destination == "Choose a location": 
            st.session_state.destination_response = ""
        else:
            st.session_state.destination_response = f'You selected: {st.session_state.destination}'

    st.selectbox('Where would you like to be dropped off?', options, on_change=destination, key='destination')

    st.write(st.session_state.destination_response)

    def wait():
        if st.session_state.location == st.session_state.destination or "Choose a location" in [st.session_state.location, st.session_state.destination]:
            return
        shortest_path = get_shortest_path(graph, st.session_state.location, st.session_state.destination)
        st.session_state.shortest_route = " -> ".join(shortest_path)
        st.session_state.route_impact = get_route_impact(st.session_state.location, st.session_state.destination)
        st.session_state.route_distance = get_route_distance(st.session_state.location, st.session_state.destination)
        st.session_state.button_click1 = True

    st.button("Request a Ride", on_click=wait)


if __name__ == '__main__':
    main()