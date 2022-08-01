from PIL import Image
II = Image.open("general_radahn.png").load()
gg = [-1,-1,-1,-1]
cc = 0
for i in range(2022):
    cc += 1
    x = list(II[i,0])
    if(gg != x):
        gg = x
        if(cc >1):
            print(chr(cc), end='')
        cc = 0