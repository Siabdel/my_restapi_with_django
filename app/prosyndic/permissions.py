# blogapi/blog/permissions
from rest_framework import permissions

class BasePermissions(object):
    
    def has_permission(self, request, view):
        """_summary_

        Args:
            request (_type_): _description_
            view (_type_): _description_
        """
        return True
    
    def has_object_permission(self, request, view, obj):
        """_summary_

        Args:
            request (_type_): _description_
            view (_type_): _description_
            obj (_type_): _description_
        """
        
        return True 
    
class IsAuthorOrReadOnly(BasePermissions):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # GET, OPTIONS, HEAD
            return True
        
        return obj.author == request.user
    