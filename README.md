<style>
    @keyframes background-pan {
      from {
        background-position: 0% center;
      }
    
      to {
        background-position: -200% center;
      }
    }

    h1 {
        font-weight: 400;
        letter-spacing: .5px
    }

    .project-name {
        background: linear-gradient(
            to right,
            #bda2fc,
            #c989f4,
            #9489f4,
            #bda2fc
        );
        animation: background-pan 3s linear infinite;
        background-size: 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-right: 5px;
        font-weight: 700;
    }
</style>

<h1><span class="project-name">Public + Private</span> Overview</h1>

## Introduction

This code is a Python script that uses the Streamlit library to create a Public + Private transport integration app.

<hr>

 The app allows users to choose amongst different uber ride options. 
 It calculates the shortest route and carbon emissions for the journey. 
 The app also provides an estimated price for the journey.

## Dependencies

The code requires the following libraries to be installed using pip install [library_name]: 

- Streamlit
- networkx
- Streamlit components v1

## How to run the code

To run the code, open a terminal and navigate to the directory where the code is saved. Then, run the following command:
streamlit run app.py (If using zsh terminal)
python -m streamlit run app.py (If using bash terminal)

## Code structure

The code is structured as follows:
The first few lines import the necessary libraries and define some variables and functions.

## App.py

The first function thats run is an if else statement. The code checks if the `button_click1` variable is `True`.

If it is, the `route()` function is called to calculate the shortest route, and the results are displayed using HTML components.

If the `button_click2` variable is `True`, the `final()` function is called to calculate the carbon emissions and estimated price for the journey, and the results are displayed using HTML components.

If neither variable is True, the `home()` function is called to display the home screen of the app.

<hr>

At the start of the code both button clicks are set to **False**, therefore the home page is run.

Refer to line 52 for explanation of home.py
At the end of home.py a "Request to ride" button is clicked. 

This click is stored in the sesion variable `st.session_state.button_click1` and is set to `True`.
Since this variable is now set to true the if statement mentioned previously is now run. On running, the first if statement value returns true and therefore runs the function "`route`".

The page route.py dosent neccesarily have any meaningful code in it except for a `st.write `statement giving a title for the page. 

On app.py we display multiple variables:

- An empty list is created to store values for different ride options.
- A for loop is run appending all ride option values in the `Ride_options_only `list
- A `st.write` statement is called that displays the `st.session_state.shortest_route` variable displaying the shortest route between two nodes (or locations for the apps purpose)
- then another for loop that runs a `components.html` expression dispalying a card-like UI for each model with details such as carbon emitted from the car, price and total distance for the route.
- after the for loop a selectbox is shown for the model the user wants to choose and a request ride button that confirms the choice

<hr>

on the click of the button a `ride` function is called:
- the `ride` function checks for the model the user has chosen and saves that into a `st.session_state.model_reponse` variable which is used to render the details for the users journey on the final page.
T hen the function sets the first button click(used to render route) and sets st.`session_state.button_click2` to True.
After this the function "final" is run.

- The route.py page has only a `st.write `statement that displays the title "Your ride details:"
- below the app.py page renders a styled html component that displays the users final ride model, journey carbon emissions, price and distance.

## Other functions in app.py

- `route_impact_model` gets the index of the model the user has chosen. This is used to find the chosen option in the array `Ride_options_only`, and display it to the user.
- Line 23-36 ivolves intializing session_state variables to be used later in the code.

## Home.py

The home page starts off with importing the neccesary libraries and functions

```py
import streamlit as st
from layout import get_layout, get_shortest_path, graph, locations, get_route_impact, get_route_distance
```

`get_layout` function draws out the map created for UberLand.
options list for the selectbox (for user destination and location) is set with the keys from `locations`

The `location_response` session varaible is set, a function location is defined which writes out the location the user has picked using the value taken from the selectbox initialized on the next line.

A `st.empty` is written to create an empty space for aesthetic purposes.

The `destitnation_response` session varaible is set, a function `destination` is defined which writes out the destination the user has picked using the value taken from the selectbox initialized on the next line.

a `wait` function is defined which is set to be called after the `request a ride` button is clicked. It involves:
a statement checking if both selectboxes have been set to different locations and not "choose a location" or the same one.
`shortest_path` variable is defined which gets the shortest path from the location to the destination with the function `get_shortest_path` defined in layout.py
the carbon emissions associated with the route and the distance of the route are also set to the variables `st.session_state.route_impact` and
`st.session_state.route_distance `respectively. these values are aquired form functions `get_route_impact` and `get_route_distance` which are defined in layout.py

Lastly, the `st.session_state.button_click1` is set to `True`. which renders the route function as explained previously

## Layout.py

Layout.py includes an array of locations that are present within UberLand. Their positions are defined within a `matplotlib` graph, using Cartesian coordinates.

The locations are plotted on the graph and a getter function passes on the `st.pyplot` function that displays the graph to the user.

Here, the different models of cars that the user can take are defined as well.

In addition to constant variables, a variety of useful helper functions are defined here. Namely, `get_route_distance` which gets the distance in kilometers for any given route:

```py
def get_route_distance(a, b):
    """Get the distance/weight between location A and location B 
    Returns the total sum of distance/weight"""
    path = get_shortest_path(graph, a, b)
    sum = 0
    for i in range(len(path) - 1):
        n1, n2 = path[i:i+2]
        sum += get_branch_distance(n1, n2)
    return sum
```