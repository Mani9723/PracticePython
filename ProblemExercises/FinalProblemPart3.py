"""
  In this exercise, 
  use the bokeh Python library to plot a histogram 
  of which months the scientists have birthdays in.
"""

from bokeh.plotting import figure, show, output_file
from FinalProblemPart2 import getNumberOfOccurences
from calendar import month_name

output_file("C:/Users/Home/Desktop/graph.html")

x,y,monthName,c = [],[],[],[]

for k,v in getNumberOfOccurences().items():
    x.append(k)
    y.append(v)

for name in range(1,13,1):
    c.append(month_name[name])
x_categories = c

#p = figure(x_range=x_categories)
p = figure(plot_width=1000, plot_height=600, title="\t\tFrequency of Birthdays",x_range = x_categories)
p.vbar(x=x, top=y, width=0.4)
p.xaxis.axis_label = "M o n t h s"
p.xaxis.axis_line_width = 3
p.xaxis.axis_line_color = "red"

# change just some things about the y-axes
p.yaxis.axis_label = "N u m b e r  o f  B i r t h d a y s"
p.yaxis.major_label_text_color = "black"
p.yaxis.major_label_orientation = "vertical"
show(p)
