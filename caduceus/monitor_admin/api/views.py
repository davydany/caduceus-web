import json

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers import serialize

from monitor_admin.models import Project, Request


class RequestViewSet(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, project_id):

        project_id = self.kwargs.get('project_id')
        project = Project.objects.get(project_id=project_id)
        return Response(
            serialize('json', project.requests.all())
        )

    def post(self, request, project_id):

        project_id = self.kwargs.get('project_id')
        project = Project.objects.get(project_id=project_id)
        data = request.data

        # create the Request object and save it
        request_keys = list(data)
        request_uuid = request_keys[0]
        request_stats = json.dumps(data[request_uuid])

        request = Request(
            project=project, 
            uuid=request_uuid, 
            request_stats=request_stats)
        request.save()

        return Response({ 'message' : 'OK' })