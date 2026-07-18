"""Colors"""

mixcl = {
    ("Red", "Yellow"): "Orange",
    ("Red", "Blue"): "Violet",
    ("Yellow", "Blue"): "Green",

    ("Yellow", "Red"): "Orange",
    ("Blue", "Red"): "Violet",
    ("Blue", "Yellow"): "Green"
}

color1 = input().strip().capitalize()
color2 = input().strip().capitalize()

cl = color1,color2

if color2 == color1 and color1 in {"Red", "Yellow", "Blue"}:
    print(color1)
else:
    print(mixcl.get(cl, "Error"))
