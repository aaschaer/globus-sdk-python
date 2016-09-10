import abc
import six


@six.add_metaclass(abc.ABCMeta)
class GlobusAuthorizer(object):
    """
    A ``GlobusAuthorizer`` is a very simple object which generates valid
    Authorization headers.
    It may also have handling for responses that indicate that it has provided
    an invalid Authorization header.
    """
    @abc.abstractmethod
    def set_authorization_header(header_dict):
        """
        Takes a dict of headers, and adds to it a mapping of
        ``{"Authorization": "..."}`` per this object's type of Authorization.
        Importantly, if an ``Authorization`` header is already set, this method
        is expected to overwrite it.
        """

    def handle_missing_authorization(self, *args, **kwargs):
        """
        This operation should be called if a request is made with an
        Authorization header generated by this object which returns a 401
        (HTTP Unauthorized).
        If the ``GlobusAuthorizer`` thinks that it can take some action to
        remedy this, it should update its state and return ``True``.
        If the Authorizer cannot do anything in the event of a 401, this *may*
        update state, but importantly returns ``False``.

        By default, this always returns ``False`` and takes no other action.
        """
        return False
