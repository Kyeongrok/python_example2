f1 = open("./a.txt", mode='w+')
f1.write("hello\n")
f1.write("nello\n")
f1.close()

numbers = [1, 2]
f2 = open("./b.txt", mode='w+')
for number in numbers:
    f2.write(str(number) + "\n")
f2.close()