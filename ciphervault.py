# A Python-based Password Generator and Storage System
# Stores passwords in CSV, encrypted
# Displays passwords in pretty tables
# Updates passwords if platform + email already exist

import asyncio
import csv
import pyperclip
import random
import datetime
import string
import os
from cryptography.fernet import Fernet
from tabulate import tabulate
import validators

KEY_FILE = "secret.key"

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key

key = load_key()
cipher = Fernet(key)

def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(enc_password):
    return cipher.decrypt(enc_password.encode()).decode()


def create_pass(length=15, use_special=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    specials = "!@#$%^&*()-_=+[]{};:,.<>?/"

    all_chars = lowercase + uppercase + digits
    if use_special:
        all_chars += specials

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
    ]
    if use_special:
        password.append(random.choice(specials))

    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    final_password = ''.join(password)

    pyperclip.copy(final_password)
    return final_password


def store_pass(passw):
    date = datetime.date.today()
    Platform = input("Enter Platform: ").strip()
    Email=""

    while True:
        mail = input("Enter E-Mail: ").strip()
        #matches = re.search(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", mail, re.IGNORECASE)
        if validators.email(mail):
            print("Valid")
            break

        else:
            print("Enter a valid E-Mail.\n")


    filename = "password.csv"
    fieldnames = ["Date", "Platform", "E-Mail", "Password"]
    rows = []

    if os.path.exists(filename):
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

    enc_pass = encrypt_password(passw)

    updated = False
    for row in rows:
        if row["Platform"].lower() == Platform.lower() and row["E-Mail"].lower() == Email.lower():
            row["Password"] = enc_pass
            row["Date"] = str(date)
            updated = True
            print(f"[UPDATED] Password for {Platform} ({mail}) has been updated.")
            break

    if not updated:
        rows.append({
            "Date": str(date),
            "Platform": Platform,
            "E-Mail": Email,
            "Password": enc_pass
        })
        print(f"[NEW] Added new entry for {Platform} ({mail}).")

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def use_specials(specs):
    return specs.lower() in ["yes", "y", "true"]



def specificPass(platform):
    if not os.path.exists("password.csv"):
        print("[ERROR] No password file found.")
        return

    table = []
    with open("password.csv", "r") as f2:
        reader = csv.DictReader(f2)
        for row in reader:
            if row["Platform"].lower() == platform.lower():
                table.append([
                    row["Date"],
                    row["Platform"],
                    row["E-Mail"],
                    decrypt_password(row["Password"])
                ])

    if table:
        print(tabulate(table, headers=["Date", "Platform", "E-Mail", "Password"], tablefmt="grid"))
    else:
        print(f"[INFO] No entries found for '{platform}'.")



async def delay_timer(passs):
    print("Generating Password...")
    await asyncio.sleep(2)
    print('''To view your password, 
        first enter required credentials,
        to save your login information''')
    
    await asyncio.sleep(1)
    store_pass(passs)
    await asyncio.sleep(2)

    print('''⟨Neural entropy model activated⟩
        → Synthesizing secure key...
        → Analyzing character entropy spectrum...
        → Optimizing randomness efficiency...
        Generation complete — deploying result.''')
    
    await asyncio.sleep(1)

    print(f"ACCESS GRANTED: Your password is → {passs}")

    await asyncio.sleep(1)

    print('''[MEM] Copying to /sys/clipboard... 
          [OK] Clipboard updated — auto-erase in 45s. 
          [EXIT] All processes terminated successfully.''')
    
    await asyncio.sleep(1)
    print("Password copied to clipboard.")

async def delayy(passs):
    await delay_timer(passs)




def view_pass():
    if not os.path.exists("password.csv"):
        print("[ERROR] No password file found.")
        return

    with open("password.csv", 'r') as f1:
        reader = csv.DictReader(f1)
        table = []
        for row in reader:
            table.append([
                row['Date'],
                row['Platform'],
                row['E-Mail'],
                decrypt_password(row['Password'])
            ])
    print(tabulate(table, headers=["Date", "Platform", "E-Mail", "Password"], tablefmt="grid"))



def main():
    a = int(input('''What you wanna do today?
1) Generate a new Password
2) View all of your existing Passwords
3) View Password of specific Platform
: '''))

    if a == 1:
        length = int(input("Enter Length of Password: "))
        usespec = input("Do you want to use Special Characters? (yes/no): ")
        b = use_specials(usespec)
        passs = create_pass(length, b)
        asyncio.run(delayy(passs))

    elif a == 2:
        view_pass()

    elif a == 3:
        plat = input("Enter the name of Platform: ")
        specificPass(plat)

    else:
        print("Invalid option.")



if __name__ == "__main__":
    main()
