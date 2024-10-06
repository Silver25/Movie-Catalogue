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
    # building app Menu with options to choose from
    while menu:
        print("""
      Menu:
      1.List the Records
      2.Add a Record
      3.Delete a Record
      4.Exit/Quit
      """)
        choice = input("What would you like to do? ")

        if choice == "1":
            print("\n >>> All records Listed!")
            # connecting to Google sheet
            movies = SHEET.worksheet('movies')
            # collecting all records from the sheet
            data = movies.get_all_values()

            for item in data:  # loop through each row in the sheet
                movie_title = item[0].title()  # convert to title case
                print(movie_title)
            time.sleep(2)  # delay for 2 seconds

        elif choice == "2":
            new_movie = SHEET.worksheet('movies')
            while True:  # loop to check if input is valid
                data = input("Enter the name of the movie: ")
                if data:
                    break
                else:
                    print("Movie name cannot be empty.")
            # update sheet with the new row of data
            new_movie.append_row([data])
            print("\n >>> New Record Added!")

        elif choice == "3":
            worksheet = SHEET.get_worksheet(0)
            # Get all the values in the sheet
            data = worksheet.get_all_values()

            # Define the word to delete
            while True:  # loop to check if input is valid
                word_to_delete = input("Enter the title you want to delete: ")
                if word_to_delete:
                    break
                else:
                    print("Movie name cannot be empty.")
            # Iterate through all cells and delete the word
            for i, row in enumerate(data):
                for j, cell in enumerate(row):
                    if word_to_delete in cell:
                        data[i][j] = cell.replace(word_to_delete, '')

            # Update the sheet with the modified data
            worksheet.update('A1', data)
            print("\n >>> Record Deleted!")

        elif choice == "4":
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
