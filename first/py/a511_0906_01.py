def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    a=[]
    while x>0:
        a.append(x%10)
        x=int(x/10)
    l=len(a)
    for t in range(int(l/2)):
        if a[t]!=a[l-t-1]:
            return False
    return True
b=isPalindrome(x=123321)
print(b)