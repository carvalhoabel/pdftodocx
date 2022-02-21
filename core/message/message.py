class Message:
    """Message model class to inform user what happen.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """New Message Model Class.
        """
        self._message = self._title = ''
        self._warning = self._error = self._info = False

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, message: str):
        self._message = message

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def warning(self) -> bool:
        return self._warning

    @warning.setter
    def warning(self, warning: bool):
        self._warning = warning

    @property
    def error(self) -> bool:
        return self._error

    @error.setter
    def error(self, error: bool):
        self._error = error

    @property
    def info(self) -> bool:
        return self._info

    @info.setter
    def info(self, info: bool):
        self._info = info

    def cleardata(self):
        """This method clean and reset data.
        """
        self.message = self.title = ''
        self.warning = self.error = self.info = False
