from abc import abstractmethod

class PresenterInterface:
    @abstractmethod
    def raise_exception_for_invalid_email(self):
        pass

    @abstractmethod
    def get_response_for_user_login(self):
        pass

    @abstractmethod
    def get_response_for_get_products(self):
        pass

    @abstractmethod
    def get_response_for_create_customer(self):
        pass