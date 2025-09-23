str = str(input("Ведите предложение на английском: "))
print("Длина предложения",len(str))
b = str.lower()
print("В нижнем регистре", b)
count = 0;
c = "aeiou"
for i in str:
    if i in c:
        count += 1
print(count)
print(str.replace("ugly", "beauty"))
print(str.startswith("The"))
print(str.endswith("end"))
