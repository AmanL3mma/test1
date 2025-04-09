print("For loop with range defaut start")
for i in range(5):
    print("Statement %s ,step 1 "%i)

print("For loops with range specifying start and end")
for i in range(5,10):
    print("Statement %s ,step 1 "%i)

print("For loop with range specifying start , end and step")
step=2
for i in range(1,10,step):
    print("Statement %S ,step : %s "%(i,step))