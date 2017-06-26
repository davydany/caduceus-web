from rest_framework.serializers import ModelSerializer

from monitor_admin.models import Request

class RequestSerializer(ModelSerializer):

    class Meta:

        model = Request
        fields = ('project', 'uuid', 'request_stats')

    