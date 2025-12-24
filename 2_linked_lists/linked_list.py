class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

head = a

# For intersection problem
a = Node(1)
b = Node(2)
c = Node(9)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)

a.next = b
b.next = c

e.next = f
f.next = g

g.next = c

c.next = d

# loop detection

j = Node(1)
k = Node(2)
l = Node(10)
m = Node(4)
n = Node(5)
o = Node(6)
p = Node(8)

j.next = k
k.next = l

l.next = m
m.next = n
n.next = o
o.next = p
p.next = l

