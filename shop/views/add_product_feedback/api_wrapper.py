from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.add_product_feedback_interactor import AddProductFeedbackInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
import json
from django.http import HttpResponse

"""
-input data:
-validate input data:
   -validate product id
      if product id is none
         raise error
   -validate customer id
      if customer id is none
         raise error
   -validate rating
      if rating id is none
         raise error
   -validate review
    if review id is none
         raise error

"""

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    product_id=kwargs['path_params']['productId']
    customer_id=kwargs['request_data']['customer_id']
    rating=kwargs['request_data']['rating']
    review=kwargs['request_data']['review']

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=AddProductFeedbackInteractor(storage=storage)
    feedback=interactor.add_product_feedback(product_id=product_id,customer_id=customer_id,rating=rating,review=review,presenter=presenter)
    response_data=json.dumps(feedback)
    return HttpResponse(response_data,status=201)
    