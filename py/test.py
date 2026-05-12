x = [1,2,[3,4],5]
print(x[2][0])  # Output: 3
y=x
y=[2][0] = 99
print(y)  # Output: [1, 2, [99, 4], 5]


