#Calculate the sum of even numbers up to a given number n.
range_num=int(input("enter the range of number : "))
sum=0
for i in range(1,range_num+1):
    if i%2==0:
        sum +=i
        print(sum)
print("sum of even number is ",sum)
