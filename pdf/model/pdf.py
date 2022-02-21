class Pdf:
    """PDF model class.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """New Pdf file.
        """
        self._pathpdf = self._pathdocx = self._name = ''

    @property
    def pathpdf(self) -> str:
        return self._pathpdf

    @pathpdf.setter
    def pathpdf(self, pathpdf: str):
        self._pathpdf = pathpdf

    @property
    def pathdocx(self) -> str:
        return self._pathdocx

    @pathdocx.setter
    def pathdocx(self, pathdocx: str):
        self._pathdocx = pathdocx

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name
