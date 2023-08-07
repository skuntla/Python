
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



'''
Objects hide their data behind abstractions and expose functions that operate on that data. 
 Data structure expose their data and have no meaningful functions.
 

let's first create an object example. In this case, let's make a `Circle` class, which hides the details of how a 
circle's area and perimeter are calculated:'''


import math

class Circle:
    def __init__(self, radius):
        self._radius = radius  # The underscore implies this is intended to be private.

    def get_area(self):
        return math.pi * (self._radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self._radius
```

'''
Here, the data (`_radius`) is hidden behind an abstraction. The class exposes functions (`get_area`, `get_perimeter`) 
that operate on that data, but you can't access the radius directly. 
This is typical of an object in object-oriented programming.

Now, let's consider a data structure that's essentially just a container for data, with no meaningful functions. 
The simplest example might be a tuple or a dictionary. However, we can also define our own data structure. 
For example, let's create a `CircleData` class:
'''

class CircleData:
    def __init__(self, radius, area, perimeter):
        self.radius = radius
        self.area = area
        self.perimeter = perimeter

'''

In this case, the `CircleData` class exposes its data and has no meaningful functions. All it does is store values. 
You're expected to create and manipulate these values outside of the class.

For instance, you might use it like this:
'''

radius = 3
area = math.pi * (radius ** 2)
perimeter = 2 * math.pi * radius
circle_data = CircleData(radius, area, perimeter)

'''
In this case, the logic for calculating the area and perimeter is not encapsulated in the `CircleData` class. 
Instead, it's up to the code that uses `CircleData` to calculate these values. 
This is more characteristic of a data structure than an object, as it's just passively holding data, not providing functionality.

'''


###########################################

'''
This exposes the fundamental dichotomy between objects and data structures: 

Procedural code (code using data structures) makes it easy to add new functions without
changing the existing data structures. OO code, on the other hand, makes it easy to add
new classes without changing existing functions.

The complement is also true: 
Procedural code makes it hard to add new data structures because all the functions must
change. OO code makes it hard to add new functions because all the classes must change.
So, the things that are hard for OO are easy for procedures, and the things that are
hard for procedures are easy for OO!

In any complex system there are going to be times when we want to add new data
types rather than new functions. For these cases objects and OO are most appropriate. On
the other hand, there will also be times when we’ll want to add new functions as opposed
to data types. In that case procedural code and data structures will be more appropriate.
Mature programmers know that the idea that everything is an object is a myth. 
Sometimes you really do want simple data structures with procedures operating on them
'''

'''
Let's take an example of a system where we're dealing with different shapes, and we want to calculate their areas. 
We'll consider two cases: 
one using procedural code with data structures, 
and one using object-oriented (OO) code.
'''

#**Procedural code with data structures:**

# Let's say we represent each shape as a dictionary, which is a simple data structure.


circle = {"type": "circle", "radius": 5}
rectangle = {"type": "rectangle", "length": 4, "width": 5}

# We could have a function for calculating the area of each type of shape:

import math
def area_of_shape(shape):
    if shape["type"] == "circle":
        return math.pi * (shape["radius"] ** 2)
    elif shape["type"] == "rectangle":
        return shape["length"] * shape["width"]

print(area_of_shape(circle))      # prints 78.53981633974483
print(area_of_shape(rectangle))   # prints 20


'''
If we want to add a new function, say, for calculating the perimeter of a shape, 
we can do that without changing the existing data structures. However, if we want to add a new type of shape (a new data structure), 
we have to modify all our existing functions to handle that new type.
'''


# **Object-oriented (OO) code:**
# Now let's represent each shape as an object, with a class for each type of shape.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(5)
rectangle = Rectangle(4, 5)


#With this setup, we can calculate the area of any shape with the `shape.area()` method:


print(circle.area())    # prints 78.53981633974483
print(rectangle.area()) # prints 20


'''
If we want to add a new type of shape, we can just define a new class for that shape without modifying any existing code. 
However, if we want to add a new function that operates on these shapes, like a function to calculate the perimeter, 
we need to add that function to each class.

As these examples illustrate, the best approach can depend on what changes you expect to make in the future. 
If you expect to add more functions, a procedural style/data structures can be easier to work with. 
If you expect to add more types of data, an object-oriented style can be more convenient. 
Real-world programs often use a mix of these approaches.
'''

'''
The Law of Demeter is also known as the principle of least knowledge. This principle states that an object should only 
interact directly with a few closely related objects. More formally, a method should only call methods on:

1. Itself (`self` in Python)
2. Objects it creates
3. Input parameters
4. Its own attributes (fields)

The law tries to enforce the principle of least privilege, meaning an object should only have access to the information 
and resources necessary for its legitimate purpose. 

'''

#Let's illustrate this with a Python example.
'''
Imagine you have an `Order` object which contains a list of `Product` objects. 
Each `Product` object has a `Price` object which contains the price of the product.

If you want to calculate the total price of an order, you might do something like this:
'''

class Price:
    def __init__(self, amount):
        self.amount = amount


class Product:
    def __init__(self, price):
        self.price = price


class Order:
    def __init__(self, products):
        self.products = products

    def calculate_total(self):
        return sum([product.price.amount for product in self.products])


# Here, the `calculate_total` method in the `Order` class is reaching through the `Product` object
# to access the `amount` attribute of the `Price` object. This is a violation of the Law of Demeter
# because the `Order` is dealing with an object (`Price`) that's a "stranger" to it.

#To comply with the Law of Demeter, we can add a method to the `Product` class that returns the product's price:


class Product:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price.amount


class Order:
    def __init__(self, products):
        self.products = products

    def calculate_total(self):
        return sum([product.get_price() for product in self.products])

# Now, the `calculate_total` method only calls methods on objects that are allowed by the
# Law of Demeter: `self.products` (an attribute of `self`) and `product.get_price()` (a method on an object in `self.products`).
# This helps encapsulate the internal structure of the `Product` and `Price` classes and makes the `Order` class more
# robust to changes in those classes.

Sure, we can simplify the example by storing the price directly in the `Product` class, without needing a separate `Price` class. Here is how you can do it:

```python
class Product:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price

class Order:
    def __init__(self, products):
        self.products = products

    def calculate_total(self):
        return sum([product.get_price() for product in self.products])

# You can create an `Order` object in a similar way:

# Create some Products with their prices
product1 = Product(10.00)  # Price for product1 is $10.00
product2 = Product(15.00)  # Price for product2 is $15.00

# Put the products into a list
products = [product1, product2]

# Create an Order with the list of products
order = Order(products)

# Calculate the total price of the order
total = order.calculate_total()

print(total)  # prints 25.00

'''

In this example, each `Product` object is initialized with a price, and the `get_price` method simply returns this price. 
The `Order` class works in the same way as before, summing up the prices of all the products in the order.

'''


##########################################################
'''
A Data Transfer Object (DTO) is a pattern that is often used in scenarios where you need to communicate between 
different parts of a system (such as between modules, between layers of an application, or between different applications),
 and you want to aggregate different data elements into a single object to make this communication more manageable.

A DTO is essentially a container for data, often represented as a class with public attributes and no methods 
(other than possibly some simple constructors or other basic helper methods). 
Because it doesn't have any behavior (i.e., no complex methods), it's considered a data structure, not a full-fledged object.

For instance, let's say you have a database of users, and you want to fetch user data to display it on a webpage. 
Here's an example of what a DTO might look like in Python:

'''
class UserDTO:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

'''
This `UserDTO` simply holds data for a user and doesn't have any other methods. You can create an instance of `UserDTO` 
with the data for a particular user:

'''
user_dto = UserDTO("Alice", "alice@example.com", 25)

# Then you could pass this DTO around your application. For example, you might have a function that takes a `UserDTO` and
# uses it to fill in a webpage template:

def display_user(user_dto):
    print(f"Username: {user_dto.username}")
    print(f"Email: {user_dto.email}")
    print(f"Age: {user_dto.age}")

display_user(user_dto)

'''
One of the benefits of this approach is that if you ever change the underlying data source 
(e.g., switch from a SQL database to a NoSQL database), you only need to change the part of your 
code that creates the `UserDTO` objects. The rest of your code just works with the DTO and 
doesn't care where the data came from, which makes it more robust to changes.
'''
