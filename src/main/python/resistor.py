
valid_colors = ["black", "brown", "red", "orange", "yellow", "green",
                "blue", "violet", "grey", "white", "gold", "silver", "none"]

def validateColorsList(colors):
    
    if len(colors) < 4 | len(colors) > 5:
        raise ValueError('There should only be 4 or 5 bands')
    
    for color in colors:
        if color not in valid_colors:
            raise ValueError('%s is not a valid resistor color' % (color))