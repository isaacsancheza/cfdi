from lxml.etree import _Element


class Emisor:
    def __init__(self, node: _Element) -> None:
        self._node = node

    @property
    def rfc(self) -> str:
        return self._node.get('Rfc')

    @property
    def nombre(self) -> str:
        return self._node.get('Nombre')

    @property
    def regimen_fiscal(self) -> str:
        return self._node.get('RegimenFiscal')
