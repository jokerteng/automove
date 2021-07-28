string = ".repair"

for i in range(10):
    open(str(i) + ".jpg", "x")
    open(str(i) + string + ".jpg", "x")
