sales = float(input("Enter sales: $"))
while sales > 0:
    if (sales < 1000):
        bonus = 0.1 * sales
        print("bonus is: ",bonus)
    else:
        Bonus = 0.15 * sales
        print("bonus is :", bonus)
        sales = float(input("enter sales : $"))