

resistor_colors = { 'black':  {            'multiplier': {'number': 1,    'prefix': "" } },
                    'brown':  {'digit': 1, 'multiplier': {'number': 10,   'prefix': "" },  'tolerance': 1},
                    'red':    {'digit': 2, 'multiplier': {'number': 100,  'prefix': "" },  'tolerance': 2},
                    'orange': {'digit': 3, 'multiplier': {'number': 1,    'prefix': "K"} },
                    'yellow': {'digit': 4, 'multiplier': {'number': 10,   'prefix': "K"} },
                    'green':  {'digit': 5, 'multiplier': {'number': 100,  'prefix': "K"},  'tolerance': 0.5},
                    'blue':   {'digit': 6, 'multiplier': {'number': 1,    'prefix': "M"},  'tolerance': 0.25},
                    'violet': {'digit': 7, 'multiplier': {'number': 10,   'prefix': "M"},  'tolerance': 0.1},
                    'grey':   {'digit': 8, 'multiplier': {'number': 100,  'prefix': "M"},  'tolerance': 0.05},
                    'white':  {'digit': 9, 'multiplier': {'number': 1,    'prefix': "G"} },
                    'gold':   {            'multiplier': {'number': 0.1,  'prefix': "" },  'tolerance': 5},
                    'silver': {            'multiplier': {'number': 0.01, 'prefix': "" },  'tolerance': 10},
                    'none':   {                                                            'tolerance': 20}   
                }


# Validates the list of color bands to meet the conditions of a valid resistor.
def validateColorsList(colors):
    
    if len(colors) < 4 or len(colors) > 5:
        raise ValueError('There should only be 4 or 5 bands')
    
    for color in colors:
        if color not in resistor_colors:
            raise ValueError('%s is not a valid resistor color band' % (color))
        
    for color in colors[0:-2]:
        if 'digit' not in resistor_colors[color]:
            raise ValueError('%s does not contain a significant figure digit' % (color))

    if 'multiplier' not in resistor_colors[colors[-2]]:
        raise ValueError('%s does not contain a multiplier' % (colors[-2]))
        
    if 'tolerance' not in resistor_colors[colors[-1]]:
        raise ValueError('%s does not contain a tolerance value' % (colors[-1]))
    
  
# Returns the tolerance of the last band in [colors].
def decodeTolerance(colors):
    
    last_band = colors[-1]
    return resistor_colors[last_band]["tolerance"]
  
    
# Returns a tuple of number, prefix for the multiplier in [colors].
def decodeMultiplier(colors):
    
    multiplier_band = colors[-2]
    number = resistor_colors[multiplier_band]["multiplier"]["number"]
    prefix = resistor_colors[multiplier_band]["multiplier"]["prefix"]
        
    return number, prefix
  
    
# Returns a string of all significant figures in [colors] combined together.
def decodeSignificantFigures(colors):
    
    significant_bands = colors[0:-2]   
    number = '';
    for color in significant_bands:
        number += str(resistor_colors[color]['digit'])
    
    return number


# Returns a formatted Resistance string of [colors] list of bands.
def createFormattedResistanceString(colors):
    
    significant_figures = decodeSignificantFigures(colors)
    multiplier = decodeMultiplier(colors)
    resistance_value = int(significant_figures) * multiplier[0]
    multiplier_prefix = multiplier[1]
    tolerance = decodeTolerance(colors)
    
    formatted_resistance = "{} {}ohms +/- {}%".format(resistance_value, multiplier_prefix, tolerance)
    return formatted_resistance


# Returns a dictionary(value, units, tolerance, formatted) for the [colors] list of bands.
def decodeResistance(colors):
    
    resistance = {}
    significant_figures = decodeSignificantFigures(colors)
    multiplier = decodeMultiplier(colors)
    
    resistance['value'] = int(significant_figures) * multiplier[0]
    resistance['units'] = multiplier[1] + "ohms"
    resistance['tolerance'] = decodeTolerance(colors)
    resistance['formatted'] = createFormattedResistanceString(colors)

    return resistance