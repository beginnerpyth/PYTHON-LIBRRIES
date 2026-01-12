import numpy as np
a=np.array([[2,3,4,5],[6,7,8,9]])
print(a)
print(np.zeros((2,3)))
print(np.ones((5,4)))
print(np.full((2,3),22))
print(np.full_like(a,5))
print(np.random.rand(2,3))
print(np.random.randint(4,7,size=(2,4)))#real ma chai size vameko elments dina
print(np.random.random_sample(a.shape))#real ma chai shape vaneko 2,3 rows and column hunxa
b=np.array([[1,2,3,4,5,6]])
c=np.repeat(b,3,axis=0)#you have to bracket inorder to do more dimensional
print(c)
d=np.ones((5,5),dtype='int32')
print(d)
g=np.zeros((3,3),dtype='int32')
print(g)
g[1,1]=(9)
print(g)

d[1:4,1:4]=g#when you size you have to exactly the given and expected to be same shape
print(d)
f=np.array([1,2,3,4,5])
h=f.copy()#if you dont use copy then it will change both sides
h[1]=100
print(h)
print(f)
#mathematics
i=np.array([2,3,6,7,7])
print(i+2)
print(i/2)
print(i-2)
print(i*2)
print(i+f)
print(i**2)
print(np.sin(i))#even you can do sin cos tan
###linear algebra
j=np.ones((2,3))#we give brackets cause to divide the rows and column if not it takes as data
k=np.full((3,2),2)
print(np.matmul(j,k))
l=np.identity(5)
print(np.linalg.det(l))
#statistics
check=(np.array([[1,2,3,4,5,6,7,8],[9,7,6,5,4,3,2,1]]))
print(check)
print(np.max(check))
print(np.min(check,axis=1))#axis 1 is row and axis 0 is columns

print(np.sum(check))
#suborganizing array reorganiizing
kk=np.array([1,2,3,4,5,6])
after= kk.reshape(3,2)
print(after)
jj=np.array([5,6,7,8,9,10])
print(np.vstack([kk,jj]))
print(np.hstack([kk,jj]))
