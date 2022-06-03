# Loops & Iterators

largest = None

smallest = None

while True:

    num = input("Enter a number:")

    if num == 'done' :

      break

    try:

        n = int(num)

    except:

      print('Invalid input')

      continue

    if smallest is None and largest is None:

        smallest = n

        largest = n 

    elif (smallest>n):

      smallest = n

    elif (largest<n):

      largest = n

  

# print('All Done')

 

print("Maximum is", largest)

print("Minimum is", smallest)
