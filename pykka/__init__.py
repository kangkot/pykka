import gevent.monkey
gevent.monkey.patch_all()

#: Pykka's version as a tuple that can be used for comparison
VERSION = (0, 6)

def get_version():
    """Returns Pykka's version as a formatted string"""
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if len(VERSION) > 2:
        version = '%s.%s' % (version, VERSION[2])
    return version

def get_all(futures, timeout=None):
    """
    Collect all values encapsulated in the list of futures.

    If ``timeout`` is not :class:`None`, the method will wait for a reply for
    ``timeout`` seconds, and then raise :exc:`gevent.Timeout`.

    :param futures: futures for the results to collect
    :type futures: list of `gevent.event.AsyncResult`

    :param timeout: seconds to wait before timeout
    :type timeout: float or :class:`None`

    :returns: list of results
    """
    return map(lambda future: future.get(timeout=timeout), futures)

def wait_all(futures, timeout=None):
    """
    Wait for all futures in the results list are available.

    This is an alias for :func:`get_all`, but with a name that is more
    describing if you do not care about the return values.
    """
    return get_all(futures, timeout)
