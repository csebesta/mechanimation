from time import sleep
print("Current values are:")
print("-" * 32)
x1 = "Value ONE is: "
x2 = "Value TWO is: "
for i in reversed(range(20)):
    print("\r" + x1 + str(i) + "   " + x2 + str(i), end="")
    sleep(0.5)
