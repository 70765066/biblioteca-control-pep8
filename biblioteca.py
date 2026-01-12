class Biblioteca:
 def __init__(s,n):
  s.n=n
  s.lb=[]

 def addb(s,b):
  s.lb.append(b)

 def show(s):
  for x in s.lb:
   print(x.t,x.a,x.i)

class Book:
 def __init__(self,t,a,i):
  self.t=t
  self.a=a
  self.i=i
  self.e=True

 def prest(self):
  if self.e==True:
   self.e=False
   return True
  else:
   return False

 def ret(self):
  self.e=True
