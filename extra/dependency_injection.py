from injector import Injector, inject, Module, singleton, provider

# Define an interface for a message service
class MessageService:
    def send(self, message: str) -> None:
        pass

# Implement the message service interface
class EmailService(MessageService):
    def send(self, message: str) -> None:
        print(f"Email sent: {message}")

# Define a module to configure dependency bindings
class AppModule(Module):
    def configure(self, binder):
        binder.bind(MessageService, to=EmailService, scope=singleton)

    # @provider
    # @singleton
    # def provide_email_service(self) -> MessageService:
    #     return EmailService()

# A class that depends on the MessageService
class MessageSender:
    @inject
    def __init__(self, message_service: MessageService):
        self.message_service = message_service

    def send_message(self, message: str) -> None:
        self.message_service.send(message)

# Set up the Injector and create a MessageSender instance
injector = Injector(AppModule())
print(injector.get(MessageSender).message_service is injector.get(MessageSender).message_service)
message_sender = injector.get(MessageSender)

# Use the MessageSender
message_sender.send_message("Hello, World!")
