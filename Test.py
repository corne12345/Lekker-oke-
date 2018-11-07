from bokeh.plotting import figure, output_file, show

list = [1 ,5, 5,3,2, 2,523,523,2,32,15152, 5]
x_axis= list.index(list[-1])
last_x_value = None
for c, values in enumerate(list):
    last_x_value = [c, values]

print(last_x_value)
print(x_axis)
