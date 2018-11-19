
    # Create visualiation
    total_houses = 20
    grid = Grid(180, 160)
    print('---------------------------------------------------')
    print(comparisons[8])
    grid.create_little_house(SingleHome(total_houses, 8, 8, 285000, 2), comparisons[8])
    x = Visualator(grid.grid, SingleHome(total_houses, 8, 8, 285000, 2), Bungalow(total_houses, 10, 7.5, 399000), Maison(total_houses, 11, 10.5, 610000))
    show(x.bokeh())
