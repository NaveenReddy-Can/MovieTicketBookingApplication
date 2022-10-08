# Naveen reddy
# TEST-2
# C0838989
# Question 1

reservation_id = 1
 
# function for booking seats. 
def reserveSeats(theatreArray, numberOfSeats, preference):
    global reservation_id 
    n = len(theatreArray)
    m = len(theatreArray[0])
    count = 0
    success = False

    if preference == 1:
        for i in range(n):
            count = 0
            if theatreArray[i].count(0) >= numberOfSeats:
                for j in range(m):
                    if theatreArray[i][j] == 0:
                        count += 1
                    elif theatreArray[i][j] != 0 and count < numberOfSeats:
                        break

                if count >= numberOfSeats:
                    count = 1
                    for j in range(m):
                        if theatreArray[i][j] == 0 and count <= numberOfSeats:
                            theatreArray[i][j] = reservation_id
                            count += 1
                    success = True
            if success:
                break

    elif preference == 2:
        for i in range(n-1, 0, -1):
            count = 0
            if theatreArray[i].count(0) >= numberOfSeats:
                for j in range(m-1, 0, -1):
                    if theatreArray[i][j] == 0:
                        count += 1
                    elif theatreArray[i][j] != 0 and count < numberOfSeats:
                        break

                if count >= numberOfSeats:
                    count = 1
                    for j in range(m-1, 0, -1):
                        if theatreArray[i][j] == 0 and count <= numberOfSeats:
                            theatreArray[i][j] = reservation_id
                            count += 1
                    success = True
            if success:
                break

    if success:
        print('Your seats are booked with reservation ID:', reservation_id)
        reservation_id += 1
    else:
        print('Reservation could not be made')    

# function for reserving specific seats 
def reserveSpecificSeats(theatreArray , numberOfSeats, row, columnStart):
    global reservation_id
    n = len(theatreArray)
    m = len(theatreArray[0])
    count = 0
    success = False
    if theatreArray[n - row].count(0) >= numberOfSeats: 
        for i in range(columnStart - 1, m):
            if theatreArray[n - row][i] == 0:
                count += 1
            elif theatreArray[n - row][i] != 0 and count < numberOfSeats:
                break

        if count >= numberOfSeats:
            count = 1
            for i in range(columnStart - 1, m):
                if theatreArray[n - row][i] == 0 and count <= numberOfSeats:
                    theatreArray[n - row][i] = reservation_id
                    count += 1
            success = True

    if success:
        print('Your seats are booked with reservation ID:', reservation_id)
        reservation_id += 1
    else:
        print('Reservation could not be made')

# function for canceling seats
def cancelSeats(theatreArray, bookingNumber):
    for i in range(len(theatreArray)):
            for j in range(len(theatreArray[0])):
                if theatreArray[i][j] == bookingNumber:
                    theatreArray[i][j] = 0


# function for remove empty seats
def removeEmptySeatsRow(theatreArray,row):
    n = len(theatreArray)
    m = len(theatreArray[0])
    i = 0
    j = 0
    while i < m:
        if theatreArray[n - row][i] > 0:
            while j < i and theatreArray[n - row][j] != 0:
                j += 1
            theatreArray[n - row][j] = theatreArray[n - row][i]
            theatreArray[n - row][i] = 0
        i +=1

# function for search the seats or booking 
def search(theatreArray, bookingNumber):
    is_found = False
    for i in range(len(theatreArray)-1, 0, -1):
        for j in range(len(theatreArray[0])):
            if theatreArray[i][j] == bookingNumber:
                if not is_found:
                    print('\nSEATS BOOKED AS SHOWN BELOW:')
                    is_found = True
                print('Row {0}, Seat {1}'.format(len(theatreArray) - i, j + 1))

    if not is_found:
        print("\n No seats with specified booking ID could be located.") 

# function for calculating total booked seats
def totalBooked(theatreArray):
    count = 0
    for i in range(len(theatreArray)):
        for j in range(len(theatreArray[0])):
            if theatreArray[i][j] != 0:
                count += 1
    return count

# function for displaying theatre map
def displayMap(theatreArray):
    print()
    for row in theatreArray:
        print(*row, sep='\t')
    print()

# function for user menu
def display_menu():
    print('\n\nMENU:')
    print('***********************')
    print('1. Reserve seats')
    print('2. Reserve seats with specific starting row and column')
    print('3. Cancel reservation')
    print('4. Remove empty seats from specific row')
    print('5. Search for reservation')
    print('6. Total seats booked')
    print('7. Display theatre map')
    print('8. Exit application')
    print('***********************')
    print("")



def get_menu():
    display_menu()
    user_input = int(input('User selection: '))
    while user_input > 8 or user_input < 1:
        print('***********************')
        print('ERROR: Invalid menu selection. Please try again!\n')
        display_menu()
        user_input = int(input('User selection: '))
        print('***********************')
    return user_input



def initialize_array(theatreArray):
    for i in range(8):
        row = []
        for j in range(10):
            row.append(0)
        theatreArray.append(row)



if __name__ == '__main__':
    theatreArray = []
    initialize_array(theatreArray)

    user_input = get_menu()
    while user_input != 8:
        if user_input == 1:
            numberOfSeats = int(input("Enter the number of adjacent seats do you required to book: "))
            preference = int(input("choose the Preference of seating (Enter 1 to choose seats BACKSIDE, Enter 2 to choose FRONTSIDE): "))
            reserveSeats(theatreArray, numberOfSeats, preference)
            displayMap(theatreArray)


        elif user_input == 2:
            numberOfSeats = int(input("Enter the number of seats do you required to book: "))
            row = int(input("Enter the row number you wish to book seats: "))
            columnStart = int(input("Enter a COLUMN number, you want your seats to begin at: "))
            reserveSpecificSeats(theatreArray, numberOfSeats, row, columnStart)
            displayMap(theatreArray)
        
        elif user_input == 3:
            bookingID = int(input("Enter Reservation number you would like to cancel: "))
            print('***********************')
            cancelSeats(theatreArray, bookingID)
            print("Your seats are successfully cancelled...!")
            displayMap(theatreArray)


        
        elif user_input == 4:
            row = int(input("Which row you like to remove empty seats from:"))
            print('***********************')
            removeEmptySeatsRow(theatreArray, row)
        
        elif user_input == 5:
            bookingID = int(input("Reservation ID you are searching for: "))
            print('***********************')
            search(theatreArray, bookingID)

        elif user_input == 6:
            count = totalBooked(theatreArray)
            print('***********************')
            print("The total number of seats is already reserverd is : ", count)

        elif user_input == 7:
            displayMap(theatreArray)
        
        user_input = get_menu()
    
    print("\n\n Thanks for using the application...!!!!!\n")