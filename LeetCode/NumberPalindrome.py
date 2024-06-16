def isPalindrome(self, x):
    b=str(x)
    if b==b[::-1]:
        return True
    else:
        return False
def isPalindrome2(self,x):
    if x<0:
        return False
    temp=x
    reversednum=0
    while temp!=0:
        dig=temp%10
        reversednum=reversednum*10+dig
        temp=temp//10
    if reversednum==x:
        return True
    else:
        return False
isPalindrome2(0,121)