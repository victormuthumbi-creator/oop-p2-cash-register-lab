#!/usr/bin/env python3


class CashRegister:
    """Models a simple cash register: add items, apply a discount,
    and void the most recent transaction."""

    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount

        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        line_total = price * quantity
        self.total += line_total

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": line_total,
            "quantity": quantity,
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total -= self.total * self.discount // 100
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"]

        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])