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
    
    @abstractmethod
    def get_response_for_search_products(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_customer_email(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_customer_phone(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_customer_address(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_customer_name(self):
        pass

    @abstractmethod
    def raise_exception_for_customer_alredy_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_customer_input_data(self):
        pass