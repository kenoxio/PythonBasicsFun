# -------------------------------- warmup task 9/13
#what are the three kinds of programming errors? can you give an example of each?
# 1 - syntax error(missing something), 2 - scemantic error (runs but doesnt give the correct answer), 3 - runtime error (division by zero is an example)
#trace the output displayed by the following program when the data entered are 12 for m and 0 for n:
m = int(input("enter an interger> "))
n = int(input("enter an interger> "))
m = m + 5
n = 3 * n
print("m =", m, "\nn =", n)
# prints "m = 17 \n = 0"