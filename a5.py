d = open(r"C:\Users\nasos\Desktop\destiny2.txt").read().split()
j = 0
for x in d:
    if len(d[j]) > 3:
        k = list(d[j])
        a = k[0]
        k.append(a)
        k[0] = "ay"
        b = ''.join(k)
        print (b)
    j = j + 1    
            
            
      