# Ex1
sum_no = 0
n = (int(input("Enter Number:")))

for n in range(51, 100):
    sum_no += n
    print("No:", n)


# Ex2
fp = (float(input("Enter floating point:")))
sum_numbers = 0
for fp in range(0, 10):
    fp += 0.5
print("Loop finishes...", fp)

# Ex3
sum = int(input("Enter No:"))
sum = 0
for i in range(20, 1, -1,):
    if i % 3 == 0:
        sum += i
        print(sum)

# Ex4
euro = float(input("Enter amount of euros:"))
CONVERSION_RATE = 120.77
conversion = euro * CONVERSION_RATE


for conversion in range(0, 1000000000, -1):
    print(conversion)
    conversion += 1

print("The amount of Japanese Yen:", conversion)


# Ex5
starting_number = int(input("Enter starting number:"))
ending_number = int(input("Enter ending number:"))
count = int(input("Count in:"))
sum_of_numbers = 0
for sum_of_numbers in range(1, 100, +1):
    sum_of_numbers += 1
    print(sum_of_numbers,"resulted from", starting_number, "to", ending_number)