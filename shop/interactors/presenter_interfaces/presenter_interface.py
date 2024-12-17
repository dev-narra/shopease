from abc import abstractmethod

class PresenterInterface:

    @abstractmethod
    def get_response_for_user_login(self):
        pass