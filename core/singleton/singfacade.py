from core.facade.facade import Facade


class SingFacade:
    """Facade Singleton Parttern.
    """

    _instance = None

    @classmethod
    def facade(cls) -> Facade:
        """New or existing Facade instance.

        Returns:
            Facade: instance of Facade.
        """
        if not cls._instance:
            cls._instance = Facade()
        return cls._instance
