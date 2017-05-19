#multiples A - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
for count in range(1, 1001, 2):
    print count

#multiples B - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for count in range(5,1000001,5):
    print count

#sum list - Create a program that prints the sum of all the values in the list
my_numbers = [1, 2, 5, 10, 255, 3]
sum = 0
for i in my_numbers:
    sum += i
print sum

#average list - Create a program that prints the average of the values in the list:
print sum/len(my_numbers)