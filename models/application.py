from pydantic import BaseModel, Field


class Application(BaseModel):
    """
    Represents an application entity.
    """

    appId: int = Field(None, description='The application ID.')
    """
    The application ID.
    """

    appName: str = Field(None, description='The name of the application.')
    """
    The name of the application.
    """

    appSuiteId: int = Field(None, description='The ID of the associated app suite.')
    """
    The ID of the associated app suite.
    """

    repository: str = Field(None, description='The URL of the repository for the application.')
    """
    The URL of the repository for the application.
    """


class AppSuite(BaseModel):
    """
    Represents an application suite.
    """

    appSuiteId: int = Field(None, description='The ID of the application suite.')
    """
    The ID of the application suite.
    """

    appSuiteName: str = Field(..., description='The name of the application suite.')
    """
    The name of the application suite.
    """