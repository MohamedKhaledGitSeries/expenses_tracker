import json
import os
import math


def load_expenses():
   try:
     valid_expense = []
     with open("expenses.json", "r") as file:
        expenses = json.load(file)
        if isinstance(expenses, list):
           for expense in expenses:
              if not isinstance(expense, dict):
                continue
              else:
                if not ("name" in expense and "amount" in expense and "category" in expense):
                  continue
                else:
                   n = expense["name"]
                   c = expense["category"]
                   if not isinstance(n, str):
                      continue
                   elif not n.strip():
                      continue
                   elif not isinstance(expense["amount"], (int, float)) or isinstance(expense["amount"], bool) or not expense["amount"] > 0:
                      continue
                   elif not isinstance(c, str):
                      continue
                   if not c.strip():
                      continue
                   elif math.isfinite(expense["amount"]):
                      valid_expense.append(expense)
        else :
          return []
           
        return valid_expense
   except FileNotFoundError:
     return []

   except json.JSONDecodeError:
     return []
   

expenses = load_expenses()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def save_expenses(expenses):
   with open("expenses.json", "w") as file:
      json.dump(expenses, file, indent=4)

def save_currency(currency):
   settings = {"currency": currency}
   with open("settings.json", "w") as file:
    json.dump(settings, file, indent=4)

def ask_for_currency():
   while True:
     currency = input("Please enter your country currency : ").strip()
     if not currency == "":
       if currency.isdigit():
         print("\n Currency cannot be numeric, try USD, EUR ... \n")
         continue
       else:
         save_currency(currency)
         clear_screen()
         return currency
     else:
        continue

def load_currency():
   try:
      with open("settings.json", "r") as file:
         settings = json.load(file)
         if not isinstance(settings, dict):
            tmp_cur = ask_for_currency()
            return tmp_cur
         elif not "currency" in settings:
          tmp_cur = ask_for_currency()
          return tmp_cur
         
         elif not isinstance(settings["currency"], str):
            tmp_cur = ask_for_currency()
            return tmp_cur

         elif not settings["currency"].strip() == "":
            return settings["currency"].strip()
         else:
            tmp_cur = ask_for_currency()
            return tmp_cur
   except FileNotFoundError:
      tmp_cur = ask_for_currency()
      return(tmp_cur)
   except json.JSONDecodeError:
      tmp_cur = ask_for_currency()
      return(tmp_cur)


def add_expense():
    print("\nYou selected: Add Expense\n")

    while True:
        while True:
            clear_screen()
            print("\n===== ADDING EXPENSES =====\n")
            new_expense_name = input("New expense name: ").strip()
            if not new_expense_name:
                print("You entered an empty name!")
                continue

            try:
                float(new_expense_name)
                print("Name Cannot Be Numeric!")
            except ValueError:
                break
        while True:
            try:
                new_expense_amount = float(
                    input("\nNew expense amount: ").strip()
                )

                if not math.isfinite(new_expense_amount) or new_expense_amount <= 0:
                    print("Invalid Amount!")
                    continue

                break

            except ValueError:
                print("Invalid Amount!")

        while True:
            new_expense_category = input(
                "\nNew expense category: "
            ).strip()

            if not new_expense_category:
                print("\nCategory Cannot Be Empty!")
                continue

            try:
                float(new_expense_category)
                print("\nCategory Cannot Be Numeric!")
            except ValueError:
                break

        tmp_expense = {
            "name": new_expense_name,
            "amount": new_expense_amount,
            "category": new_expense_category
        }

        expenses.append(tmp_expense)
        save_expenses(expenses)

        print("\nExpense Added Successfully!\n")

        while True:
            con = input(
                "Do you want to add another expense? (Y/N): "
            ).strip().upper()

            if con == "Y":
                break

            elif con == "N":
                clear_screen()
                return

            else:
                print("\nInvalid input! Please enter Y or N.")



