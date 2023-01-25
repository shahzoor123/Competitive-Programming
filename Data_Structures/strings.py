# x = 'computer'


# y = [2,3,4,6,1,0]

# print(sorted(y))
# print(sum(y[1:]))

# c = 0
# for i in x:
#     c += 1
# print(f"The len of the string is {c}")    

from calendar import c


def buddy_string(goal,s):

    for i in goal:
        pass
    for x in s:
        if i == x:
            pass
        else:
            s_list = [*s]
            s_list[x] = c
            s_list[x+1] = s_list[x]
            s_list[x+1] = c
            print(s)
            
     



# buddy_string("aaaaaaaab","aaacaba")
buddy_string("ac","ab")