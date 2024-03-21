from Bike001 import BikeRental
obj=BikeRental(100)
def main():
    while True:
        obj.print_menu()
        choice=int(input('Enter the choice Your want: '))
        if choice==1:
            obj.Create()
        elif choice==2:
            obj.display()
        elif choice==3:
            obj.update()
        elif choice==4:
            obj.Delete()
        elif choice==5:
            obj.Quit()
        elif choice==6:
            obj.ReturnBike()
        else:
            print("No Output")
if __name__=="__main__":
    main()


