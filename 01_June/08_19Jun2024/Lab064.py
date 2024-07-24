n = [1,2,3]

# collection of items
def do_stuff(n):
    n.append(4)
    n[0] = 20
    return n

l = do_stuff(n)

print(l)