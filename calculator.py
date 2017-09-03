import math
op=["log","magnitude","sin","cos","tan"]
def calcy(data):
    a=str(data).split(" ")
    global op
    if a[1] not in op:
        if a[2]=="+":
            res=str(int(a[1])+int(a[-1]))
            return res   
        elif a[2]=="-":
            res=str(int(a[1])-int(a[-1]))
            return res
        elif a[2]=="X":
            res=str(int(a[1])*int(a[-1]))
            return res
        elif a[2]=="/":
            res=str(int(a[1])/int(a[-1]))
            return res
    elif a[1] in op:
        if a[1]=="log":
            res=math.log(int(a[2]),int(a[-1]))
            return res
        elif a[1]=="magnitude":
            res=math.sqrt(int(a[3])*int(a[3])+int(a[5])*int(a[5]))
            return res
        
    
        
    
