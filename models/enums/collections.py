from enum import Enum


class Collections(Enum):
    """Enumerates the names of the database collections."""

    APPLICATIONS = 'Applications'
    """Collection for storing application data."""

    APPLICATION_SUITES = 'ApplicationSuites'
    """Collection for storing application suite data."""

    COUNTERS = 'Counters'
    """Collection for storing counters data."""

    LOGS = 'Logs'
    """Collection for storing log data."""