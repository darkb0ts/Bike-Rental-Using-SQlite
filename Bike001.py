import sqlite3
conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("CREATE TABLE bikes (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,NumofBike INT)")
cur.close()
class BikeRental:
    def __init__(self,bike):
        self.bike=bike
        self.rental=0
    def print_menu(self):
        print("1. Create")
        print("2. Display")
        print("3. Update")
        print("4. Delete")
        print("5. Quit")
        print("6 Return Bike")
    def Create(self):
        name=input("Enter the Username: ")
        NumofBike=input("Enter the Num of Bike: ")
        try:
            NumofBike =int(NumofBike)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO bike (name, NumofBike) VALUES (?, ?)", (name,NumofBike))
            conn.commit()
            conn.close()
        except:
            print("Invaild the Number of Bikes")
    def display(self):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM bikes")
        cur.close()
    def ReturnBike(self):
        IDnumber=input('Enter the ID number: ')
        try:
            IDnumber=int(IDnumber)
            cursor=conn.cursor()
            cursor.execute("select * from bikes WHERE id = ?", (IDnumber))
            store = cursor.fetchone()
            print("ID number :{} Username : {} Number of Bike : {}".format(store[0],store[1],store[2]*5))
            conn.close()
        except:
            print('INVAILD ID NUMBER ')

    def update(self):
        IDnumber=input('Enter the ID number: ')
        name=input("Enter the Username: ")
        NumofBike=input("Enter the Num of Bike: ")
        try:
            IDnumber=int(IDnumber)
            cursor=conn.cursor()
            cursor.execute("UPDATE bike set name = ?,NumofBike = ? WHERE id = ?", (name,NumofBike,IDnumber))
            conn.close()
        except:
            print('INVAILD ID NUMBER ')
    def Delete(self):
        IDnumber=input('Enter the ID number: ')
        try:
            IDnumber=int(IDnumber)
            cursor=conn.cursor()
            cursor.execute("DELETE FROM BIKE WHERE id = ?",(IDnumber))
            conn.close()
        except:
            print('INVAILD ID NUMBER ')
    def Quit(self):
        quit



        