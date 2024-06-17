class Star_Cinema:
    __hall_list = []  # class attribute to hold all hall objects

    @staticmethod
    def entry_hall(hall):
        Star_Cinema.__hall_list.append(hall)

    @staticmethod
    def view_hall_list():
        return Star_Cinema.__hall_list


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        self.__seats = {}  # Dictionary to hold seats 
        self.__show_list = []  # List to hold tuples 

        Star_Cinema.entry_hall(self)  # insert hall object into the Star_Cinema hall_list

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)  # create a tuple

        self.__show_list.append(show_info)

        seats_allocation = [[0] * self.cols for _ in range(self.rows)]   # seats with rows and cols

        self.__seats[show_id] = seats_allocation  # make a key with show_id

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            raise ValueError("Invalid show ID")

        for seat in seat_list:
            row, col = map(int, seat.split(','))

            if self.__seats[show_id][row][col] == 1:
                raise ValueError(f"Seat ({row}, {col}) is already booked")
            else:
                self.__seats[show_id][row][col] = 1  # booking seat

    def view_show_list(self):
        return self.__show_list

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            raise ValueError("Invalid show ID")

        else:
            seats_matrix = self.__seats[show_id]
            available_seats = []
            for row in range(self.rows):
                for col in range(self.cols):
                    if seats_matrix[row][col] == 0:
                        available_seats.append((row, col))

            return seats_matrix, available_seats


def main():
    Cinema_hall = Hall(5, 5, 'Classic_1')

    Cinema_hall.entry_show('Show_1', 'Avenger Infinity War', '10:00 AM')
    Cinema_hall.entry_show('Show_2', 'Spider Man No Way Home', '02:00 PM')

    while True:
        print("\nOptions:")
        print("1. View Movie Information")
        print("2. View Available Seats")
        print("3. Book Seats")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nMovie Information:")
            hall_list = Star_Cinema.view_hall_list()
            for hall in hall_list:
                print(f"\nHall No: {hall.hall_no}")
                show_list = hall.view_show_list()
                for show in show_list:
                    print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

        elif choice == '2':
            show_id = input("\nEnter show ID to view available seats: ")
            hall_list = Star_Cinema.view_hall_list()
            for hall in hall_list:
                try:
                    seats_matrix, available_seats = hall.view_available_seats(show_id)
                    print(f"\nAvailable Seats for {show_id}:")
                    for row in seats_matrix:
                        print(row)
                    print("Available Seats:", available_seats)
                except ValueError as Error:
                    print(Error)

        elif choice == '3':
            show_id = input("\nEnter show ID to book seats: ")
            seat_input = input("Enter seat numbers to book (Exmple: 0,0 1,1 2,2): ")
            seats_to_book = seat_input.split()
            hall_list = Star_Cinema.view_hall_list()
            for hall in hall_list:
                try:
                    hall.book_seats(show_id, seats_to_book)
                    print(f"Successfully booked seats for show {show_id}.")
                except ValueError as Error:
                    print(Error)

        elif choice == '4':
            print("Exiting......")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__": #control main function calling
    main()
