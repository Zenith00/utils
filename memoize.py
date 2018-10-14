from datetime import time
from functools import wraps

class _timed_memoize(object):

    """Decorator that caches the value of function.
    Does not care about arguments to the function, will still only cache
    one value.
    """

    def __init__(self, timeout):
        """Initialize with timeout in seconds."""
        self.timeout = timeout
        self.last = None
        self.cache = None

    def __call__(self, fn):
        """Create the wrapped function."""
        @wraps(fn)
        def inner(*args, **kwargs):
            if self.last is None or time() - self.last > self.timeout:
                self.cache = fn(*args, **kwargs)
                self.last = time()
            return self.cache
        return inner