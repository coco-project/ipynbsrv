from ipynbsrv.conf import global_vars


def login_allowed(user):
    """
    @user_passes_test decorator to check whether the user is allowed to access the application or not.

    We do not want to allow non-UserBackend users to access the application
    (because we need the LDAP entry for the shares etc.) so we check that here.
    """
    if not user.username:
        return False
    else:
        user_backend = global_vars.USER_BACKEND
        return user_backend.user_exists(user.username)
