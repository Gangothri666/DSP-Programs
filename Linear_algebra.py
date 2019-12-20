#Program using Linear algebra
import numpy as np
a=input('enter a 3*3 array:')  
print(a[0],a[1],a[2])         
a[0]=6                        
print a
b=np.zeros((3,3))            
print"matrix of zeroes:",b    
c=np.ones((2,3))             
print('matrix of ones:')        
print c
d=np.full((2,3),6)            
print('matrix of constant:')         
print d
e=np.eye(3,3)                
print('identity matrix:')                
print e
f=np.random.random((3,3))     
print('matrix of random values:')
print f
m=np.matrix([[1,2,3],[3,4,5],[6,7,8]])
print m
print('transpose matrix:')
print(m.T)                   
x=np.matrix([[1,2],[3,4]])
y=np.matrix([[6,7],[9,3]])
g=np.linalg.eig(m)
print('eigen values:')
print g
h=np.linalg.det(m)
print('determinent:')
print h
i=np.linalg.matrix_rank(m)
print('rank of matrix:')
print i
j=np.linalg.inv(m)
print('inverse of a matrix:')
print j
k=np.linalg.solve(x,y)
print('solved equations:')
print k
print('sum of two matrices:')
print(x+y)                    
print('difference of two matrices:')
print(x-y)                    
print('product of two matrices:')
print(x*y)                    
print('division of two matrices:')
print(x/y)                    
print('elementwise square root of matrix:')
print(np.sqrt(x))             
print('inner product of matrix:') 
print(x.dot(y))  
             
