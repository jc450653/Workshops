Instruction = "Welcome to our program.\nInput negative number of Items to quit:"
print("Instruction")


numofItems = 1
while numofItems > 0 :
    numofItems = int(input("please input the number of Items: "))
    costperItem = float(input("the shipping cost for each Item: $"))
    totalshippingcost = numofItems * costperItem;
    if totalshippingcost > 100:
        totalshippingcost = totalshippingcost * 0.9
    print("the Total cost for delivering your product is: ",totalshippingcost)
