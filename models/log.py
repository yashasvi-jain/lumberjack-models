from pydantic import BaseModel, Field


class Log(BaseModel):
    """
    Represents a log entry.
    """

    logId: int = Field(None, description="Auto-incrementing log identifier")
    """
    The auto-incrementing identifier of the log entry.
    """

    logLevel: int = Field(..., description="The numerical representation of the log level.")
    """
    The numerical representation of the log level.
    """

    logLevelName: str = Field(..., description="The name of the log level.")
    """
    The name of the log level.
    """

    logMessage: str = Field(..., description="The message of the log entry.")
    """
    The message of the log entry.
    """

    loggerName: str = Field(..., description="The name of the logger.")
    """
    The name of the logger.
    """

    language: str = Field(None, description="The name of the language.")
    """
    The name of the language.
    """

    languageVersion: str = Field(None, description="The version of the language.")
    """
    The version of the language.
    """

    applicationName: str = Field(None, description="The name of the application.")
    """
    The name of the application associated with the log entry.
    """

    applicationId: str = Field(None, description="The ID of the application.")
    """
    The ID of the application associated with the log entry.
    """

    applicationSuite: str = Field(None, description="The name of the application suite.")
    """
    The name of the application suite associated with the log entry.
    """

    applicationSuiteId: str = Field(None, description="The ID of the application suite.")
    """
    The ID of the application suite associated with the log entry.
    """

    environment: str = Field(None, description="The name of the environment.")
    """
    The name of the environment in which the log entry was generated.
    """

    username: str = Field(..., description="The username of the user who emitted the log.")
    """
    The username of the user who emitted the log entry.
    """

    machineName: str = Field(..., description="The machine name where the log was emitted.")
    """
    The name of the machine where the log entry was emitted.
    """

    timestamp: str = Field(..., description="The timestamp when the log was emitted.")
    """
    The timestamp when the log entry was emitted.
    """

    stackTrace: str = Field(None, description="The stack trace of the log.")
    """
    The stack trace associated with the log entry, if available.
    """