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
            IdQueryParameter(name='following_id', required=True,
                             description="User id to check.")
        ]
    )
    def get(self, request):
        following_id = request.query_params.get('following_id')
        follower = request.user

        try:
            follow = Follow.objects.get(
                follower=follower, following__pk=following_id)
        except:
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

        try:
            follow_user = User.objects.get(pk=follow_user_id)
        except:
            raise exceptions.NotFound(detail="User not found.")

        follower = request.user
        follow, _ = Follow.objects.get_or_create(
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

        try:
            follow = Follow.objects.get(
                follower=follower, following__pk=follow_user_id)
        except:
            raise exceptions.NotFound()

        follow.delete()
        return response.Response(self.serializer_class(follow).data)
