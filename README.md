# Object Oriented Programming (OOP) Part 2 - Cash Register Lab

Now that we’ve discussed more about object oriented design philosophies and techniques like decorators we will be looking at building more complex objects. In this case we will be building a cash register object to simulate different functions of a cash register for an e-commerce site.

## What this does

`lib/cash_register.py` defines a `CashRegister` class that models a real
checkout register:

- **`CashRegister(discount=0)`** — creates a register. `discount` is an
  optional integer percentage (0–100). An invalid discount (not an int, or
  outside 0–100) prints `Not valid discount` and the register falls back to
  no discount.
- **`add_item(item, price, quantity=1)`** — adds `quantity` units of `item`
  at `price` each, updates `total`, appends the item(s) to `items`, and logs
  the line in `previous_transactions`.
- **`apply_discount()`** — applies the register's percentage discount to
  `total` and prints the new total, or prints `There is no discount to
  apply.` when the register has no discount set.
- **`void_last_transaction()`** — reverses the most recent `add_item` call:
  subtracts its price from `total` and removes its item(s) from `items`, or
  prints `There is no transaction to void.` when there's nothing to undo.

### Example

\`\`\`python
from cash_register import CashRegister

register = CashRegister(20)                 # 20% discount
register.add_item("Notebook", 5, 2)          # total: 10
register.add_item("Pen", 1.50, 3)            # total: 14.5
register.apply_discount()                    # total: 11.6
register.void_last_transaction()             # undoes the pens, total: 10.0
\`\`\`

### Running the tests

\`\`\`bash
pipenv install
pipenv run pytest
\`\`\`

<!-- Add a screenshot of your passing test run here, e.g.: -->
<!-- ![Passing tests](docs/tests-passing.png) -->

## Tools & Resources
* [GitHub Repo](https://github.com/learn-co-curriculum/oop-p2-cash-register-lab)
* [Python Classes](https://docs.python.org/3/tutorial/classes.html)

## Instructions

### Set Up
...
