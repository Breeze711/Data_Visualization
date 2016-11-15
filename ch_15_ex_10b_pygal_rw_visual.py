import pygal
from pygal.style import LightSolarizedStyle

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    #Make a random walk and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    xy_chart = pygal.XY(height=10, width=6, stroke=True,
                        style=LightSolarizedStyle)                  
    xy_chart.title = 'Random Walk'
    xy_chart.add('rw.x_values', 'rw.y_values', show_dots=True, dot_size=4,
             stroke_style={'width':5})
    xy_chart.render(show_legend=True, human_readable=True, fill=True)    
                 
    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break

xy_chart.render_to_file('pygal_rw_visual.svg')

