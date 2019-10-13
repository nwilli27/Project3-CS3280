

resistor_colors = { 'black':  {'digit': 0, 'multiplier': {'number': 1} },
                    'brown':  {'digit': 1, 'multiplier': {'number': 10},                  'tolerance': 1},
                    'red':    {'digit': 2, 'multiplier': {'number': 100},                 'tolerance': 2},
                    'orange': {'digit': 3, 'multiplier': {'number': 1,   'prefix': "K"} },
                    'yellow': {'digit': 4, 'multiplier': {'number': 10,  'prefix': "K"} },
                    'green':  {'digit': 5, 'multiplier': {'number': 100, 'prefix': "K"},  'tolerance': 0.5},
                    'blue':   {'digit': 6, 'multiplier': {'number': 1,   'prefix': "M"},  'tolerance': 0.25},
                    'violet': {'digit': 7, 'multiplier': {'number': 10,  'prefix': "M"},  'tolerance': 0.1},
                    'grey':   {'digit': 8, 'multiplier': {'number': 100, 'prefix': "M"},  'tolerance': 0.05},
                    'white':  {'digit': 9, 'multiplier': {'number': 1,   'prefix': "G"} },
                    'gold':   {            'multiplier': {'number': 0.1},                 'tolerance': 5},
                    'silver': {            'multiplier': {'number': 0.01},                'tolerance': 10},
                    'none':   {            'multiplier': {'number': 0},                   'tolerance': 20}    
                }

# Validates the list of color bands to meet the conditions of a valid resistor.
def validateColorsList(colors):
    
    if len(colors) < 4 | len(colors) > 5:
        raise ValueError('There should only be 4 or 5 bands')
    
    for color in colors:
        if color not in resistor_colors:
            raise ValueError('%s is not a valid resistor color band' % (color))
    
  
#
def decodeTolerance(colors):
    
    last_band = colors[-1]
    return resistor_colors[last_band]["tolerance"]
    


  
    
print(resistor_colors["green"]["multiplier"]["number"])      
    