def edit_expense():
   print("\n")
   expense_number = 1
   if len(expenses) > 0:
    for expense in expenses:
       print(expense_number, ". " ,f"Name: {expense['name']} | Amount: {expense['amount']} | Category: {expense['category']}", "\n")    
       expense_number += 1
    while True:
       choice = input("Enter Expense Number: ")

       try:
          choice = int(choice) - 1
          if 0 <= choice < len(expenses):
              print("You selected Expense Number:", expenses[choice]["name"])
              break
          else:
              print("Expense Not Found!")
              continue
          

       except ValueError:
           print("You Entered Invalid Number!")
           continue
       

    if 0 <= choice < len(expenses):
       clear_screen()
       print("You selected Expense Number: ", expenses[choice]["name"])
       loop = True
       while loop:
            print("\n")
            print("===== Edit Expense =====")
            print("1. Edit Expense Name")
            print("2. Edit Expense Amount")
            print("3. Edit Expense Category")
            print("4. Delete Expense")
            print("5. Return To Main Menu")
            print("\n")

            choice1 = input("Select Something To edit: ")

            if choice1 == "1":
               while True:
                print("\n")
                new_name = input("Enter A New Name : ").strip()
                if not new_name:
                   print("\n Name cannot be empty!")
                   continue
                else:
                 try:
                     float(new_name)
                     print("\nName cannot be numeric!")
                     continue
                 except ValueError:
                 
                  expenses[choice]["name"] = new_name
                  print("\n" ,"Name Changed Successfuly!", "\n")
                  save_expenses(expenses)
                  break

            elif choice1 == "2":
             while True:
              new_amount = input("\n Enter A New Amount: ")
              try:
                new_amount = float(new_amount)

                if math.isfinite(new_amount) and new_amount > 0:
                   expenses[choice]["amount"] = new_amount
                   save_expenses(expenses)
                   print("\n Amount Changed Successfully!")
                   break
                else:
                  print("\n Invalid Amount!")
                  continue

              except ValueError:
                  print("\n Please Enter A Valid Number!")
                  continue

            elif choice1 == "3":
               while True:
                print("\n")
                new_category = input("Enter A New Category : ").strip()
                if not new_category:
                   print("\n Category cannot be empty!")
                   continue
                else:
                 try:
                     float(new_category)
                     print("\n Category cannot be numeric!")
                     continue
                 except ValueError:
                 
                  expenses[choice]["category"] = new_category
                  print("\n" ,"Category Changed Successfuly!", "\n")
                  save_expenses(expenses)
                  break

            elif choice1 == "4":
               delete_expense(choice)
               break

            elif choice1 == "5":
               clear_screen()
               break

            else:
               print("\n Invalid Choice!")

    else:
       print("Expense Not Found!")

   else:
      print("No Expenses Found!")    

def delete_expense(num):
   while True:
    case = input("Are you sure you want to delete this expense? (Y/N): ")
    case = case.strip().upper()

    if case == "Y":
        expenses.pop(num)
        save_expenses(expenses)
        print("\nExpense Deleted Successfully!\n")
        break

    elif case == "N":
        print("\nDeletion Cancelled!\n")
        break

    else:
        print("\nInvalid input! Please enter Y or N.\n")

currency = load_currency()

