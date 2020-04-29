def ecuacion(x,y):
    R = x**2 -y*x +4*y
    if R < 0:
        R = (-1*R)**0.5
    else:
        R = R**0.5
    return R 

N = ecuacion(8,6) 
print(N)
M = ecuacion(5,12)
print(M)


