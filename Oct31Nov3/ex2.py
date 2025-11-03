def show_x_plus_2(x):
    global my_var
    y = x + 2
    print("Function shows:", y, "and my_var is", my_var)
    my_var = 15
    return y


my_var = -128
show_x_plus_2(10)
print("Main program shows:", y + my_var)
