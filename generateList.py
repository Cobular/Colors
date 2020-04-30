file1 = open("colors.txt","w")#write mode 
for r in range(256): 
    for g in range(1):
        for b in range(1):
            file1.write('\n'+("#{:02x}{:02x}{:02x}".format(r,g,b)).replace(" ",""))
            #print(("#{:02x}{:02x}{:02x}".format(r,g,b)).replace(" ",""))

file1.close()
