def from_hex_to_rgb(color: str) -> tuple:
    s16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    r = []
    for i in color[1:]:
        r.append(s16.index(i))
    red = r[0] * 16 + r[1]
    green = r[2] * 16 + r[3]
    blue = r[4] * 16 + r[5]
    return red, green, blue


colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A',
          '#FA8072', '#FFA07A', '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#B8860B', '#DAA520',
          '#EEE8AA', '#BDB76B', '#F0E68C', '#808000', '#FFFF00', '#9ACD32', '#556B2F', '#6B8E23',
          '#7CFC00', '#7FFF00', '#ADFF2F']

for red, green, blue in map(from_hex_to_rgb, colors):
    print(f"Red={red}, Green={green}, Blue={blue}")
