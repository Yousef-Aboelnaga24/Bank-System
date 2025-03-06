class Bank:
    def __init__(self, balance):
        self.__balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'\n✅ Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}\n')
        else:
            print("\n❌ Invalid deposit amount!\n")

    # Withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            print(f'\n❌ Insufficient funds. Your balance: ${self.__balance:.2f}\n')
        elif amount > 0:
            self.__balance -= amount
            print(f'\n✅ Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}\n')
        else:
            print("\n❌ Invalid withdrawal amount!\n")

    # Transfer money
    def transfer(self, amount, recipient):
        if not isinstance(recipient, Bank):  # التأكد من أن المستلم كائن من Bank
            print("\n❌ Invalid recipient!\n")
            return
        
        if amount > self.__balance:
            print(f'\n❌ Insufficient funds. Your balance: ${self.__balance:.2f}\n')
        elif amount > 0:
            self.__balance -= amount
            recipient.__balance += amount
            print(f'\n✅ Transferred ${amount:.2f} successfully. Your new balance: ${self.__balance:.2f}\n')
        else:
            print("\n❌ Invalid transfer amount!\n")

    # Display balance
    def display(self):
        print(f'\n📊 Current balance: ${self.__balance:.2f}\n')


# إنشاء حسابات للمستخدمين
users = {
    'yousef': Bank(1200),
    'mohanad': Bank(200),
    'marwan': Bank(850),
    'moaaz': Bank(700),
    'shehap': Bank(600),
    'abdelrihem': Bank(950),
    'abdulallah': Bank(8500),
}

print("\n👥 Available Users:", list(users.keys()), "\n")

while True:
    user = input("Enter your username: ").strip().lower()

    if user not in users:
        print("\n❌ Username not found! Please enter a valid username.\n")
        continue  # يطلب اسم المستخدم مرة ثانية

    current_user = users[user]

    while True:
        print("1️⃣ - 💰 Deposit \n2️⃣ - 💸 Withdraw \n3️⃣ - 🔄 Transfer \n4️⃣ - 📊 Bank statement \n5️⃣ - 🚪 Exit")
        try:
            banking = int(input("Enter a Banking operation: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1-5.\n")
            continue

        if banking == 1:
            try:
                add = float(input("💰 Enter a Deposit amount: "))
                current_user.deposit(add)
            except ValueError:
                print("❌ Invalid amount! Please enter a valid number.\n")

        elif banking == 2:
            try:
                take = float(input("💸 Enter a Withdraw amount: "))
                current_user.withdraw(take)
            except ValueError:
                print("❌ Invalid amount! Please enter a valid number.")

        elif banking == 3:
            username = input("👤 Enter recipient username: ").strip().lower()
            if username in users:
                try:
                    transfers = float(input("🔄 Enter a transfer amount: "))
                    current_user.transfer(transfers, users[username])
                except ValueError:
                    print("❌ Invalid amount! Please enter a valid number.")
            else:
                print("❌ Recipient not found!")

        elif banking == 4:
            current_user.display()

        elif banking == 5:
            print("🚪 Thank you for using our Banking System. Goodbye!")
            exit()

        else:
            print("❌ Invalid choice! Please select a valid operation.")
