from bokeh.plotting import figure, output_file, show

list = [12 ,5, 5,3,2, 2,523,523,2,32,1,15152, 5]
print(len(list) - list[::-1].index(1) - 1)
