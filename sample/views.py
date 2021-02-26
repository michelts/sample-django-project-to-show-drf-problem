from rest_framework import decorators, response, status, serializers
from django.contrib.auth.models import User


class SampleSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(is_active=True)
    )


@decorators.api_view(["POST"])
def sample_view(request):
    serializer = SampleSerializer(data=request.data)
    data = serializer.is_valid(raise_exception=True)
    raise Exception

    return response.Response(data, status=status.HTTP_200_OK)
