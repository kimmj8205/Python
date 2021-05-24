#기본 전략:len(s)가 1보다 클 때, 리스트를 반으로 쪼갠다
#계속 쪼개서 하나만 남을 때까지 쪼개고, 다시 반대로 합치면서 정렬한다.
def msort(s):#함수를 둘로 쪼갠다.
    if len(s)>1:
        m=len(s)//2
        return merge0(msort(s[:m]),msort(s[m:]))#삽입 정렬에서 그러했든 함수를 나눠가며 합쳐야 한다.
    else:
        return s
def merge0(L,R):#함수를 정리하며 합쳐 새로운 함수를 만든다.
    if not (L==[] or R==[]):
        if L[0]<R[0]:
            print(L,',2,',R)
            return [L[0]]+merge0(L[1:],R)
        #왼쪽과 오른쪽 중 작은 0번째 값을 빼내어 입력하고 나머지를 합쳐 새로운 함수로 만든다.
        #즉, 재귀를 이용한다
        else:
            print(L,',1,',R)
            return [R[0]]+merge0(L,R[1:])
    elif L==[]:
        return R
    #만약 왼쪽 또는 오른쪽이 비면 자동으로 나머지 값이 뒤에 이어 붙도록 한다.
    #함수 설계상 양쪽이 모두 빈 리스트일 수는 없다.
    elif R==[]:
        return L
s=[8,7,5,6,3,4,1,1,3,4,5]
ss=msort(s)
print(ss)
