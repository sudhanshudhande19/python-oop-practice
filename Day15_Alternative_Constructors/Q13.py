# Create a Configuration class with:

    # app_name
    # version
    # debug_mode

# Requirements:

    # Create a class method from_dict(data).
    # Accept application settings through a dictionary.
    # Use default values for optional fields.
    # Validate the data types.
    # Display the final configuration.
#--------------------------------------------------------------------------------------------------------------



class Configuration:
    def __init__(self, app_name, version, debug_mode):
        self.app_name = app_name
        self.version = version
        self.debug_mode = debug_mode

    @classmethod
    def from_dict(cls, data):

      
        app_name = data.get('app_name', 'My App')
        version = data.get('version', 1.0)
        debug_mode = data.get('debug_mode', False)

       
        if not isinstance(app_name, str):
            raise ValueError("App name must be a string")

        if not isinstance(version, (int, float)) or isinstance(version, bool):
            raise ValueError("Version must be a number")

        if not isinstance(debug_mode, bool):
            raise ValueError("Debug mode must be True or False")

        return cls(app_name, version, debug_mode)

    def display(self):
        print("Application Configuration")
        print("-" * 30)
        print(f"App Name   = {self.app_name}")
        print(f"Version    = {self.version}")
        print(f"Debug Mode = {self.debug_mode}")


# Test 1: All values provided
e1 = Configuration.from_dict({
    'app_name': 'Samsung',
    'version': 2.14,
    'debug_mode': True
})

e1.display()

print()

# Test 2: Default values
e2 = Configuration.from_dict({
    'app_name': 'My Website'
})

e2.display()

print()

# Test 3: Invalid input
try:
    e3 = Configuration.from_dict({
        'app_name': 'Google',
        'version': '2.5',
        'debug_mode': 2023
    })
    e3.display()

except ValueError as error:
    print("Error:", error)
