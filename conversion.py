length = {
    "meters" : {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters" : 100,
        "inches": 39.3701,
        "feet" : 3.28084,
        "yards": 1.09361,
        "miles": 0.000621
    },

    "kilometers": {
        "meters": 1000,
        "kilometers": 1,
        "centimeters" : 100000,
        "inches": 39370,
        "feet" : 3281,
        "yards": 1094,
        "miles": 0.6214
    },

    "centimeters": {
        "meters": 0.01,
        "kilometers": 0.00001,
        "centimeters" : 1,
        "inches": 0.393701,
        "feet" : 0.0328084,
        "yards": 0.0109361,
        "miles": 0.00000621
    },
    "inches": {
        "meters": 0.0254,
        "kilometers": 0.0000254,
        "centimeters" : 2.54,
        "inches": 1,
        "feet" : 0.0833333,
        "yards": 0.0277778,
        "miles": 0.0000157
    },
    "feet": {
        "meters": 0.3048,
        "kilometers": 0.0003048,
        "centimeters" : 30.48,
        "inches": 12,
        "feet" : 1,
        "yards": 0.333333,
        "miles": 0.000189
    },
    "yards":{
        "meters": 0.9144,
        "kilometers": 0.0009144,
        "centimeters" : 91.44,
        "inches": 36,
        "feet" : 3,
        "yards": 1,
        "miles": 0.000568
    },
    "miles": {
        "meters": 1609.34,
        "kilometers": 1.609,
        "centimeters" : 160934,
        "inches": 63360,
        "feet" : 5280,
        "yards": 1760,
        "miles": 1

    }
}

mass = {
    "grams": {
        "grams": 1,
        "kilograms": 0.001,
        "pounds":0.0022,
        "ounces":0.035274
    },
    "kilograms":{
        "grams": 1000,
        "kilograms":1,
        "pounds": 2.20462,
        "ounces":35.274

    } ,
    "pounds": {
        "grams":453.592,
        "kilograms":0.453592,
        "pounds":1,
        "ounces": 16

    },
    "ounces": {
        "grams":28.3495,
        "kilograms":0.0283495,
        "pounds": 0.0625,
        "ounces": 1
    },
}

volume = {
    "liters": {
        "liters": 1,
        "gallons": 0.264172,
        "cubic meters": 0.001
    },
    "gallons": {
        "liters": 3.78541,
        "gallons":1,
        "cubic meters": 0.003785
    },
    "cubic meters": {
        "liters": 1000,
        "gallons":264.172,
        "cubic meters": 1
    }
}


###################### Functions to retrieve answers
#need to account for invalid token (0 infront)
def get_length_conversion(base, new, num):
    converter = length[base][new]
    result = float(num) * converter
    return round(result,3)

def get_mass_conversion(base,new,num):
    converter = mass[base][new]
    result = float(num) * converter
    return result

def get_volume_conversion(base,new,num):
    converter = volume[base][new]
    result = float(num) * converter
    return result