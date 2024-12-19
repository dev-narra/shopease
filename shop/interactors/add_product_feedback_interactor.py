from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidCustomerId,InvalidProductId,CustomerIdDoesNotExists,ProductIdDoesNotExists,InvalidRating,InvalidReview
class AddProductFeedbackInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def add_product_feedback(self,product_id:int,customer_id:int,rating:str,review:str,presenter:PresenterInterface):

        validate_input=self.validate_input_data(product_id=product_id,customer_id=customer_id,rating=rating,review=review,presenter=presenter)
        if validate_input:
            return validate_input

        try:
            self.storage.validate_product_id_exists(product_id=product_id)
        except ProductIdDoesNotExists:
            presenter.raise_exception_for_product_id_does_not_exists()

        try:
            self.storage.validate_customer_id_exists(customer_id=customer_id)
        except CustomerIdDoesNotExists:
            presenter.raise_exception_for_customer_id_does_not_exists()

        feedback=self.storage.add_product_feedback(product_id=product_id,customer_id=customer_id,rating=rating,review=review)
        return presenter.get_response_for_add_product_feedback(feedback)

        
    def validate_input_data(self,product_id:int,customer_id:int,rating:str,review:str,presenter:PresenterInterface):

        try:
            self.storage.validate_customer_id(id=customer_id)
        except InvalidCustomerId:
            presenter.raise_exception_for_invalid_customer_id()

        try:
            self.storage.validate_product_id(product_id=product_id)
        except InvalidProductId:
            presenter.raise_exception_for_invalid_product_id()

        try:
            self.storage.validate_rating(rating=rating)
        except InvalidRating:
            presenter.raise_exception_for_invalid_rating()

        try:
            self.storage.validate_review(review=review)
        except InvalidReview:
            presenter.raise_exception_for_invalid_review()

        return None

        

        