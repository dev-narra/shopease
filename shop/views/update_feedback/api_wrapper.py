from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass

"""
-inputs: feedback_id
-validate_inputs:
   -validate feedback_id
     if feedback id is exists:
        do updation
     else
       raise error
"""



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    

    