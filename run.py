import time

menu=True
while menu:
    print ("""
    Menu:
    1.Add a Record
    2.Delete a Record
    3.List the Records
    4.Exit/Quit
    """)
    menu=input("What would you like to do? ") 
    if menu=="1": 
      print("\n >>> Record Added!") 
    elif menu=="2":
      print("\n >>> Record Deleted!") 
    elif menu=="3":
      print("\n >>> Records Listed!") 
    elif menu=="4":
      print("\n >>> Closing app!")
      time.sleep(3)  # Delay for 3 seconds
      print("\n Goodbye") 
      break
    elif menu!="":
      print("\n >>> Not Valid Choice Try again!") 