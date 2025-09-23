string = "hello"
memory = " world"
counter = 0
while counter != 10:
    print(string + memory)
    print(string)
    counter += 1
string = string + " world"
memory = string
print(memory)