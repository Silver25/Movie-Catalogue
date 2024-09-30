
import time

menu=True
while menu:
    print ("""
    Menu:
    1.List the Records
    2.Add a Record
    3.Edit a record
    4.Delete a Record
    5.Exit/Quit
    """)
    menu=input("What would you like to do? ") 
    if menu=="1": 
      print("\n >>> Records Listed!") 
    elif menu=="2":
      print("\n >>> Record Added!") 
    elif menu=="3":
      print("\n >>> Record Edited!") 
    elif menu=="4":
      print("\n >>> Record Deleted!")
    elif menu=="5":
      print("\n >>> Closing app!")
      time.sleep(3)  # Delay for 3 seconds
      print("\n Goodbye") 
      break
    else:
      print("\n >>> Not Valid Choice. Try again!") 