#Anyways. 
#this is a program to compute the percent change of emissions and to display it in a way 
# that is #engaging 

#it is a program designed to be used in Dash. Run in terminal as python methane.py 

import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go
import dash_daq as daq
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

em = pd.read_csv('emissions.csv') #spreadsheet data
available_counties = em['county'].unique() #this is to parse how many counties we have from the uploaded file
available_states = em['state'].unique()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children = [
    
    html.Div(children = [
        html.H1(children='Methane Changes in the San Juan Basin',
                style = {'display' : 'inline',
                         'float' : 'left',
                         'font-size': '3.0em',
                         'margin-left': '7px',
                         'font-weight': 'bolder',
                         'font-family': 'Gill Sans',
                         'color': "#A1D078",
                         'margin-top': '20px',
                           'margin-bottom': '0'
    
                         
                         
                         }
                ),  #title  
        html.Img(src="https://www.sanjuancitizens.org/wp-content/uploads/2019/06/SJCA-Logo-Name-Color.png",
                        style={
                            'height': '200px',
                            'float': 'right', 
                            'margin-right': '20px'
                        },
                ),    #SJCA Logo    
    
    ]),
    
            
             
            
    
    
    html.Div(children= 'Pick a state and a county in the San Juan Basin',
             style = {'display' : 'inline',
                      'textAlign':'left',
                      'float' : 'left',
                      'font-size': '2.2em',
                      'margin-left': '7px',
                      'font-weight': 'bold',
                      'font-family': 'Gill Sans',
                      'color': "#007F8D",
                      'margin-top': '100px',
                        'margin-bottom': '0'    
                        }
                      ),   #subtitle   
    
    #html.Div([
        #dcc.Dropdown(
            #id = 'select-state',
            #options = [{'label' : i, 'value' : i} for i in available_states],
            #value = 'Colorado'
        #)    
    
    
    #]),
    
    html.Div([
        
        
        
    dcc.Dropdown(
        id='select-county', #this is the ID of the drop down. We will use it later as an output of the program during the call back
        options = [{'label': i , 'value': i} for i in available_counties],
        
        value='La Plata'
    )
    ],
        style = {'width': '48%'}         
        ),
    
    #html.Div(id = 'output')
    html.Div([
         dcc.Graph(id = 'methane-by-county') #this is the bar graph that shows the difference in methane by year
    
    ], style = {'display':'inline-block', 'width' : '49%', 'padding' : '0 20'}), 
    
    html.Div([
        dcc.Graph(id = 'car-graph'),
        dcc.Graph(id = 'not-sure'),
    ], style={'display': 'inline-block', 'width': '49%'})
             
   
    
    
    ])

@app.callback(
    dash.dependencies.Output('methane-by-county', 'figure'),
    [dash.dependencies.Input('select-county', 'value')])

def update_figure(selected_county):
   #return 'You have selected "{}"'.format(value)
    methane = em[em['gas'] == 'CH4'] #this extracts the methane data from the spreadsheet
    traces = []
    yrs = [str(' 2014'),str(' 2018')]  
    
    filtered_counties = methane[methane.county == selected_county]
    
    #for i in filtered_counties:
        
    traces.append(go.Bar(
        x = [str('2014 (Measured) '), str('2018 (Projected) ')],
        y = filtered_counties['tons']
        #width = [1,1]
            
        
        
        ))
        
    return {
        'data' : traces,
        'layout' : go.Layout(
            xaxis = {'title' : 'Year'},
            yaxis = {'title' : 'Tons of Methane Emitted'},
            #title = {"Methane Emissions"},
            margin={'l': 60, 'b': 40, 't': 1, 'r': 10},
            height = 800
        
        )
    }

#@app.callback(dash.dependencies.Output('car-graph', 'figure'),
              #[dash.dependencies.Input('select-county', 'value')])
    



if __name__ == '__main__':
    app.run_server(debug=True)