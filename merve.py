l = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
l1 = []

def flatten(l):

    for i in l:
        if isinstance(i, list):
            flatten(i)
        else:
            l1.append(i)

flatten(l)
print(l1)