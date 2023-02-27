import math

l, w, h = map(int, input().split())
print(math.ceil(((l + w) * h) / 8))
