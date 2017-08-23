from time import sleep
t1 = "Value one is: "
t2 = "Value two is: "
s = "  "
for i in range(20):
    print("\r" + t1 + str(i) + s + t2 + str(i), end="")
    sleep(0.5)
