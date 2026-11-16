#Hotel Management

"class for person"
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


"guest inheriting person"
class Guest(Person):
    def __init__(self, name: str, age: int, room_number: int, nights: int):
        super().__init__(name, age)
        self.room_number = room_number
        self.nights = nights

    def calculate_bill(self, rate_per_night: float) -> float:
        "calculating night per night price"
        return self.nights * rate_per_night

    def get_details(self):
        print(
            f"Guest -> Name: {self.name}, Age: {self.age}, "
            f"Room: {self.room_number}, Nights: {self.nights}"
        )

"staff inheriting person"
class Staff(Person):
    def __init__(self, name: str, age: int, position: str, salary: float):
        super().__init__(name, age)
        self.position = position
        self.salary = salary
#giving raise to the staff
    def give_raise(self, amount: float):
        self.salary += amount
#presenting staff details
    def get_details(self):
        print(
            f"Staff -> Name: {self.name}, Age: {self.age}, "
            f"Position: {self.position}, Salary: {self.salary:.2f}"
        )

"hotel class"
class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.guests = []
        self.staff = []
#adding a new guest
    def check_in(self, guest: Guest):
        self.guests.append(guest)
        print(f"{guest.name} checked in to room {guest.room_number}.")
#removing guest
    def check_out(self, guest: Guest):
        if guest in self.guests:
            self.guests.remove(guest)
            print(f"{guest.name} checked out.")
        else:
            print(f"{guest.name} is not a guest of {self.name}.")
#adding staff
    def hire_staff(self, member: Staff):
        self.staff.append(member)
        print(f"{member.name} hired as {member.position}.")

    def list_guests(self):
        print(f"\nGuests at {self.name}:")
        if not self.guests:
            print("  (no guests)")
        for guest in self.guests:
            guest.get_details()

    def list_staff(self):
        print(f"\nStaff at {self.name}:")
        if not self.staff:
            print("  (no staff)")
        for member in self.staff:
            member.get_details()


#Creating guests

guest1 = Guest("Maria Papadopoulou", 34, room_number=1, nights=3)
guest2 = Guest("Armando Gonzalez", 24, room_number=2, nights=5)

#manually adding a new guest
name = input("New guest name:")
age = int(input("Age:"))
room = int(input("Room:"))
nights = int(input("nights:"))
guest3 = Guest(name,age,room,nights)

#creating staff
receptionist = Staff("Fedogiorgos Komninos", 29, "Receptionist", 1300.00)
housekeeper1 = Staff("Eleni Vlachaki", 41, "Housekeeping", 1100.00)
housekeeper2 = Staff("Kostantinos Katakoyzinos", 50, "Housekeeping", 1100.00)


#adding everyone into the hotel
hotel = Hotel("Apartments Syros")
hotel.check_in(guest1)
hotel.check_in(guest2)
hotel.check_in(guest3)
hotel.hire_staff(receptionist)
hotel.hire_staff(housekeeper1)
hotel.hire_staff(housekeeper2)

#listing everyone in the hotel
hotel.list_guests()
hotel.list_staff()

#adding price per night and raise for the staff
rate = 80.00
bill1 = guest1.calculate_bill(rate)
print(f"\n{guest1.name}'s bill: {guest1.nights} nights x {rate:.2f} = {bill1:.2f}")
hotel.check_out(guest1)

bill2 = guest2.calculate_bill(rate)
print(f"\n{guest2.name}'s bill: {guest2.nights} nights x {rate:.2f} = {bill2:.2f}")
hotel.check_out(guest2)

bill3 = guest3.calculate_bill(rate)
print(f"\n{guest3.name}'s bill: {guest3.nights} nights x {rate:.2f} = {bill3:.2f}")
hotel.check_out(guest3)

receptionist.give_raise(150.00)
print(f"{receptionist.name} received a raise of 150.00.")

housekeeper1.give_raise(80)
print(f"{housekeeper1.name} got a raise of 80")

housekeeper2.give_raise(10)
print(f"{housekeeper2.name} got a raise of 10")

#list of everyone in the hotel again
hotel.list_guests()
hotel.list_staff()
