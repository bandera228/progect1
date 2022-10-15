a  = float(input("введіть перше чило"))
b = str(input("оберіть дію +,-,*,/"))
u = float(input("введіть третє число"))5

if b == "+":
    print (a, "+", u, "=", a+u)
elif b == "-":
    print (a, "-", u, "=", a-u)
elif b == "*":
    print (a, "*", u, "=", a*u)
else:
    print(a, "/", u, "=", a / u)


