from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.user_login_interactor import UserLoginInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from ib_users.interfaces.service_interface import ServiceInterface
from django.http import HttpResponse
import json


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
   email=kwargs['request_data']['email']
   storage=StorageImplementation()
   presenter=PresenterImplementation()
   interactor=UserLoginInteractor(storage=storage)
   auth_token=interactor.user_login(email=email,presenter=presenter)
   response_data=json.dumps(auth_token)
   return HttpResponse(response_data,status=201)

