from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
mp = (max(one) + max(two) +max(three)) / 2
mip = (min(one) + min(two) +min(three)) / 2
max_square = sqrt(mp * (mp - max(one)) * (mp - max(two)) * (mp - max(three)))
min_square = sqrt(mip * (mip - min(one)) * (mip - min(two)) * (mip - min(three)))
print(max_square)
print(min_square)