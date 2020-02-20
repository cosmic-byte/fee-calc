from rest_framework import status
from rest_framework.exceptions import APIException


class ModelNotFoundException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Model not found"
    default_code = "bad_request"

