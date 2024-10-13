import winzy


# An example plugin implementation.

class HelloWorld:
    __name__ = "mail"

    @winzy.hookimpl
    def register_commands(self, subparser):
        parser = subparser.add_parser("mail", description="Access outlook email using cli.")
        # Add subprser arguments here.
        parser.set_defaults(func=self.hello)
    
    def hello(self, args):
        # this routine will be called when "winzy "mail is called."
        print("Hello! This is an example ``winzy`` plugin.")

mail_plugin = HelloWorld()
