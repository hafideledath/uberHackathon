import streamlit as st
from layout import get_layout, get_shortest_path, graph, locations, get_route_impact, get_route_distance
import streamlit.components.v1 as components

def main():
    components.html(f"""<div>
                            <nav style="color: #fff; display: flex; align-items: center; font-family: monospace; font-size: 1.5em; width: 100%; justify-content: space-between;">
                                <h4>UberLand P+P</h4>
                                <p>{st.session_state.total_points} points</p>
                            </nav>
                        </div>
                    """)
    
    map, inputs = st.columns(2)

    with map:
        get_layout()

    with inputs:
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