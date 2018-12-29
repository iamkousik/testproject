
def hel(rel, rels):
    print(rel, "It's Addition")
    print(rels, "It's Subtraction")
def add_sub(x,y):
    a = x+y
    s = x-y
    hel(a, s)
    c = x*y
    k = x/y
    return c, k

fst = int(input("Enter 1st number :"))
sec = int(input("Enter 2nd number :"))
mul, div = add_sub(fst, sec)
print(mul, "It's Multiplication")
print(div, "It's Division")