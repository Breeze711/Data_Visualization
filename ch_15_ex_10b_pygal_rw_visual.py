import pygal
from pygal.style import LightSolarizedStyle
from random import choice


xy_chart = pygal.XY(height=10, width=6, stroke=True,
                    style=LightSolarizedStyle, show_legend=True,
                    human_readable=True, fill=True, show_dots=True,
                    dot_size=4)                  
xy_chart.title = 'Random Walk'
xy_chart.x_labels = map(str, range(-2, 6))
xy_chart.y_labels = map(str, range(-2, 6))
xy_chart.add('x = choice(x)', [choice((-1, 1)) for x in range(0, 5)])
xy_chart.add('x = num_points(x)', [num_points((50))])
xy_chart.add('y = choice(y)', [choice((-1, 1)) for y in range(0, 5)])
xy_chart.add('y = num_points(y)', [num_points((50))])                                   
xy_chart.render_to_file('tues_test.svg')   



