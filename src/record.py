from typing import Optional, List, Dict


class Record:
    def __init__(self) -> None:
        self.first_name: Optional[str] = None
        self.last_name: Optional[str] = None
        self.age: Optional[int] = None
        self.phone_number: Optional[str] = None

    @staticmethod
    def prompt_for_number(prompt_text: str, error_text: str) -> int:
        """
        Continuously prompt the user until a valid integer is entered.

        :param prompt_text: The text displayed when asking for input.
        :param error_text: The error message displayed if the input is invalid.
        :return: The valid integer input by the user.
        """
        while True:
            try:
                number = int(input(prompt_text))
                return number
            except ValueError:
                print(error_text)

    @staticmethod
    def prompt_for_text(prompt_text: str, error_text: str) -> str:
        """
        Continuously prompt the user until a valid string without numbers is entered.

        :param prompt_text: The text displayed when asking for input.
        :param error_text: The error message displayed if the input is invalid.
        :return: The valid text input by the user.
        """
        while True:
            text = input(prompt_text)
            if text.isalpha():
                return text
            else:
                print(error_text)

    @staticmethod
    def list_users(database: List[Dict[str, str]]) -> None:
        """
        Retrieve and display all insured persons from the in-memory database.

        :param database: A list of dictionaries to store user records.
        """
        for user in database:
            print(f"{user['first_name']}\t{user['last_name']}\t{user['age']}\t{user['phone_number']}")
        input("Press ENTER to continue...")


    def add_user(self, database: List[Dict[str, str]]) -> None:
        """
        Collect information from the user and add a new insured person to the in-memory database.

        :param database: A list of dictionaries to store user records.
        """
        self.first_name = self.prompt_for_text("Enter the first name of the insured person: ",
                                               "Invalid input! Name must contain only letters.")
        self.last_name = self.prompt_for_text("Enter the last name: ",
                                              "Invalid input! Last name must contain only letters.")
        self.age = self.prompt_for_number("Enter age: ", "Invalid input! Age must be a number.")
        self.phone_number = self.prompt_for_text("Enter phone number: ",
                                                 "Invalid input! Phone number must be a string.")

        new_user = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'phone_number': self.phone_number
        }
        database.append(new_user)
        input("Data has been saved. Press ENTER to continue...")

    def search_user(self, database: List[Dict[str, str]]) -> None:
        """
        Search for an insured person in the in-memory database using their first and last name.

        :param database: A list of dictionaries to store user records.
        """
        first_name = self.prompt_for_text("Enter the first name of the insured person: ",
                                          "Invalid input! Name must contain only letters.")
        last_name = self.prompt_for_text("Enter the last name: ", "Invalid input! Last name must contain only letters.")

        found_users = [user for user in database if user['first_name'] == first_name and user['last_name'] == last_name]
        for user in found_users:
            print(f"{user['first_name']}\t{user['last_name']}\t{user['age']}\t{user['phone_number']}")
        if not found_users:
            print("No users found.")
        input("Press ENTER to continue...")


    def display_menu(self, database: List[Dict[str, str]]) -> None:
        """
        Present a menu of actions for the user to choose from.

        :param database: A list of dictionaries to store user records.
        """
        while True:
            print("\n------------------------------")
            print("Insurance Record")
            print("------------------------------")
            print("Select an action: ")
            print("1 - Add a new insured person")
            print("2 - List all insured persons")
            print("3 - Search for an insured person")
            print("4 - Exit")
            action_number = self.prompt_for_number("Your choice: ",
                                                   "Invalid input! Please enter a number between 1 and 4.")

            if action_number == 1:
                self.add_user(database)
            elif action_number == 2:
                self.list_users(database)
            elif action_number == 3:
                self.search_user(database)
            elif action_number == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice! Please select a valid option.")

    def run(self, database: List[Dict[str, str]]) -> None:
        """
        Run the main loop for user interaction, allowing selection of various actions.

        :param database: A list of dictionaries to store user records.
        """
        self.display_menu(database)
