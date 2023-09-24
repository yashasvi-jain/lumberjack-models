from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Log(BaseModel):
    """
    A Lumberjack log.
    """

    logLevel: int = Field(...,
                          description='The numerical representation of the log level.')
    """
    The numerical representation of the log level.
    """

    logLevelName: str = Field(..., description='The name of the log level.')
    """
    The name of the log level.
    """

    logMessage: str = Field(..., description='The message of the log entry.')
    """
    The message of the log entry.
    """

    loggerName: str = Field(..., description='The name of the logger.')
    """
    The name of the logger.
    """

    language: Optional[str] = Field(
        None, description='The name of the language.')
    """
    The name of the language.
    """

    languageVersion: Optional[str] = Field(
        None, description='The version of the language.')
    """
    The version of the language.
    """

    applicationName: Optional[str] = Field(
        None, description='The name of the application.')
    """
    The name of the application associated with the log entry.
    """

    applicationId: Optional[str] = Field(
        None, description='The ID of the application.')
    """
    The ID of the application associated with the log entry.
    """

    applicationSuite: Optional[str] = Field(
        None, description='The name of the application suite.')
    """
    The name of the application suite associated with the log entry.
    """

    applicationSuiteId: Optional[str] = Field(
        None, description='The ID of the application suite.')
    """
    The ID of the application suite associated with the log entry.
    """

    environment: Optional[str] = Field(
        None, description='The name of the environment.')
    """
    The name of the environment in which the log entry was generated.
    """

    username: str = Field(...,
                          description='The username of the user who emitted the log.')
    """
    The username of the user who emitted the log entry.
    """

    machineName: str = Field(...,
                             description='The machine name where the log was emitted.')
    """
    The name of the machine where the log entry was emitted.
    """

    timestamp: datetime = Field(...,
                                description='The timestamp when the log was emitted.')
    """
    The timestamp when the log entry was emitted.
    """

    stackTrace: Optional[str] = Field(
        None, description='The stack trace of the log.')
    """
    The stack trace associated with the log entry, if available.
    """

    filename: Optional[str] = Field(
        None, description='The filename where the logger was invoked.')
    """
    The filename where the logger was invoked.
    """

    filepath: Optional[str] = Field(
        None, description='The absolute file path for the file the logger was invoked.')
    """
    The absolute file path for the file the logger was invoked.
    """

    lineno: Optional[int] = Field(
        None, description='The line number in the file where the logger was invoked.')
    """
    The line number in the file where the logger was invoked.
    """

    code: Optional[str] = Field(
        None, description='The source code where the logger was invoked.')
    """
    The source code where the logger was invoked.
    """
