from bokeh.plotting import figure, output_file, show

l = 123
a = list(range(1, l//2))
b = [l*(l-2*i)/(2*(l-i)) for i in a]

output_file("problem75_plots.html")

p = figure(
   tools="resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select,save",
   y_axis_type="log", y_range=[0.001, 10**11], title="Proj.Euler plots",
   x_axis_label='a', y_axis_label='f(a)'
)

p.line(a, b, legend="f(a)")

show(p)
