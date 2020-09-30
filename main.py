
#count occurrences 
data = [1,2,3,4,5,6,7,8,9,10]  
total = 0                       
to_count = int(input("Enter search number: ")) 
for x in range(0,len(data)):   
  if to_count == data[x]:         
    total = total + 1  

print("The number " +str(to_count)+" was found "+str(total)+" time(s)")
print()
"""
Alternative method: 
x = data.count(to_count)
print (x)

"""

#linear search
search = int(input("Enter search number: "))

present = False
while present == False:
  for x in range (len(data)):
    present = False
    for x in range(len(data)):
      if search == data[x]:
        present = True

if present == True:
  print("The number "+str(search)+" was found")
if present == False:
  print("The number "+str(search)+" was not found")
print()

#find max
maximum = data[0]
for x in range(len(data)):
  if maximum > data[x]:
    maximum = data[x]
print ("The maximum is "+str(maximum))
print ()


#find min
minimum = data[0]
for x in range(len(data)):
  if minimum < data[x]:
    minimum = data[x]
print ("The minimum is "+str(minimum))