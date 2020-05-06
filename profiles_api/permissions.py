from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """allow users to edit own profiles only"""
    def has_object_permission(self,request,view,obj):
        """check if user trying to edit their own profile every time a request is made"""
        if request.method in permissions.SAFE_METHODS:
            #SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True
        
        return (obj.id == request.user.id)

class UpdateOwnStatus(permissions.BasePermission):
    """allow users to edit own profiles only"""
    def has_object_permission(self,request,view,obj):
        """check if user trying to edit their own profile every time a request is made"""
        if request.method in permissions.SAFE_METHODS:
            #SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True
        
        return (obj.user_profile.id == request.user.id)