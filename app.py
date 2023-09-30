import streamlit as st
from home import main as home, st
from final import main as final
from route import main as route
from login import main as login
from layout import connections, Ride_options
import streamlit.components.v1 as components
import sqlite3
def main():
    if 'ride_history' not in st.session_state:
        st.session_state.ride_history = []

    total_carbon_emissions = 0
    total_distance = 0
    
    for entry in st.session_state.ride_history:
        carbon_emissions = entry["carbon_emissions"]
        distance = entry["distance"]
        total_carbon_emissions += carbon_emissions
        total_distance += distance

    Ride_options_only=[]
    for i in range(len(Ride_options)):
        Ride_options_only.append(Ride_options[i][0])
            
    def route_price(distance, model):
        match model:
            case "Uber_Green":
                return distance * 1
            case "UberX_Share":
                return distance*0.25
            case "UberXL":
                return distance*0.5
            case "Uber_Comfort":
                return distance * 2
            case "Uber_WAV":
                return distance * 1.5
            case _:
                return 0
    
    if 'model_response' not in st.session_state:
            st.session_state.model_response = ''

    def back_home():
        st.session_state.location, st.session_state.destination = "Choose a location", "Choose a location"
        st.session_state.location_response, st.session_state.destination_response = "", ""


        st.session_state.button_click1 = False
        st.session_state.button_click2 = False
        st.session_state.button_click3 = False
        

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
    
    if 'button_click3' not in st.session_state:
        st.session_state.button_click3 = True
        
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
        
            
        st.write(f"Shortest route: {st.session_state.shortest_route}")

        for impact in range(len(st.session_state.route_impact)):    
            components.html(
                f"""
                    <div style="background-color: #fff; font-family: sans-serif; padding: 10px 20px; border-radius: 5px; height: 100%; margin: 0;">
                    <h1>{Ride_options_only[impact].replace("_", " ")}</h1>
                    <div style="opacity: 0.8; line-height: 0.4;">
                        <p>{st.session_state.route_impact[impact]}g of Carbon emissions</p>
                        <p>{st.session_state.route_distance} kilometers for your journey</p>
                        <p>The price for your journey: {route_price(st.session_state.route_distance, Ride_options_only[impact])}$</p>
                    </div>
                    </div>
                """, height=212)
        Ride_options_only.insert(0, "Choose a model")
        st.selectbox(' ', Ride_options_only, key='model')
        st.button("Book ride!", on_click=ride)
    elif(st.session_state.button_click2):
        final()

        st.session_state.ride_history.append({
            'location': st.session_state.location_response.removeprefix("You selected: "),
            'destination': st.session_state.destination_response.removeprefix("You selected: "),
            'carbon_emissions': st.session_state.route_impact[route_impact_model()],
            'distance': st.session_state.route_distance,
            'price': route_price(st.session_state.route_distance, st.session_state.model_response),
            'model': st.session_state.model_response.replace("_", " ")
        })      

        components.html(
            f"""
                <div style="background-color: #fff; font-family: sans-serif; padding: 10px 20px; border-radius: 5px; height: 100%; margin: 0;">
                <h1>{st.session_state.model_response.replace("_", " ")}</h1>
                <div style="opacity: 0.8; line-height: 0.4;">
                    <p>{st.session_state.route_impact[route_impact_model()]}g of Carbon emissions</p>
                    <p>{st.session_state.route_distance} kilometers for your journey</p>
                    <p>The price for your journey: {route_price(st.session_state.route_distance, st.session_state.model_response)}$</p>
                </div>
                </div>
            """, height=212)
        st.button("Back to Home", on_click=back_home)
    elif(st.session_state.button_click3):
        login()
    else: 
        home()
        st.write('''# Stats:''')
        components.html(
        f"""
            <div style="background-color: #fff; font-family: sans-serif; padding: 10px 20px; border-radius: 5px; height: 100%; margin: 0;">
                <div style="opacity: 0.8; line-height: 0.4;">
                    <p>{total_carbon_emissions}g total Carbon emissions</p>
                    <p>{total_distance}km total distance</p>
                </div>
            </div>
        """, height=90)
        st.write('''# Your Ride History:''')
        if st.session_state.ride_history:   
            for item in st.session_state.ride_history:
                components.html(
                f"""
                    <div style="background-color: #fff; font-family: sans-serif; padding: 10px 20px; border-radius: 5px; height: 100%; margin: 0;">
                        <h1>{item['model']}</h1>
                        <h2>{item['location']} --> {item['destination']}</h2>
                        <div style="opacity: 0.8; line-height: 0.4;">
                            <p>{item['carbon_emissions']}g of Carbon emissions</p>
                            <p>{item['distance']} kilometers for your journey</p>
                            <p>The price for your journey: {item['price']}$</p>
                        </div>
                    </div>
                """, height=242)
        else:
            st.write("You have not ridden anywhere yet")
       
    

if __name__ == '__main__':
    main()