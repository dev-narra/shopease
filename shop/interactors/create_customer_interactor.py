from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface

class CreateCustomerInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def create_customer(self,name:str,email:str,phone:str,address:str,presenter:PresenterInterface):
        customer_id=self.storage.create_customer(name=name,email=email,phone=phone,address=address)
        return presenter.get_response_for_create_customer(customer_id)



