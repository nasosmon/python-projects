import random

#Deck Creation function
def a(cards,t):
    for i in range(1,14):
        if i == 1:
            cards.append(t + " " + "A")
        if (i > 1 and i <= 10):
            cards.append(t + " " + str(i))
        if i == 11:
            cards.append(t + " " + "J")
        if i == 12:
            cards.append(t + " " + "Q")
        if i == 13:
            cards.append(t + " " + "K")
    return cards    

#Checking if the hand is straight

def Straight(values):
    count=0
    a=[]
    for i in range(0,5):
        if values[i]==" A":
            a.append(1)
            
        elif values[i]==" J":    
            a.append(11)
        elif values[i]==" Q":
            a.append(12)
        elif values[i]==" K":
            a.append(13)
        else:
            a.append(values[i])
            
    
    count=0
        
    
    for i in range(1,5):    
        if int(a[i])-int(a[i-1])==1:
                count+=1  
    
                 
            
    return count        
            
#Checking if the hand has a pair            

def Pair(values):
    count=0
    for i in range(0,5):
        for j in range(0,5):
            if i!=j:
                if values[i]==values[j]:
                    count+=1
    return count
    
#Checking if the hand has flush    

def Flush(suit):
  
    x=False
    suit.sort()
    if suit[0]==suit[4]:
        x=True
    return x    
            
            
def Change_Cards(pos,cards,player):
    draw_card=cards.pop()
    player[pos-1]=draw_card
    
    return player    

#Checking the highest card in the hand    

def Higher_Card(values):
    a=[]
    for i in range(0,5):
        if values[i]=="A":
            a.append(1)
            a.append(14)
        elif values[i]=="J":    
            a.append(11)
        elif values[i]=="Q":
            a.append(12)
        elif values[i]=="K":
            a.append(13)
        else:
            a.append(values[i])
    a.sort(reverse=True)
    h=a[0]
    return h    

#Checking if the hand has straight flush        

def Straight_Flush(s,f):
    x=False
    if s==5 and f==5:
        x=True
    return x    


#Checking if the hand has three of a kind            

def Three_Of_A_Kind(values):
    a=[]
    for i in range(0,5):
        if values[i]=="A":
            a.append(1)
            
        elif values[i]=="J":    
            a.append(11)
        elif values[i]=="Q":
            a.append(12)
        elif values[i]=="K":
            a.append(13)
        else:
            a.append(values[i])
    count=0    
    a.sort()
    for i in range(1,5):
        if a[i]==a[i-1]:
            count +=1
    x=False
    if count==3:
       x=True
    return x   

#Start of Main Programm


#Creating the deck

cards =[]
a(cards,"D")
a(cards,"H")
a(cards,"C")
a(cards,"S")
deck = cards
random.shuffle(cards)
p1=random.sample(cards,5)
print(p1)
p2=random.sample(cards,5)
print(p2)

#Changing Cards

x1= input("Player 1 how many cards do you want to change?")

if int(x1)>0:
    for i in range (0,int(x1)):
        pos=int(input("Which cards do you want to change?(Provide a number 1-5):"))
        p1=Change_Cards(pos,cards,p1)
print("New hand:")
print(p1) 

x2=input("Player 2 how many cards do you want to change?")
if int(x2)>0:
    for i in range(0,int(x2)):
        pos=int(input("Which cards do you want to change?(Provide a number 1-5):"))
        p2=Change_Cards(pos,cards,p2)    
 
print("New hand:")
print(p2) 

#Seperating the suits from values

suit1=[]
value1=[]
for i in range(0,5):
    suit1.append(p1[i][:1])
    value1.append(p1[i][1:])

suit2=[]
value2=[]     
for i in range(0,5):
    suit2.append(p2[i][:1])
    value2.append(p2[i][1:])    

#Calling functions to find who has the best hand

f1=Flush(suit1)
f2=Flush(suit2)
s1=Straight(value1)
s2=Straight(value2)
p1=Pair(value1)
p2=Pair(value2)
h1=Higher_Card(value1)
h2=Higher_Card(value2)
sf1=Straight_Flush(s1,f1)
sf2=Straight_Flush(s2,f2)
t1=Three_Of_A_Kind(value1)
t2=Three_Of_A_Kind(value2)
x=False
y=False
z=False
p=False
t=False

#Declaring the winner

if sf1==True:
    print("The winner is Player1 with Straight Flush")
    y=True
elif sf2==True:
    print("The winner is Player2 with Straight Flush")
    y=True

if y==False:
    if t1==3:
        print("The winner is Player1 with Three of a kind")
    elif t2==3:
        print("The winner is Player2 with Three of a Kind")
if t==False and y==False:
    if f1==True:
       print("The winner is Player1 with Flush")
       x=True
    elif f2==True:
       print("The winner is Player2 with Flush")
       x=True
        
if x==False and y==False and t==False:
    if s1==5:
        print("The winner is Player1 with Straight")
        z=True
    elif s2==5:
        print("The winner is Player2 with Straight")
        z=True
if x==False and y==False and z==False and t==False:
    if p1==3:
        print("The winner is Player1 with Double Pair")
        p=True
    elif p2==3:
        print("The winner is Player2 with Double Pair")
        p=True
    elif p1==2:
        print("The winner is Player1 with Pair")
        p=True
    elif p2==2:
        print("The winner is Player2 with Pair")
        p=True
        
if x==False and y==False and z==False and p==False and t==False:
    if h1>h2:
        print("The winner is Player1 with Higher Card")
    elif h1<h2:
        print("The winner is Player2 with Higher Card")
    
#End of Main Programm
    

            
        
        
            
            
    


            
        


        
        
        
    




 
        
        


    