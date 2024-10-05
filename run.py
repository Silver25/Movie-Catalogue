# Library to include timing/delay options in code
import time
# Library essential for interacting with Google Sheets
import gspread
# Authentication to access and interact with Google Sheets
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Constant variables for credentials and path of Google sheet
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('dvdcollector')

def menu():
    """
    Main function of the app!
    Hold all elements from Menu within separate code blocks
    and functionality for every option.
    """
    menu = True
    while menu:   # building app Menu with options to choose from
        print("""
      Menu:
      1.List the Records
      2.Add a Record
      3.Edit a Record
      4.Delete a Record
      5.Exit/Quit
      """)
        choice = input("What would you like to do? ")  # expected user action

        if choice == "1":
            print("\n >>> All records Listed!")
            movies = SHEET.worksheet('movies')  # connecting to Google sheet
            data = movies.get_all_values()  # collecting all records from sheet

            for item in data:
                print(f"{item[0]}")  # display of records in terminal

        elif choice == "2":
            sheet = SHEET.worksheet('movies')
            data = input("Enter the name of the movie: ")
            sheet.append_row([data])
            print("\n >>> New Record Added!")

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
            time.sleep(3)  # Delay for 3 seconds
            continue


if __name__ == "__main__":
    menu()
