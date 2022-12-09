### 1) Create a program that allows a user to continue to add people to an address book until the user quits. Once the user quits, break out of the loop and print out the name and address of everyone in the address book

address_list = {}
name = input('Enter name:')
address = input('Enter address:')
address_list[name] = address
quit = input('Do you want to quit? y/n')
while quit != 'y':
    name = input('Enter name:')
    address = input('Enter address:')
    address_list[name] = address
    quit = input('Do you want to quit? y/n')
    if quit == 'y':
        break
    print(address_list) 

print(address_list)



### 2) Billy is trying to figure out if there is a time that he and his team can meet to work on the project. His three teammates each give him a list of times they are available ('HH:MM' 24-hour). Create a function that will take in an original list plus any number of lists of teammate's available times (*remember \*args*) and return a list of times where everyone can meet.

person1 = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
person2 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
person3 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
person4 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']
# Available Times: '12:00' and '14:30'

#function needs to take at least one list of times, and also any number *args, return list of overlapping times. 


def right_time(*times):
    one_time = []
    one_time_set = {}

    x = max(set(times), key=times.count)
    y = times.count(x)
    for time in times:
        if times.count(time) == y:
            one_time.append(time) 

    one_time_set = set(one_time) 
    return one_time_set


           
             

    
print(right_time(*person1, *person2, *person3, *person4))