"""
Enumerations
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import enum  # python3 enums ported to python2


class ConductorScheme(enum.Enum):
    """
    Schemes for building urls. The value of each scheme is used for
    prioritizing GET/POST/... operations, so the FILE scheme should be the
    first one (meaning that since the local filesystem is cheaper to use,
    it makes sense to try it before the others)
    """

    FILE = 1
    FTP = 2
    SFTP = 3
    HTTP = 4


class ServerSchemeMethod(enum.Enum):
    GET = 1
    POST = 2
    FIND = 3


class ParameterType(enum.Enum):
    NUMBER = 1
    STRING = 2


class TimeslotStrategy(enum.Enum):

    SINGLE = 1
    MULTIPLE = 2


class TaskResourceRole(enum.Enum):

    INPUT = 1
    OUTPUT = 2


class TemporalSelectionRule(enum.Enum):

    LATEST = 1
    EARLIEST = 2


class ParameterSelectionRule(enum.Enum):

    HIGHEST = 1
    LOWEST = 2


class TemporalPart(enum.Enum):
    YEAR = 1
    MONTH = 2
    DAY = 3
    HOUR = 4
    MINUTE = 5
    SECOND = 6
    YEAR_DAY = 7
    DEKADE = 8
