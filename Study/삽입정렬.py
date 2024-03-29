#기본 전략:
#s[0]를 떼어내 s[1:]을 정렬한 후, 알맞은 위치에 넣는 작업을 반복한다.
#함수를 모두 떼어낸 후 알맞은 위치에 넣어주자.
#insert 함수 구상:
#원소를 알맞은 위치에 집어넣는 함수이다.
#리스트가 비어 있으면 그냥 s[0]를 리스트에 넣어 출력한다.
#리스트가 비지 않았다면 s[0]를 s[1]과 비교해 순서를 결정한다.
#만약 s[1]가 s[0]보다 작으면, s[0]를 s[2:]중 알맞은 위치에 집어넣는다.(재귀)
def isort(s):#함수를 정렬한다.
    if s!=[]:
        return insert(s[0],isort(s[1:]))
    else:
        return []
#s가 빈 리스트가 아니면, s를 0번째와 그 이후로 나누고, 0번째를 isort된 뒤의 함수에 insert한다.
#물론 우리는 함수를 정렬한 적이 없지만, 
#아래의 insert 함수를 이용해 "알맞은" 위치에 반복적으로 넣어줌으로써 정렬을 할 수 있게 된다.
def insert(x,ss):#함수의 "알맞은" 위치에 원소를 넣는다.
    if ss!=[]:
        if ss[0]<=x:
            return [ss[0]]+insert(x,ss[1:])
        #만약 x가 ss[0]보다 크면 ss[0]를 맨 앞으로 보내고, 그 뒤의 함수의 "알맞은" 위치에 원소를 넣는다.
        #우리는 그 알맞은 위치가 어딘지는 모르지만, insert함수가 자동으로 알맞은 위치로 보내주므로 상관없다.
        else:
            return [x]+ss
        #x가 더 크면 x만 앞으로 빼서 이어 쓴다. 이때 ss는 정렬된 상태로 넣어주므로 그대로 이어 붙이면 된다.
        #물론 우리는 ss를 정렬한 적이 없지만, 재귀함수로 인해 결국 컴퓨터가 알아서 정렬하게 될 것이다.
    else:
        return [x]
    #만약 함수가 비어 있으면 그냥 x를 넣어주면 된다.
s=[8,7,5,6,3,4,1,1,3,4,5]
ss=isort(s)
print(ss)
#위에서 알지 못하는 계산 과정을 생략하는 것이 이해되지 않는다면 다음의 예를 들어보자.
#A는 자료를 만들기 위해 B의 자료를 인용하고, B는 후속 자료를 만들기 위해 A의 자료를 인용한다.
#만약 A와 B에게 자료의 신뢰성을 묻는다면, A는 B가 처리한 부분이라고 답할 것이고, B는 A가 처리한 부분이라고 답할 것이다.
#그렇다면 최초에 B가 A에게 준 정보만 타당하다면 모든 A와B가 만든 정보는 타당할 것이다.
#따라서 우리는 최초의 자료와 A와 B가 각각 어떤 작업을 했는지만 알고 있으면 모든 정보를 신뢰할 수 있다.
