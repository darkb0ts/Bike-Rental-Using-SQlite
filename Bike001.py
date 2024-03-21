import sqlite3
import random
conn = sqlite3.connect("database.db")
# cur = conn.cursor()
# cur.execute("CREATE TABLE bikes (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, NumofBike INT, ID_number INT)")
# conn.commit()
# conn.close()
class BikeRental:
    def __init__(self, bike):
        self.bike = bike
        self.rental = 0

    def print_menu(self):
        print("1. Create")
        print("2. Display")
        print("3. Update")
        print("4. Delete")
        print("5. Return Bike")
        print("6. Quit")

    def Create(self):
        name = input("Enter the Username: ")
        NumofBike = input("Enter the Num of Bike: ")
        cursor = None  # Initialize cursor to None

        try:
            NumofBike = int(NumofBike)
        except ValueError as e:
            print("Error converting NumofBike to integer:", e)
            return

        try:
            random_number = random.randint(1, 100)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO bikes (name, NumofBike, ID_number) VALUES (?, ?, ?)", (name, NumofBike, random_number))
            conn.commit()
            print("Successfully taken {} bike(s) and your ID is {}".format(NumofBike, random_number))
        except Exception as e:
            print("An error occurred:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def display(self):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM bikes")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()

    def ReturnBike(self):
        IDnumber = input('Enter the ID number: ')
        try:
            IDnumber = int(IDnumber)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bikes WHERE ID_number = ?", (IDnumber,))
            store = cursor.fetchone()
            if store:
                print("ID number: {}, Username: {}, Number of Bikes: {}".format(store[0], store[1], store[2] * 5))
            else:
                print("ID number not found")
            conn.close()
        except ValueError:
            print('INVALID ID NUMBER')

    def update(self):
        IDnumber = input('Enter the ID number: ')
        name = input("Enter the Username: ")
        NumofBike = input("Enter the Num of Bike: ")
        try:
            IDnumber = int(IDnumber)
            cursor = conn.cursor()
            cursor.execute("UPDATE bikes SET name = ?, NumofBike = ? WHERE ID_number = ?", (name, NumofBike, IDnumber))
            conn.close()
        except ValueError:
            print('INVALID ID NUMBER')

    def Delete(self):
        IDnumber = input('Enter the ID number: ')
        try:
            IDnumber = int(IDnumber)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM bikes WHERE ID_number = ?", (IDnumber,))
            conn.close()
        except ValueError:
            print('INVALID ID NUMBER')

    def Quit(self):
        quit()



        
