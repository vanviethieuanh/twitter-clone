from rest_framework import views
from rest_framework import response
from rest_framework import permissions
from rest_framework import exceptions

from authentication.models import User

from twitter.models import Follow
from twitter.serializers import FollowingSerializer

from common.helpers.doc import IdQueryParameter
from drf_yasg.utils import swagger_auto_schema


class FollowView(views.APIView):
    """
    Follow or Unfollow a user
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FollowingSerializer
    queryset = Follow.objects.all()

    @swagger_auto_schema(
        operation_summary="Check if user is follow another user or not.",
        manual_parameters=[
            IdQueryParameter(required=True, description="User id to check.")
        ]
    )
    def get(self, request):
        follow_user_id = request.query_params.get('id')
        follower = request.user

        follow = Follow.objects.filter(
            follower=follower, following=follow_user_id).first()
        if not follow:
            raise exceptions.NotFound()

        return response.Response(self.serializer_class(follow).data)

    @swagger_auto_schema(
        operation_summary="Follow another user",
        manual_parameters=[
            IdQueryParameter(required=True, description="User id to follow.")
        ]
    )
    def post(self, request):
        follow_user_id = request.query_params.get('id')

        follow_user = User.objects.filter(id=follow_user_id).first()
        follower = request.user

        if not follow_user:
            raise exceptions.NotFound()

        follow = Follow.objects.create(
            follower=follower,
            following=follow_user
        )

        return response.Response(self.serializer_class(follow).data)

    @swagger_auto_schema(
        operation_summary="Unfollow an user.",
        manual_parameters=[
            IdQueryParameter(required=True, description="User id to unfollow.")
        ]
    )
    def delete(self, request):
        follow_user_id = request.query_params.get('id')
        follower = request.user

        follow = Follow.objects.filter(
            follower=follower, following=follow_user_id).first()
        if not follow:
            raise exceptions.NotFound()

        follow.delete()
        return response.Response(self.serializer_class(follow).data)
