# for eolymp:
a, b, c = [int(d) for d in input().split()]

# a < b < c
if a < b and b < c:
    print(b)
if c < b and b < a:
    print(b)

if b < a and a < c:
    print(a)
if c < a and a < b:
    print(a)

if (a<c and c<b) or (b<c and c<a):
    print(c)


# a, b, c = [int(d) for d in input().split()]
#
# # a < b < c
# if a < b and b < c:
#     print("b equals", b)
# if c < b and b < a:
#     print("b equals", b)
#
# if b < a and a < c:
#     print("a equals", a)
# if c < a and a < b:
#     print("a equals", a)
#
# if (a<c and c<b) or (b<c and c<a):
#     print("c equals", c)
#
# print("Ready!")