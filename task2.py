# Создайте класс BankAccount, который имеет:

# Атрибут balance, начальное значение которого равно 0.

# Метод deposit(amount), который увеличивает баланс на
# сумму amount.

# Метод withdraw(amount), который уменьшает баланс на сумму
# amount, если на счете достаточно средств;
# если недостаточно, выведите сообщение "Недостаточно средств".

# Метод get_balance, который возвращает текущий баланс.


class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Недостаточно средств")
            return
        self.__balance -= amount

    def get_balance(self):
        return f"Balance: {self.__balance}"


if __name__ == "__main__":
    bk = BankAccount()
    bk.deposit(1000)
    print(bk.get_balance())
    bk.withdraw(500)
    print(bk.get_balance())
    bk.withdraw(1000)

