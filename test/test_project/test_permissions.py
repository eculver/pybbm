"""
Custom permission backend for pybbm that demonstrates circular import.
"""

from pybb import permissions


class CustomPermissionHandler(permissions.DefaultPermissionHandler):
    """
    The custom permission handler to take care of the aforementioned issues
    with querysets containing duplicates.
    """
    def filter_topics(self, user, qs):
        """ return a queryset with topics `user` is allowed to see """
        qs = super(CustomPermissionHandler, self).filter_topics(user, qs)
        return qs.distinct()

    def filter_posts(self, user, qs):
        """ return a queryset with posts `user` is allowed to see """
        qs = super(CustomPermissionHandler, self).filter_posts(user, qs)
        return qs.distinct()
