from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidFeedbackId,FeedbackIdDoesNotExists,InvalidRating,InvalidReview

class UpdateFeedbackInteractor:

    def __init__(self,storage=StorageInterface):
        self.storage=storage

    def update_feedback(self,feedback_id:int,rating:float,review:str,presenter:PresenterInterface):
  
        self.validate_input_data(feedback_id=feedback_id,rating=rating,review=review,presenter=presenter)
    
        try:
            self.storage.validate_feedback_id_exists(feedback_id=feedback_id)
        except FeedbackIdDoesNotExists:
            presenter.raise_exception_for_feedback_id_does_not_exists()

        feedback=self.storage.update_feedback(feedback_id=feedback_id,rating=rating,review=review)
        return presenter.get_response_for_update_feedback(feedback)
        

    def validate_input_data(self,feedback_id:int,rating:float,review:str,presenter:PresenterInterface):
        try:
            self.storage.validate_feedback_id(feedback_id=feedback_id)
        except InvalidFeedbackId:
            presenter.raise_exception_for_invalid_feedback_id()

        try:
            self.storage.validate_rating(rating=rating)
        except InvalidRating:
            presenter.raise_exception_for_invalid_rating()

        try:
            self.storage.validate_review(review=review)
        except InvalidReview:
            presenter.raise_exception_for_invalid_review()

        return None