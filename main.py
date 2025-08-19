# Show Welcome message
print("WELCOME TO MEST ATM")
print("Please insert your atm card")
# Ask user to insert the card
user_card_name = input("Enter your name>> ") 
user_card_number = int(input("Enter your serial number>> "))
# Ask user to enter their pin
user_pin = 4190
current_balance = 10000.00

def pin_authentication():
    while True:
        pin = int(input("Enter your pin>> "))
        try:
            if pin == user_pin:
                print("Login Successful")
                break
            else:
                print("Authentication Failed")
                
        except ValueError:

            print("Invalid pin - Try again!")
    return pin        
    
pin_authentication()

def withdrawal():
    global current_balance
    amount = float(input("Enter the amount>> ")) 
    if amount <= 0:
        print("invalid input")
        
    if amount <= current_balance:
        current_balance -= amount
        print("withdrawal successful, please take your cash.")
    else:
        print("Insufficient balance")    

# Display options
def choices():
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Transaction History")
    print("5. Exit")

    options = input("Choose an option>> ")
    if options == "1":
        print(f"Your balance is Ghs {current_balance}")
    elif options == "2":
        print("Ready to Deposit") 
    elif options == "3":
        withdrawal()
    elif options == "4":
        print("History")  
    elif options == "5":
        print("Exit")
    else:
        print("Choose from the options")

choices()

from datetime import datetime, date

# --- Google Sheets Settings (optional) ---
SHEETS_ENABLED = False           # Set to True after you configure gspread
SHEET_ID = "PUT_YOUR_SPREADSHEET_ID_HERE"
WORKSHEET = "Transactions"
SERVICE_ACCOUNT_FILE = "service_account.json"  # path to your credentials JSON
CSV_FALLBACK_FILE = "transactions.csv"

gspread = None
if SHEETS_ENABLED:
    try:
        import gspread  # type: ignore
    except Exception:
        print("gspread not available, falling back to CSV logging.")
        SHEETS_ENABLED = False

# Try to set up Google Sheets if enabled
gs_client = None
gs_ws = None
if SHEETS_ENABLED:
    try:
        gs_client = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
        sh = gs_client.open_by_key(SHEET_ID)
        try:
            gs_ws = sh.worksheet(WORKSHEET)
        except Exception:
            gs_ws = sh.add_worksheet(title=WORKSHEET, rows="1000", cols="6")
            gs_ws.append_row(["Timestamp", "Type", "Amount", "Balance After"])
    except Exception as e:
        print(f"Google Sheets setup failed ({e}). Falling back to CSV.")
        gs_client = None
        gs_ws = None

# --- App State ---
transactions = []   # list of dicts: {"time": "...", "type": "DEPOSIT/WITHDRAW", "amount": x, "balance": y}
daily_withdrawn = 0.0
daily_limit = 2000.0
last_withdraw_date = date.today()






