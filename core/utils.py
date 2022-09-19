def rand(fxd1,fxd2,var1,var2,var3):
    res=[]
    for i in var1:
        for j in var2:
            for k in var3:
                if fxd2 < i and i < j and j < k:
                    res.append(fxd1*100000000 + fxd2*1000000 + i*10000 + j*100 + k)
    return res

def formatInputData(var):
    temp = var.split(",")
    var = list(map(int, temp))
    return var