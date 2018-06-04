# Data_Visualization
Project two from 'Python Crash Course' by Eric Matthes

This project involves data visualization. I tend to use chart and graph interchangeably in my description below.

Exercise 15-10, practicing with both libraries: Try using matplotlib to make a die-rolling visualization, and use Pygal to make the visualization for a random walk. I'm calling the matplotlib exercise 15-10a and the Pygal problem 15-10b. I've included my notes for how to lay out 15-10a, as well as the graph and the die class that Eric Matthes demonstrated in the book. 

For 15-10b, I could not get a random walk chart to 'go' in Pygal, so I created an xy chart that would go!  

One error I kept running into was a memory error that would prevent any graph I tried to render from going. I learned that this error could be due to having a 32 bit version of Python on an operating system that is 64 bit. Sure enough, once I uninstalled the 32 bit version of Python 3.5.2 from both of my computers and installed the 64 bit version, the memory error removed itself. 

Then I had a new error: 'This XML file does not appear to have any style information associated with it. The document tree is shown below.' This was due to how I was trying to set up my chart height and width, which I attempted to do like this:
xy_chart = pygal.XY(height=10, width=6)

Once I changed things to this:
HEIGHT = 600
WIDTH = 600
xy_chart = pygal.XY(height=HEIGHT, width=WIDTH)

Voila! I got a chart. 

In chapter 16, I'm downloading data sets and creating charts and graphs from the data. The first part of chapter 16 involves working with csv files, graphing out high and low temperatures for different citiess. In ch_16_ex_16-1, I downloaded weather info for San Francisco, CA for 2014 in a csv file and converted some of the data into a chart(graph) that shows high and low temperatures. 

In ch_16_ex_16_2, I integrated two previous charts (Sitka, AK and Death Valley, CA) I did during the book exercises in an attempt to directly compare/contrast the temperature ranges. 
