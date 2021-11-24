'''
This web service extends the Alphavantage api by creating a visualization module, 
converting json query results retuned from the api into charts and other graphics. 

This is where you should add your code to function query the api
'''
import requests
from datetime import datetime
from datetime import date
import pygal


#Helper function for converting date
def convert_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()

#function to render graph in browser
def render_graph(data, inputs):
  # Created arrays to hold data
  dates = []
  open_data = []
  high_data = []
  low_data = []
  close_data = []

  # Looped through the data and added values to arrays
  for x in data:
    dates.append(x)
    open_data.append(float(data[x]['1. open']))
    high_data.append(float(data[x]['2. high']))
    low_data.append(float(data[x]['3. low']))
    close_data.append(float(data[x]['4. close']))

  # Reversed the arrays so they are in ascending order
  dates.reverse()
  open_data.reverse()
  high_data.reverse()
  low_data.reverse()
  close_data.reverse()

  # Selected Graph Type based of the Inputs array from user_input.py
  if(inputs["graph_type"].upper() == "BAR"):
    line_chart = pygal.Bar()
  elif(inputs["graph_type"].upper() == "LINE"):
    line_chart = pygal.Line()
  else:
    print("Invalid graph choice")

  # Added Data to Chart and Rendered Graph in browser
  line_chart.title = "Stock Prices for $" + inputs['stock_symbol']
  line_chart.x_labels = map(str, dates)
  line_chart.add('Open', open_data)
  line_chart.add('High', high_data)
  line_chart.add('Low', low_data)
  line_chart.add('Close', close_data)
  line_chart.render_in_browser()
  return

