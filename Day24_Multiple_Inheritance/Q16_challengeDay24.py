print('===================================================================')
print('                 Smart Device Management System                    ')
print('===================================================================')


class Camera:
    def take_photo(self):
        print("Photo Captured")

    def record_video(self):
        print("Video Recording Started")


class Phone:
    def make_call(self):
        print("Calling...")

    def send_message(self):
        print("Message Sent")


class MusicPlayer:
    def play_music(self):
        print("Music Playing")

    def stop_music(self):
        print("Music Stopped")


class SmartPhone(Camera, Phone, MusicPlayer):

    def __init__(self, brand, model, price):
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: Rs. {self.price}")

    def use_camera(self):
        print("\n--- Camera Features ---")
        self.take_photo()
        self.record_video()

    def use_phone(self):
        print("\n--- Phone Features ---")
        self.make_call()
        self.send_message()

    def use_music_player(self):
        print("\n--- Music Features ---")
        self.play_music()
        self.stop_music()


# Create Smartphone Objects
mobile1 = SmartPhone("Samsung", "Galaxy S24", 75000)
mobile2 = SmartPhone("Apple", "iPhone 16", 90000)


# Test First Smartphone
mobile1.display_details()
mobile1.use_camera()
mobile1.use_phone()
mobile1.use_music_player()

print("\n--- Inheritance Information ---")
for cls in SmartPhone.mro():
    print(cls.__name__)

print("\n" + "=" * 40 + "\n")

# Test Second Smartphone
mobile2.display_details()
mobile2.use_camera()
mobile2.use_phone()
mobile2.use_music_player()