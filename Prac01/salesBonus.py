
sales=1
while sales > 0:
    sales = float(input("enter sales: $"))
if(sales <= 1000):
    bonus=(10/100)*sales
    print("your bonus is ",bonus)
elif(sales >= 1000 and sales <=5000):
    bonus=(15/100)*sales
    print("your bonus is",bonus)
else:
    print("excessive amount of sales")


