from pdf.model.pdf import Pdf
from pdf.service.servicepdf import ServicePdf


class Facade:
    """Facade Project Class.

    Author:
        abelbcarvalho
    """

    # access service
    _serv_pdf = ServicePdf()

    def __init__(self) -> None:
        """New Facade.
        """
        pass

    def convert_pdf_to_docx(self, pdf: Pdf) -> bool:
        """Converts from pdf to docx.

        Args:
            pdf (Pdf): pdf file.

        Returns:
            bool: True if converted, False else.
        """
        return self._serv_pdf.convert_pdf_to_docx(pdf=pdf)
