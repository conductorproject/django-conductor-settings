import enum


class ServerSchemeMethod(enum.Enum):
    GET = 1
    POST = 2
    FIND = 3


class ConductorScheme(enum.Enum):
    FILE = 1
    FTP = 2
    SFTP = 3
    HTTP = 4


class ParameterType(enum.Enum):
    NUMBER = 1
    STRING = 2


class TemporalRule(enum.Enum):
    LATEST = 1
    EARLIEST = 2


class ParameterRule(enum.Enum):
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
