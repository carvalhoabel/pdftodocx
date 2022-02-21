from core.message.message import Message


class SingMessage:
    """Message Singleton Pattern.

    Author:
        abelbcarvalho
    """

    _instance = None

    @classmethod
    def message(cls) -> Message:
        """New or existing Message instance.

        Returns:
            Message: instance of Message.
        """
        if not cls._instance:
            cls._instance = Message()
        return cls._instance
