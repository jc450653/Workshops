lower = 10
upper = 100
str = "Enter a number  {} - {}:".format(lower, upper)
print(str)



for i in range(lower, upper):
    print("{} {}".format(i, chr(i)))

