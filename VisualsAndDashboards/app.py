import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
	html.H1("Hello Dash"),
    	html.Div("Dash: A web application framework for Python."),
    	])

if __name__ == '__main__': 
	app.run(debug=True)

#Read more here: https://locall.host/localhost-dash/
