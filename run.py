
import time

def menu():
    """
    """
    menu = True
    while menu:
        print("""
      Menu:
      1.List the Records
      2.Add a Record
      3.Edit a record
      4.Delete a Record
      5.Exit/Quit
      """)
        choice = input("What would you like to do? ")
        if choice == "1":
            print("\n >>> Records Listed!")
        elif choice == "2":
            print("\n >>> Record Added!")
        elif choice == "3":
            print("\n >>> Record Edited!")
        elif choice == "4":
            print("\n >>> Record Deleted!")
        elif choice == "5":
            print("\n >>> Closing app!")
            time.sleep(3)  # Delay for 3 seconds
            print("\n Goodbye")
            break
        else:
            print("\n >>> Not Valid Choice. Try again!")
            continue
        
if __name__ == "__main__":
    menu()

