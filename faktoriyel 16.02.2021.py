#n! ( faktöriyel)
#16.02.2021

def faktoriyel(n):
     sonuc=1
     for i in range(1,n+1):   #1..n arası sayıların çarpım döngüsü 
          sonuc=sonuc*i

     return sonuc




def faktoriyel2(n):  #n!=n.(n-1)!  #bildiğim gerçek:0!=1
     if n==0:
          return 1
     else:
          return n*faktoriyel2(n-1)



#ana program
print(faktoriyel(10))
print(faktoriyel2(10))
