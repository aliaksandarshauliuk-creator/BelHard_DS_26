#  check weather a value can be converted into positive float or integer number
def is_valid_side_val(val):
    try:
        number = float(val)
        return number > 0
    except ValueError:
        return False

#  instructions to give valid rectangle side from inputs
#  side should be numeric and greater than 0
def get_rectangle_side(side_name):
    side_val = input(f'Enter {side_name} of rectangle in centimeters: ')

    while not is_valid_side_val(side_val):
        side_val = input(f'Please enter valid {side_name} of rectangle in centimeters: ')

    #  numeric string is converted into integer number
    #  string that contains dot symbol is converted into float number
    return int(side_val) if side_val.isnumeric() else float(side_val)

length = get_rectangle_side('length')
width = get_rectangle_side('width')

def calculate_area (length_val, width_val):
    square = length_val * width_val
    return square

print(f'The area of a rectangle equals {calculate_area(length,width)} square centimeters')
