from abc import abstractmethod
from dataclasses import dataclass

@dataclass
class AuthTokenDto:
    access_token:str
    expires_in:float

class StorageInterface:

    @abstractmethod
    def user_login(self,email:str)->AuthTokenDto:
        pass
   
    