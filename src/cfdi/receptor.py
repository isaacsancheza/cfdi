class Receptor:
    def __init__(self, node):
        self._node = node
        
    @property
    def rfc(self):
        return self._node.get('Rfc')
    
    @property
    def nombre(self):
        return self._node.get('Nombre')
    
    @property
    def uso_de_cfdi(self):
        return self._node.get('UsoCFDI')

    @property
    def domicilio_fiscal(self):
        return self._node.get('DomicilioFiscalReceptor')

    @property
    def regimen_fiscal(self):
        return self._node.get('RegimenFiscalReceptor')
