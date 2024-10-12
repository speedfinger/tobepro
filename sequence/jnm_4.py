"""
https://codepass.co.kr/contest/406/problem/4?cursor=eyJwcm9ibGVtc2V0IjoiY180MDYiLCJmaWVsZCI6MCwiaWR4IjozfQ==


deque로도 풀수 있구나,,

1.
deque.appendleft()를 제공함..
ARRAY.reverse()
ARRAY.append(value)
ARRAY.reverse()

위 코드가 한줄로 해결..


3. 정렬
seq.sort(key=lambda x: (abs(value - x), x))
seq.sort(...):

sort() 메서드는 리스트를 제자리에서 정렬합니다. 즉, 기존의 리스트 seq를 변경하고, 반환값은 None입니다.
key=lambda x: ...:

key 인자는 정렬에 사용할 기준을 정의하는 함수입니다. 여기서는 lambda 함수를 사용하여 익명 함수(즉, 이름이 없는 함수를 정의하고 있습니다)로 정렬 기준을 설정합니다.
x는 리스트의 각 요소를 나타냅니다.
abs(value - x):

각 요소 x와 value의 차이의 절댓값을 계산합니다. 이는 x가 value에 얼마나 가까운지를 측정하는 기준이 됩니다.
(abs(value - x), x):

이 부분은 튜플을 반환합니다. 첫 번째 요소는 abs(value - x)로 각 요소가 value와의 거리이고, 두 번째 요소는 x 자신입니다.
Python의 정렬 알고리즘은 튜플의 첫 번째 요소를 먼저 기준으로 정렬하고, 첫 번째 요소가 동일한 경우 두 번째 요소를 기준으로 정렬합니다. 따라서, 먼저 거리로 정렬하고, 거리가 같은 경우에는 원래의 값 x로 정렬합니다.


만약 deque를 사용 시 :
seq = deque(sorted(seq, key=lambda x: (abs(value - x), x))) # O(N * log N), deque

1. sorted 에는 리스트,튜플,deque등이 올수 있는것으로 보임
2. deque(sorted(seq,))  sorted는 무조건 리스트를 반환해서 deque로 한번 싸준것으로 보임


"""
import sys
import copy

sys.stdin = open("./sequence/jnm_4.txt",'r')

input = sys.stdin.readline


COMMAND_Q = int(input().strip())


ARRAY = []


def _add(pos,value):
    # print(f"add : {pos}, {value}")
    if pos ==0:
        ARRAY.reverse()
        ARRAY.append(value)
        ARRAY.reverse()
    else:
        ARRAY.append(value)
    

def _erase(pos,value):
    # print(f"erase : {pos}, {value}")
    global ARRAY
    
    NEW_ARRAY =[]

    erased_count = 0
    if pos==0:
        for i in range(0,len(ARRAY)):
            if ARRAY[i]>=value and erased_count<=2:
                erased_count=erased_count+1
            else:
                NEW_ARRAY.append(ARRAY[i])
    else:
        for i in range(len(ARRAY)-1,-1,-1):
            if ARRAY[i]>=value and erased_count<=2:
                erased_count=erased_count+1
            else:
                NEW_ARRAY.append(ARRAY[i])
                
        NEW_ARRAY.reverse()    
    ARRAY=NEW_ARRAY


def _sort(value):
    # print(f"sort : {value}")
    global ARRAY
    
    NEW_ARRAY=[]

    # DOUBLE_ARRAY=[[]]*1000
    DOUBLE_ARRAY= [[] for _ in range(1000)]

    for i in range(0,len(ARRAY)):
        current= ARRAY[i]
        abs_value = abs(current-value)

        DOUBLE_ELEMENT=DOUBLE_ARRAY[abs_value]

        if len(DOUBLE_ELEMENT)==0:
            DOUBLE_ELEMENT.append(current)
        else:
            prev_len=len(DOUBLE_ELEMENT)
            for n in range(0,len(DOUBLE_ELEMENT)):
                N_current=DOUBLE_ELEMENT[n]

                if N_current>current:
                    DOUBLE_ELEMENT.insert(n,current)
                    break

                if N_current==current:
                    DOUBLE_ELEMENT.insert(n,current)
                    break
            post_len=len(DOUBLE_ELEMENT)

            if prev_len==post_len:
                DOUBLE_ELEMENT.append(current)
        
        # print(f"@@@{i} has : {DOUBLE_ELEMENT}")
    # print(DOUBLE_ARRAY)
    for idx in range(0,len(DOUBLE_ARRAY)):
        D_ELEMENT = DOUBLE_ARRAY[idx]

        if len(D_ELEMENT)==0:
            continue
        for k in range(0,len(D_ELEMENT)):
            NEW_ARRAY.append(D_ELEMENT[k])
    
    # print(f"@@@ : {NEW_ARRAY}")
    ARRAY = NEW_ARRAY


    
    # for i in range(0,len(ARRAY)):
    #     current= ARRAY[i]

    #     if len(NEW_ARRAY)==0:
    #         NEW_ARRAY.append(current)
    #     else:
    #         abs_value=abs(current-value)
    #         # print(f"{current} - {value} = {abs_value}")
    #         for n in range(0,len(NEW_ARRAY)):
    #             N_current = NEW_ARRAY[n]
    #             N_abs_value=abs(N_current-value)

    #             #ARRAY의 abs값이 더 작으면 갱신
    #             if N_abs_value>abs_value:
    #                 NEW_ARRAY.insert(n,current)


    #    ARRAY에 NEW_ARRAY 갱신

def _print(pos):
    # print(f"print : {pos}")

    
    if pos ==0:
        print_str = ' '.join(map(str,ARRAY))
    else:
        NEW_ARR = copy.deepcopy(ARRAY)
        NEW_ARR.reverse()
        print_str = ' '.join(map(str,NEW_ARR))

    print(f"{print_str}")


    pass

for _ in range(0,COMMAND_Q):
    commands = list(map(int,input().split()))
    # print(commands[0])
    cmd = commands[0]

    if cmd == 1:
        _add(commands[1],commands[2])
    elif cmd ==2:
        _erase(commands[1],commands[2])
    elif cmd ==3:
        _sort(commands[1])
    else:
        _print(commands[1])
    
    # print(ARRAY)