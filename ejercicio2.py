'''2. En la jerarquía de operadores, cuáles son los que más
prioridad tienen cuando el intérprete de Python los evalúa? '''

''' 1.operador de asignacion'''
a=7
b=2
print("Operadores de asignacion")
x=a; x+=b; print("x+=", x)
x=a; x-=b;  print("x-=", x)
x=a; x*=b;  print("x*=", x)  
x=a; x/=b;  print("x/=", x)  
x=a; x%=b;  print("x%=", x)  
x=a; x//=b; print("x//=", x) 
x=a; x**=b; print("x**=", x) 
x=a; x&=b;  print("x&=", x)  
x=a; x|=b;  print("x|=", x)  
x=a; x^=b; print("x^=", x)   
x=a; x>>=b; print("x>>=", x) 
x=a; x<<=b; print("x<<=", x) 

'''Operadores aritmeticos'''
print("Operadores aritmeticos")
print("x+b =", x+b)   
print("x-b =", x-b)   
print("x*b =", x*b)   
print("x/b =", x/b)   
print("x%b =", x%b)   
print("x**b =", x**b) 
print("x//b =", x//b) 

'''Operadores Relacionales'''
print("Operadores Relacionales")
print("x==y =", x==b) 
print("x!=y =", x!=b) 
print("x>y  =", x>b)  
print("x<y  =", x<b)  
print("x>=y =", x>=b) 
print("x<=y =", x<=b) 

'''Operadores logicos '''
print("Operadores logicos")
print("Operadores and")
print(True and True)
print(True and False)  
print("Operadores or")
print(True or True)   
print(True or False) 
print("Operadores not")
print(not True)  
print(not False)     