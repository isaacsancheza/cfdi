from uuid import UUID
from datetime import datetime

from lxml.etree import _Element


class TimbreFiscalDigital:
    def __init__(self, node: _Element) -> str:
        self._node = node

    @property
    def uuid(self) -> UUID:
        return UUID(self._node.get('UUID'))

    @property
    def version(self) -> str:
        return self._node.get('Version')

    @property
    def rfc_prov_certif(self) -> str:
        return self._node.get('RfcProvCertif')

    @property
    def fecha_timbrado(self) -> datetime:
        return datetime.strptime(self._node.get('FechaTimbrado'), '%Y-%m-%dT%H:%M:%S')

    @property
    def sello_cfd(self) -> str:
        return self._node.get('SelloCFD')

    @property
    def no_certificado_sat(self) -> str:
        return self._node.get('NoCertificadoSAT')

    @property
    def sello_sat(self) -> str:
        return self._node.get('SelloSAT')
