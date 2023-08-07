
''''
Abstraction in programming is the process of hiding the complex details of some system while providing a simpler interface.
In object-oriented programming (OOP), this often involves using classes to hide the internal state and implementation details of an
object and exposing a set of methods (functions within a class) that provide an interface to the object's functionality.

Here's an example: let's say we are creating a software for a bank. The "Account" class can be an abstraction of a bank account.
The account has an internal state (like the balance) and methods for interacting with the state (like deposit and withdraw).
'''

class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return self._balance
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            print("Invalid amount or insufficient balance")
```

'''
You don't need to know how deposit or withdrawal works internally, you just need to call the method: that's abstraction.

In some cases, you might want to have more control over how the internal state of an object is accessed or modified.
This is where getter and setter methods come in.
Getters and setters are used in OOP to ensure the principle of data encapsulation.
A getter method allows reading a property's value. A setter method allows modifying a property's value.
They are used to control access to an object's internal state. ' 

Here's how we could add a getter and a setter to the "Account" class for the `_balance` attribute:
'''

class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    # ... (rest of the class as before)
```
'''
Here, we've added a `balance` property that provides getter and setter methods for the `_balance` attribute.

The `@property` decorator turns the `balance()` method into a getter for a property of the same name,
and the `@balance.setter` decorator turns the `balance(amount)` method into a setter for that property.

Now you can access the balance of an account using `account.balance`
(like it's an attribute), and Python will automatically call the getter method. '
'And you can set the balance using `account.balance = amount`, and Python will automatically call the setter method.

When to use getters and setters can depend on a few things:

1. **Use getters and setters when you want to add logic to the process of getting or setting a property,
like validation or transformation.** In the example above, the setter prevents the balance from being set to a negative value.

2. **You might not want to use getters and setters if you're just directly getting or setting a value with no additional logic.'
'** Python isn't as strict about encapsulation as some other languages, and it's often considered more Pythonic to leave '
'attributes public unless there's a good reason to protect them. Directly accessing or setting a value is more concise and
more in line with Python's philosophy of "we're all consenting adults here".

Remember that you can always start with a public attribute and later change it to a property with a getter and setter 
if you need to add additional logic, without changing the interface of your class. 
    This is one of the strengths of Python's property system.
'''
