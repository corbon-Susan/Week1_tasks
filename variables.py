#creating variables showing different data types
names=("daniel", "10years", "12.5cm tall")
numbers=(2,3,4,5,6,7)
fractional_numbers=(23.1,0.23, 0.06)
print(names)
print(numbers)
check=True
print(check)
# print=(fractional_numbers)
# int()
# float()
# str()
# bool()
# print()
#convert string to int
age =int(input("Enter your age:"))
print(f"you will be {age + 1} years old next year.")
# calculator using input
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
sum_result=num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")
sum_result=num1 * num2
print(f"The sum of {num1} and {num2} is {sum_result}.")
#class task
#asking my students to identify theirselves  using numbers

Welcome =int(input("Are you a student in this school?,enter 1 if yes or 2 if no "))
print(f"you are welcome to school {Welcome}.")

#trying to ask a customer for the kind of service they want to be offered
service = int(input("enter the service you want using numbers, 1:barbing, 2:plaiting"))
service2 = float(input("enter the time you will like to have this service"))
print(f"you booked for {service} : {service2}" )
