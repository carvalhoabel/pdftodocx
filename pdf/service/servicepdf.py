from pdf.model.pdf import Pdf
from core.singleton.singmessage import SingMessage as Msg
from core.tools.tools import isitdir, isitfile
from core.conversor.conversor import Conversor


class ServicePdf:
    """Service checks from model pdf.

    Author:
        abelbcarvalho    
    """

    def __init__(self) -> None:
        """New Pdf Service.
        """
        self._conversor = Conversor()

    @property
    def conversor(self) -> Conversor:
        return self._conversor

    def convert_pdf_to_docx(self, pdf: Pdf) -> bool:
        """Converts from pdf to docx.

        Args:
            pdf (Pdf): pdf file.

        Returns:
            bool: True if converted, False else.
        """
        if not pdf.pathpdf:
            Msg.message().cleardata()
            Msg.message().message = 'Warning! Pdf path Empty'
            Msg.message().title = 'Warning - Pdf Path'
            Msg.message().warning = True
            return False
        if not pdf.pathdocx:
            Msg.message().cleardata()
            Msg.message().message = 'Warning! Docx path save empty'
            Msg.message().title = 'Warning - Docx path'
            Msg.message().warning = True
            return False
        if not isitfile(pathfile=pdf.pathpdf):
            Msg.message().cleardata()
            Msg.message().message = 'Warning! Pdf not exists'
            Msg.message().title = 'Warning - Pdf File'
            Msg.message().warning = True
            return False
        if not isitdir(path=pdf.pathdocx):
            Msg.message().cleardata()
            Msg.message().message = 'Warning! Docx saving invalid path'
            Msg.message().title = 'Warning - Docx File'
            Msg.message().warning = True
            return False
        if not pdf.name:
            name = list(pdf.pathpdf)
            name.reverse()
            name = name[:name.index('/')]
            name.reverse()
            pdf.name = ''.join(name)
        if pdf.name.__len__() < 2:
            pdf.name = '/filedocx.docx'
        elif pdf.name[0] != '/':
            pdf.name = f'/{pdf.name}'
        # checking success
        if self.conversor.convert_pdf_to_docx(pdf=pdf):
            Msg.message().cleardata()
            Msg.message().message = 'Sucess! PDF was changed to Docx'
            Msg.message().title = 'Success - PDF Convertort'
            Msg.message().info = True
            return True
        else:
            Msg.message().cleardata()
            Msg.message().message = 'Error! PDF wasn\'t changed to Docx'
            Msg.message().title = 'Error - PDF Convertort'
            Msg.message().error = True
            return False
