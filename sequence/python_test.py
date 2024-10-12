DOUBLE_ARRAY=[[]]*1000
print(DOUBLE_ARRAY)


print_array = [1,23,5]

print(print_array)
print(*print_array)

from collections import deque
print_que = deque()
print_que.append(2)
print_que.append(3)
print_que.appendleft(5)

print(print_que)
print(*print_que)

test_list = list(print_que)
print(type(test_list))
print(test_list)
print(*test_list)