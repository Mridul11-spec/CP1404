hex_colors = {"aliceblue": "#f0f8ff", "blanchedalmond": "#ffebcd", "blue": "#0000ff", "brown": "#a52a2a",
              "coral": "#ff7f50", "cyan": "#00ffff", "darkgreen": "#006400", "darkorange": "#ff8c00",
              "darkviolet": "#9400d3", "gold": "#ffd700", "gray": "#bebebe", "hotpink": "#ff69b4"}

colors = str(input("What color do you like: \n >>>"))

while colors.lower() != "":
    if colors.lower() in hex_colors:
        print("{} is {}".format(colors, hex_colors[colors.lower()]))
    else:
        print("Invalid color / Color doesn't included")
    colors = str(input("What color do you like: \n >>>"))