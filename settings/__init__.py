# -*- coding: utf-8 -*-

from .common import *  # noqa

try:
    from .dev import *  # noqa
except ImportError:
    pass

try:
    from .prod import *  # noqa
except ImportError:
    pass
