from django.core.exceptions import PermissionDenied

class UserIsAuthorMixin:
    def dispatch(self, request, *args, **kwargs):
        song = self.get_object()
        if not request.user.is_superuser and song.user_author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
