#Task1
Number=int(input("enter a number:"))
if Number % 2==0:
    print(f"{Number} is an even number.")
else:
    print(f"{Number} is an odd number.")

#Task2
total=0
for i in range(1,51):
    total+=i
print("The sum of numbers from 1 to 50 is:",total)