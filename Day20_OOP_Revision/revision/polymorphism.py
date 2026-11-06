"""
Day 20 - OOP Revision
polymorphism.py - Overriding, duck typing and built-in polymorphism
"""


# --- Polymorphism through method overriding ---
class Notification:
    def send(self):
        print("Sending a notification")


class Email(Notification):
    def send(self):
        print("Sending an email")


class SMS(Notification):
    def send(self):
        print("Sending an SMS")


# --- Duck typing: no common parent needed ---
class Duck:
    def speak(self):
        print("Quack")


class Robot:
    def speak(self):
        print("Beep boop")


if __name__ == "__main__":
    print("--- Overriding + one loop ---")
    for item in [Notification(), Email(), SMS()]:
        item.send()                               # same call, different behaviour

    print("\n--- Duck typing ('if it speaks, it works') ---")
    for thing in [Duck(), Robot()]:
        thing.speak()

    print("\n--- Built-in polymorphism ---")
    print("len('hello')   :", len("hello"))
    print("len([1, 2, 3]) :", len([1, 2, 3]))
    print("len({'a': 1})  :", len({"a": 1}))
    print("5 + 3          :", 5 + 3)
    print("'5' + '3'      :", "5" + "3")
    print("[1] + [2]      :", [1] + [2])
