from lxml.etree import _Element


class Receptor:
    def __init__(self, node: _Element) -> None:
        self._node = node
        
    @property
    def rfc(self) -> str:
        return self._node.get('Rfc')
    
    @property
    def nombre(self) -> str:
        return self._node.get('Nombre')
    
    @property
    def uso_de_cfdi(self) -> str:
        return self._node.get('UsoCFDI')

    @property
    def domicilio_fiscal(self) -> str:
        return self._node.get('DomicilioFiscalReceptor')

    @property
    def regimen_fiscal(self) -> str:
        return self._node.get('RegimenFiscalReceptor')
