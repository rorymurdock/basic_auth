"""Configure Basic Auth"""
import argparse
from basic_auth import Auth

AUTH = Auth()


class Config():
    """Configure Basic Auth"""
    def __init__(self, output="general.json"):
        self.output = output

    def interactive(self):
        """Ask the user for the information and format the config"""
        # Get data from user
        url = AUTH.ask("URL: ")
        username = AUTH.ask("Username: ")
        password = AUTH.ask("Password: ")

        # Encode data into base64
        encoded = AUTH.encode(username, password)

        # Generate data structure
        data = AUTH.basic_config_generate(url, encoded)

        # Return the completed data
        return data

    def arguments(self, args):
        """Using data from the arguments format the config"""
        url = args.url
        username = args.username
        password = args.password

        # Encode data into base64
        encoded = AUTH.encode(username, password)

        # Generate data structure
        data = AUTH.basic_config_generate(url, encoded)

        # Return the completed data
        return data

    def write_data(self, data, filename):
        """Write the config to a file"""
        write = AUTH.write_config(data, filename)

        return write

    def get_args(self):  # pragma: no cover
        """Parse arguments and return the namespace"""
        # This is indirectly tested by the test_main_results() funtion
        parser = argparse.ArgumentParser()
        optional = parser.add_argument_group('Optional arguments')

        optional.add_argument("-url", help="URL")
        optional.add_argument("-username", help="Username")
        optional.add_argument("-password", help="Password")
        args = parser.parse_args()

        return args

    def main(self, args):
        """Main function"""
        if None in (args.url, args.username, args.password):
            print("No arguments found, running in interactive mode")
            data = self.interactive()
        else:
            data = self.arguments(args)

        if self.write_data(data, self.output):
            print("Config sucessfully written")
            return True

        print("Unable to write config")  # pragma: no cover
        return False  # pragma: no cover


# This is indirectly tested by the test_main_results() funtion
if __name__ == "__main__":  # pragma: no cover
    ARGS = Config().get_args()
    Config().main(ARGS)
