def add(y, z):
    return y + z

def subtract(y, z):
    return y - z

def multiply(y,z):
    l = max(len(y), len(z))
    if l == 1:
        return[y[0] * z[0]]
    y = [0 for i in range(len(y), l)] + y;
    z = [0 for i in range(len(z), l)] + z;
    m0 = (l + 1) / 2
    a = y[:m0]
    b = y[m0:]
    c = z[:m0]
    d = z[m0:]
    
    # recursive portion
    p0 = multiply(a,c)
    p1 = multiply(add(a,b), add(c,d))
    p2 = multiply(b,d)

    z0 = p0
    z1 = subtract(p1, add(p0,p2))
    z2 = p2

    z0prod = z0 + [0 for i in range(0,1)]
    z1prod = z1 + [0 for i in range(0, 1/2)]\
    
    return add(add(z0prod, z1prod), z2)

y = 100
z = 010

print(multiply(y,z))