def romanToInt(self, s):
    A={"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    ans=0
    for i in range(len(s)-1):
        if A[s[i]]<A[s[(i+1)]]:
            ans-=A[s[i]]
        else:
            ans+=A[s[i]]
    return ans+A[s[-1]]
