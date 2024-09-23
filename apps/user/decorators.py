from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def group_required(group_name):
    """
    Decorator for views that checks whether a user has a particular group,
    redirects to the login page if necessary.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if not request.user.groups.filter(name=group_name).exists():
                return HttpResponseForbidden('You do not have permission to view this page.')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def student_required(view_func):
    return group_required('Student')(view_func)

def librarian_required(view_func):
    return group_required('Librarian')(view_func)
