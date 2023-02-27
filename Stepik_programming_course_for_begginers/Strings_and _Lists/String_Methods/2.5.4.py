r, g, b = int(input()), int(input()), int(input())
print(f'#{hex(r).replace("0x", "0").upper() if 0 <= r < 16 else (hex(r)).strip("0x").upper()}{hex(g).replace("0x", "0").upper() if 0 <= g < 16 else (hex(g)).strip("0x").upper()}{hex(b).replace("0x", "0").upper() if 0 <= b < 16 else (hex(b)).strip("0x").upper()}')
