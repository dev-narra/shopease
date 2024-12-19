from abc import abstractmethod

class PresenterInterface:
    @abstractmethod
    def raise_exception_for_invalid_email(self):
        pass

    @abstractmethod
    def get_response_for_user_login(self):
        pass
    
    @abstractmethod
    def get_response_for_create_product(self):
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
    def raise_exception_for_invalid_description(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_price(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_product_name(self):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_product_name_exists(self):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_exp_date(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_mfg_date(self):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_category(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_stock_quantity(self):
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

    @abstractmethod
    def get_response_for_update_customer(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_customer_id(self):
        pass
        
    
    @abstractmethod
    def get_response_for_get_customers(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_limit_value(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_offset_value(self):
        pass

    @abstractmethod
    def get_response_for_search_customers(self):
        pass
    
    @abstractmethod
    def get_response_for_delete_product(self):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_product_id(self):
        pass
    
    @abstractmethod
    def get_response_for_create_payment(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_payment_amount(self):
        pass 

    @abstractmethod
    def raise_exception_for_invalid_payment_method(self):
        pass 

    @abstractmethod
    def raise_exception_for_invalid_payment_transaction_date(self):
        pass 

    @abstractmethod
    def get_response_for_get_payments(self):
        pass

    @abstractmethod
    def get_response_for_update_payment(self):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_payment_id(self):
        pass

    @abstractmethod
    def get_response_for_update_product(self):
        pass