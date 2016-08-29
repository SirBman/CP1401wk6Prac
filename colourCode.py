"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
colourCodes = {"blue1": "#0000ff", "black": "#000000","cyan1": "#00ffff","gray41": "#696969","goldenrod1": "#ffc125","magenta": "#ff00ff","pink": "#ffc0cb","red1": "#ff0000","violet": "#ee82ee"}
print(colourCodes.keys())

colourIn = str(input("Please enter the colour you want the code for: "))


if colourIn in colourCodes:
    print(colourIn + "'s hex code is {}.".format(colourCodes[colourIn]))


