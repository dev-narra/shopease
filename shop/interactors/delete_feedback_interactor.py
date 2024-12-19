from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import FeedbackIdDoesNotExists

class DeleteFeedbackInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def delete_feedback(self,feedback_id:int,presenter:PresenterInterface):

        try:
            self.storage.validate_feedback_id_exists(feedback_id=feedback_id)
        except FeedbackIdDoesNotExists:
            presenter.raise_exception_for_feedback_id_does_not_exists()

        self.storage.delete_feedback(feedback_id=feedback_id)
        return presenter.get_response_for_delete_feedback()