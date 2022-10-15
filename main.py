a  = float(input("введіть перше чило"))
b = str(input("оберіть дію +,-,*,/"))
с = float(input("введіть третє число"))

if b == "+":
    print (a, "+", c, "=", a+c)
elif b == "-":
    print (a, "-", c, "=", a-c)
elif b == "*":
    print (a, "*", c, "=", a*c)
else:
    print(a, "/", c, "=", a / c)


