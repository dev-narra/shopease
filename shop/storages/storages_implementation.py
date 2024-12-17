from shop.interactors.storage_interfaces.storage_interface import StorageInterface,AuthTokenDto
from ib_users.interfaces.service_interface import ServiceInterface
from shop.models import User


class StorageImplementation(StorageInterface):
       
       def user_login(self,email:str)->AuthTokenDto:
          user = User.objects.get(email=email).id
          service_interface = ServiceInterface()
          auth_tokens = service_interface.create_auth_tokens_for_user(user)
          return auth_tokens
