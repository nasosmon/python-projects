
d = open(r"C:\Users\nasos\Desktop\destiny2.txt").read().split()
d.sort(key = len, reverse = True)
k = [None] * 5
for i in range (0, 5):
    k[i] = d [i]

j = 0
for x in k:
    a = k[j] 
    a = a.translate({ord(i): None for i in "aeiou"})
    print (a[::-1])
    j = j + 1

        





    

    
    
        
    