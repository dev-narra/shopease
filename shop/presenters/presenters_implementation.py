from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.interactors.storage_interfaces.storage_interface import AuthTokenDto

class PresenterImplementation(PresenterInterface):

    def get_response_for_user_login(self,auth_tokens:AuthTokenDto):
        return{
            "access_token":auth_tokens.access_token,
            "expires_in":auth_tokens.expires_in
        }
