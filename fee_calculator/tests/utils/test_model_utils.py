import pytest
from django.contrib.auth.models import Permission, Group

from fee_calculator.utils.custom_exceptions import ModelNotFoundException
from fee_calculator.utils.model_utils import get_object_or_400, get_object_or_none


class TestModelUtils:
    @pytest.mark.django_db
    def test_get_object_or_400_should_return_object(self):
        group = Group.objects.create(name="_groupowner")
        saved_perm = get_object_or_400(Group, id=group.id)
        assert saved_perm

    @pytest.mark.django_db
    def test_get_object_or_400_should_raise_exception(self):
        with pytest.raises(ModelNotFoundException) as exception_info:
            get_object_or_400(Permission, id=0)
        assert "Permission with id = 0 was not found" in str(exception_info.value)

    @pytest.mark.django_db
    def test_get_object_or_400_with_error_message(self):
        with pytest.raises(ModelNotFoundException) as exception_info:
            get_object_or_400(Permission, error_message="Not found", id=0)
        assert "Not found" in str(exception_info.value)

    @pytest.mark.django_db
    def test_get_object_or_none(self):
        permission = get_object_or_none(Permission, id=0)
        assert not permission
