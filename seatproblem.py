# Initialize the train coach with 0's (all seats available).
# First 10 rows have 7 seats, and the last row has 3 seats.
train_coach = [[0 for _ in range(7)] for _ in range(10)]
train_coach.append([0 for _ in range(3)])  # Last row with 3 seats

# Sample pre-booked seats, marked as 1.
# You can assume this is dynamically updated by the system in a real app.
train_coach[0][1] = 1  # Seat 2 is booked
train_coach[4][3] = 1  # Seat 32 is booked
train_coach[9][6] = 1  # Seat 70 is booked
train_coach[10][2] = 1 # Seat 80 is booked

# Function to display the current seating arrangement
def display_seats(coach):
    for i, row in enumerate(coach):
        row_display = "Row " + str(i+1) + ": " + " ".join(['X' if seat == 1 else 'O' for seat in row])
        print(row_display)
    print()

# Function to book seats
def book_seats(num_seats):
    # Iterate over the rows to find seats
    booked_seats = []
    for i, row in enumerate(train_coach):
        available_seats = [index for index, seat in enumerate(row) if seat == 0]
        
        # Check if enough seats are available in the current row
        if len(available_seats) >= num_seats:
            for j in range(num_seats):
                train_coach[i][available_seats[j]] = 1
                # Add seat number to the booked list
                seat_number = i * 7 + available_seats[j] + 1  # Calculate the seat number
                booked_seats.append(seat_number)
            break  # Stop once seats are booked
        else:
            # If not enough seats in one row, book as many as possible and move to the next row
            for seat in available_seats:
                if len(booked_seats) < num_seats:
                    train_coach[i][seat] = 1
                    seat_number = i * 7 + seat + 1
                    booked_seats.append(seat_number)
            # Continue to the next rows if seats still need to be booked
    
    if len(booked_seats) == num_seats:
        print(f"Successfully booked {num_seats} seat(s): {booked_seats}")
    else:
        print(f"Could not book {num_seats} seat(s). Only booked {len(booked_seats)} seats: {booked_seats}")
    
    display_seats(train_coach)
    return booked_seats

# Function to handle user input for booking
def main():
    while True:
        display_seats(train_coach)  # Display current seating arrangement
        try:
            seats_to_book = int(input("Enter the number of seats to book (1-7): "))
            if seats_to_book < 1 or seats_to_book > 7:
                print("Please enter a valid number of seats (1-7).")
                continue
            book_seats(seats_to_book)
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        # Ask if the user wants to book more seats
        more_booking = input("Do you want to book more seats? (yes/no): ").strip().lower()
        if more_booking != 'yes':
            break

if __name__ == "__main__":
    main()
