from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidEmail

class UserLoginInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def user_login(self,email:str,presenter=PresenterInterface):

        try:
            self.storage.validate_email(email=email)
        except InvalidEmail:
            presenter.raise_exception_for_invalid_email()
            return 

        auth_tokens=self.storage.user_login(email=email)
        return presenter.get_response_for_user_login(auth_tokens)