from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.update_feedback_interactor import UpdateFeedbackInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
import json
from django.http import HttpResponse

"""
-inputs: feedback_id,request_data
-validate_inputs:
   -validate request_data
   -validate feedback_id
     if feedback id is exists:
        do updation
     else
       raise error
"""



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
   feedback_id=kwargs['path_params']['feedbackId']
   rating=kwargs['request_data']['rating']
   review=kwargs['request_data']['review']
   storage=StorageImplementation()
   presenter=PresenterImplementation()
   interactor=UpdateFeedbackInteractor(storage=storage)
   feedback=interactor.update_feedback(feedback_id=feedback_id,rating=rating,review=review,presenter=presenter)
   response_data=json.dumps(feedback)
   return HttpResponse(response_data,status=200)
   

    