# Create a Configuration class with class variables:

    # app_name = "My Application"
    # version = "1.0"
    # debug_mode = False

# Requirements:

    # Create a class method update_version(new_version).
    # Create a class method enable_debug().
    # Create a class method display_config().
    # Update the version and enable debug mode.
    # Display the final configuration.

#----------------------------------------------------------------------------------------------------


class Configuration:
    app_name = "My Application"

    version = "1.0"

    debug_mode = False

    @classmethod
    def update_version(cls,new_vwesion):
        cls.version = new_vwesion

    @classmethod
    def enable_debug(cls,new_mode):
        cls.debug_mode = new_mode

    @classmethod
    def diplay_config(self):
        print(f'App Name = {self.app_name}')
        print(f'Version = {self.version}')
        print(f'Debug Mode = {self.debug_mode}')


Configuration.update_version('2.0')
Configuration.enable_debug(True)
Configuration.diplay_config()