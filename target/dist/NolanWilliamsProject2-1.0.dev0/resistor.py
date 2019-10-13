

resistor_colors = { 'black': {'digit': 0, 'multiplier': 1},
                    'brown': {'digit': 1, 'multiplier': 10, 'tolerance': 1},
                    'red': {'digit': 2, 'multiplier': 100, 'tolerance': 2},
                    'orange': {'digit': 3, 'multiplier': 1000},
                    'yellow': {'digit': 4, 'multiplier': 10000},
                    'green': {'digit': 5, 'multiplier': 100000, 'tolerance': 0.5},
                    'blue': {'digit': 6, 'multiplier': 1000000, 'tolerance': 0.25},
                    'violet': {'digit': 7, 'multiplier': 10000000, 'tolerance': 0.1},
                    'grey': {'digit': 8, 'multiplier': 100000000, 'tolerance': 0.05},
                    'white': {'digit': 9, 'multiplier': 1000000000},
                    'gold': {'multiplier': 0.1, 'tolerance': 5},
                    'silver': {'multiplier': 0.01, 'tolerance': 10},
                    'none': {'multiplier': 1, 'tolerance': 20}    
                }


def validateColorsList(colors):
    
    if len(colors) < 4 | len(colors) > 5:
        raise ValueError('There should only be 4 or 5 bands')
    
    for color in colors:
        if color not in resistor_colors:
            raise ValueError('%s is not a valid resistor color band' % (color))
    
    
        
    