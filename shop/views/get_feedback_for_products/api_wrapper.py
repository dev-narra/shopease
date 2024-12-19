from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.get_feedbacks_interactor import GetFeedbacksInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
import json
from django.http import HttpResponse

"""
-inputs: limit and offset
-validate the inputs:
   -validate limit
     - if limit value < 1
        raise error
   -validate offset
     - if offset value is none
       raise error

"""

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    limit=kwargs['query_params']['limit']
    offset=kwargs['query_params']['offset']

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=GetFeedbacksInteractor(storage=storage)
    feedbacks_array=interactor.get_feedbacks(limit=limit,offset=offset,presenter=presenter)
    response_data=json.dumps(feedbacks_array)
    return HttpResponse(response_data,status=200)

    