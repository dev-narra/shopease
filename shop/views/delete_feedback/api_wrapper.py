from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.delete_feedback_interactor import DeleteFeedbackInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Feedback
from django.http import HttpResponse
import json

"""
-inputs: feedback_id
-validate the input 
   -> validate the feedback id
       if feedbackid is exist
          do deletion
       else 
          raise error 

"""


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    feedback_id=kwargs['path_params']['feedbackId']
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=DeleteFeedbackInteractor(storage=storage)
    feedback=interactor.delete_feedback(feedback_id=feedback_id,presenter=presenter)
    response_data=json.dumps(feedback)
    return HttpResponse(response_data,status=200)

