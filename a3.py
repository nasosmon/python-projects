a={}
product = []
price = []
x = True
c = 0
while x == True:
    b = input("Give product name: ")
    y=False
    while y ==False:
        p = input("Give product price: ")
        if float(p)>0:
            y=True
        else:
            print("Invalid price.Please try again")
            
    c = c+1
    product.append(b)
    price.append(p)
    
    ans= input("Do you want to add another product?(Y/N)")
    z=False
    while z==False:
        if ans=="Y" or ans=="N":
            z=True
        else:
            print("Invalid answer")
        
        
    if ans == "N":
        x = False


a = zip(product,price)        
    
        
        

s = 0
final_price=[]
for i in range(0,c) :
    fp=float(price[i]) + 24/100 * float(price[i])
    final_price.append(fp)
    s = s + final_price[i]
    
    
print("The total cost is" ,s)    
    
        
    
    
    
    

