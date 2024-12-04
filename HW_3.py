class BankAccount:
    class __Balance:
        def __init__(self, initial_balance=0):
            self._balance = initial_balance
        
        def deposit(self, amount):
            if amount < 0:
                print("Ошибка: сумма пополнения не может быть отрицательной.")
            else:
                self._balance += amount
        
        def withdraw(self, amount):
            if amount < 0:
                print("Ошибка: сумма снятия не может быть отрицательной.")
            elif amount > self._balance:
                print("Ошибка: недостаточно средств на счете.")
            else:
                self._balance -= amount
        
        def get_balance(self):
            return self._balance

    def __init__(self, initial_balance=0):
        self.__balance = self.__Balance(initial_balance)

    def deposit(self, amount):
        self.__balance.deposit(amount)

    def withdraw(self, amount):
        self.__balance.withdraw(amount)

    def get_balance(self):
        return self.__balance.get_balance()

    @property
    def balance(self):
        return self.get_balance()

    @balance.setter
    def balance(self, value):
        print("Ошибка: нельзя изменить баланс напрямую.")

account = BankAccount(1000)  # Начальный баланс 1000
print(account.get_balance())  # 1000

account.deposit(500)  # Пополнение на 500
account.withdraw(200)  # Снятие 200
account.withdraw(1500)  # Попытка снять больше, чем есть на счете

print(account.get_balance())  # Текущий баланс
account.balance = 5000  # Попытка изменить баланс напрямую (ошибка)
