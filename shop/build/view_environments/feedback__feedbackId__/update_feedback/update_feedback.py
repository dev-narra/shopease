from dsu.runtime.security.request_response import request_response
from dsu.dsu_gen.openapi.constants.config import PARSER_MAPPING
from dsu.dsu_gen.openapi.constants.config import RENDERER_MAPPING
from shop.build.view_environments.feedback__feedbackId__.update_feedback.UpdateFeedbackRequestPathParamSerializer import UpdateFeedbackRequestPathParamSerializer
from shop.build.serializers.definitions.UpdateFeedbackRequest.UpdateFeedbackRequestSerializer import UpdateFeedbackRequestSerializer
from shop.build.serializers.definitions.Feedback.FeedbackSerializer import FeedbackSerializer
from shop.build.view_environments.feedback__feedbackId__.update_feedback.responses.Status_400.Status_400.Status_400Serializer import Status_400Serializer
from shop.build.view_environments.feedback__feedbackId__.update_feedback.responses.Status_404.Status_404.Status_404Serializer import Status_404Serializer


options = {
    'METHOD': 'PUT',
    'REQUEST_WRAPPING_REQUIRED': False,
    'REQUEST_ENCRYPTION_REQUIRED': False,
    'REQUEST_IS_PARTIAL': False,
    'PARSER_CLASSES': [
        PARSER_MAPPING["application/json"]
    ],
    'RENDERER_CLASSES': [
        RENDERER_MAPPING["application/json"]
    ],
    'REQUEST_QUERY_PARAMS_SERIALIZER': None,
    'REQUEST_HEADERS_SERIALIZER': None,
    'REQUEST_PATH_PARAMS_SERIALIZER': UpdateFeedbackRequestPathParamSerializer,
    'DEFAULT_REQUEST_PATH_PARAMS': {"feedbackId": 635},
    'REQUEST_SERIALIZER': UpdateFeedbackRequestSerializer,
    'REQUEST_SERIALIZER_MANY_ITEMS': False,
    'RESPONSE': {
        
        '200': {
           'RESPONSE_SERIALIZER': FeedbackSerializer,
           'RESPONSE_SERIALIZER_MANY_ITEMS':  False,
           'HEADERS_SERIALIZER': None,
        }
        ,
        
        '400': {
           'RESPONSE_SERIALIZER': Status_400Serializer,
           'RESPONSE_SERIALIZER_MANY_ITEMS':  False,
           'HEADERS_SERIALIZER': None,
        }
        ,
        
        '404': {
           'RESPONSE_SERIALIZER': Status_404Serializer,
           'RESPONSE_SERIALIZER_MANY_ITEMS':  False,
           'HEADERS_SERIALIZER': None,
        }
        
    },
    "SECURITY": {

        "oauth" : [
            "update"
            
        ]
    },
    'LOG_CONFIG': {'request_log_selector': 'ENABLE_COMPLETE_LOG', 'response_log_selector': 'ENABLE_COMPLETE_LOG'}
}

app_name = "shop"
operation_id  = "update_feedback"
group_name = ""


@request_response(options=options, app_name=app_name, operation_id=operation_id, group_name=group_name)
def update_feedback(request, *args, **kwargs):
    args = (request,) + args
    from dsu.dsu_gen.openapi.wrappers.view_env_wrapper import view_env_wrapper
    return view_env_wrapper(app_name, "update_feedback", group_name, *args, **kwargs)