while True:
    print("\n")
    print("===== EXPENSE TRACKER ===== \n")
    print("1. Add an Expense")
    print("2. Manage Expenses")
    print("3. Show All Expenses")
    print("4. Calculate Total Expenses")
    print("5. Show Expenses by Category")
    print("6. Calculate Expenses by Category")
    print("7. Calculate Average Expenses")
    print("8. Show Highest Expense")
    print("9. Show Lowest Expense")
    print("10. Exit")
    print(f"\n Note : You are using {currency} as a currency for your expenses \n")
    print("=========================== \n")

    choice = input("Choose an option: ")

    if choice == "10":
        print("\n", "Goodbye! \n")
        break


    elif choice == "1":
        add_expense()

    elif choice == "2":
       edit_expense()


    elif choice == "3":
     while True:
        clear_screen()
        print("\n===== ALL EXPENSES =====\n")
        i = 1

        if len(expenses) > 0:
            for expense in expenses:
                print(
                    f"{i:02d}. Name: {expense['name']} | "
                    f"Amount: {expense['amount']} {currency} | "
                    f"Category: {expense['category']}\n"
                )
                i += 1
        else:
            print("\nNo Expenses Found!")

        choic = input("Do you want to go back? (Y/N): ").strip().upper()

        if choic == "Y":
            clear_screen()
            break
        elif choic == "N":
            continue
        else:
            print("\nInvalid input! Please enter Y or N.")
            input("Press Enter to continue...")
            clear_screen()


    elif choice == "4":
      while True:
        clear_screen()
        print("\n===== TOTAL EXPENSES =====\n")

        total_expenses = sum(
            expense["amount"] for expense in expenses
        )

        print(f"Total Expenses: {total_expenses:.2f} {currency}")

        choice_back = input(
            "\nDo you want to go back? (Y/N): "
        ).strip().upper()

        if choice_back == "Y":
            clear_screen()
            break
        elif choice_back == "N":
            continue
        else:
            print("\nInvalid input! Please enter Y or N.")
            input("Press Enter to continue...")


    
    elif choice == "5":
      while True:
        clear_screen()
        print("\n===== EXPENSES BY CATEGORY =====\n")

        cat = input("Enter the category: ").strip()

        found = False

        for expense in expenses:
            if expense["category"].lower() == cat.strip().lower():
                print(
                    f"Name: {expense['name']} | "
                    f"Amount: {expense['amount']} {currency} | "
                    f"Category: {expense['category']}\n"
                )
                found = True

        if not found:
            print("\nNo Expenses Found in This Category!")

        choice_back = input(
            "\nDo you want to go back? (Y/N): "
        ).strip().upper()

        if choice_back == "Y":
            clear_screen()
            break
        elif choice_back == "N":
            continue
        else:
            print("\nInvalid input! Please enter Y or N.")
            input("Press Enter to continue...")


    
    
    elif choice == "6":
     while True:
        clear_screen()
        print("\n===== TOTAL EXPENSES BY CATEGORY =====\n")

        expense_category = input(
            "Enter the category: "
        ).strip()

        found = False
        total_expenses = 0

        for expense in expenses:
            if expense["category"].strip().casefold() == expense_category.casefold():
                total_expenses += expense["amount"]
                found = True

        if found:
            print(
                f"\nTotal Expenses for {expense_category}: "
                f"{total_expenses:.2f} {currency}"
            )
        else:
            print("\nNo Expenses Found in This Category!")

        choice_back = input(
            "\nDo you want to go back? (Y/N): "
        ).strip().upper()

        if choice_back == "Y":
            clear_screen()
            break
        elif choice_back == "N":
            continue
        else:
            print("\nInvalid input! Please enter Y or N.")
            input("Press Enter to continue...")

      
    elif choice == "7":
     while True:
        clear_screen()
        print("\n===== AVERAGE EXPENSES =====\n")

        if len(expenses) > 0:
            average = sum(
                expense["amount"] for expense in expenses
            ) / len(expenses)

            print(
                f"Average Expenses: {average:.2f} {currency}"
            )
        else:
            print("\nNo Expenses Found!")

        choice_back = input(
            "\nDo you want to go back? (Y/N): "
        ).strip().upper()

        if choice_back == "Y":
            clear_screen()
            break
        elif choice_back == "N":
            continue
        else:
            print("\nInvalid input! Please enter Y or N.")
            input("Press Enter to continue...")



    
    elif choice == "8":
     while True:
        clear_screen()
        print("\n===== HIGHEST EXPENSE =====\n")

        if len(expenses) > 0:
            highest_expense = max(
                expenses, key=lambda expense: expense["amount"]
            )

            print(
                f"Name: {highest_expense['name']}\n"
                f"Amount: {highest_expense['amount']:.2f} {currency}\n"
                f"Category: {highest_expense['category']}"
            )
        else:
            print("\nNo Expenses Found!")

        choice_back = input(
            "\nDo you want to go back? (Y/N): "
        ).strip().upper()

        if choice_back == "Y":
            clear_screen()
            break
        elif choice_back == "N":
            continue
        else:
            print("\nInvalid input! Please enter Y or N.")
            input("Press Enter to continue...")


    
    elif choice == "9":
     while True:
        clear_screen()
        print("\n===== LOWEST EXPENSE =====\n")

        if len(expenses) > 0:
            lowest_expense = min(
                expenses, key=lambda expense: expense["amount"]
            )

            print(
                f"Name: {lowest_expense['name']}\n"
                f"Amount: {lowest_expense['amount']:.2f} {currency}\n"
                f"Category: {lowest_expense['category']}"
            )
        else:
            print("\nNo Expenses Found!")

        choice_back = input(
            "\nDo you want to go back? (Y/N): "
        ).strip().upper()

        if choice_back == "Y":
            clear_screen()
            break
        elif choice_back == "N":
            continue
        else:
            print("\nInvalid input! Please enter Y or N.")
            input("Press Enter to continue...")
    else:
       print("\nInvalid Choice! Please select from 1 to 10.")

