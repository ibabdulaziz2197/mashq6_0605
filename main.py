# 5
class Book:
    def __init__(self, title, author, pages, code):
        self.title = title
        self.author = author
        self._pages = pages
        self.__code = code

    def read(self, pages):
        print(f"Reading {pages} pages")

    def bookmark(self, page):
        print(f"Bookmark at {page}")

    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self._pages}")

book1 = Book("Python Basics", "Ali Valiyev", 200, "B001")

book1.read(10)
book1.bookmark(50)
book1.info()

# 6
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = password

    def login(self, pw):
        return pw == self.__password

    def change_password(self, old, new):
        if old == self.__password:
            self.__password = new
            print("Password changed")
        else:
            print(False)

    def info(self):
        print(f"Username: {self.username}, Email: {self._email}")

user1 = User("coder01", "coder@mail.com", "1234")

print(user1.login("1234"))
user1.change_password("1234", "abcd")
print(user1.login("1234"))

# 7
class Laptop:
    def __init__(self, brand, ram, storage, serial):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.serial = serial

    def upgrade_ram(self, x):
        self.ram += x

    def upgrade_storage(self, x):
        self.storage += x

    def info(self):
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print(f"Serial: {self.serial}")


# Misol uchun
laptop = Laptop("HP", 8, 256, "ABC123")

laptop.upgrade_ram(8)
laptop.upgrade_storage(256)

laptop.info()

# 8
class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self._subject = subject
        self.__salary = salary

    def teach(self, hours):
        print(f"Teaching {hours} hours")

    def increase_salary(self, x):
        self.__salary += x

    def info(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self._subject}")
        print(f"Salary:{self.__salary}")



t = Teacher("Ali", "Math", 1000)

t.teach(2)
t.increase_salary(200)
t.info()

# 9
class GameCharacter:
    def __init__(self, name, health, level, power):
        self.name = name
        self._health = health
        self._level = level
        self.__power = power

    def attack(self):

        self._health -= 20
        if self._health < 0:
            self._health = 0
        print(f"Health:{self._health}")

    def heal(self, x):
        self._health += x
        if self._health > 100:
            self._health = 100
        print(f"Health:{self._health}")

    def level_up(self):
        self._level += 1
        print(f"Level:{self._level}")


# Misol
g = GameCharacter("Hero", 100, 1, 50)

g.attack()
g.heal(20)
g.level_up()

# 10
class Movie:
    def __init__(self, title, duration, rating):
        self.title = title
        self._duration = duration
        self.__rating = rating

    def play(self):
        print(f"Playing {self.title}")

    def rate(self, x):
        self.__rating = x

    def info(self):
        print(f"Title: {self.title}")
        print(f"Duration: {self._duration}")
        print(f"Rating:{self.__rating}")



m = Movie("Avengers", 120, 8)

m.play()
m.rate(9)
m.info()
