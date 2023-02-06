class Emisor:
    def __init__(self, node):
        self._node = node

    @property
    def rfc(self):
        return self._node.get('Rfc')

    @property
    def nombre(self):
        return self._node.get('Nombre')

    @property
    def regimen_fiscal(self):
        return self._node.get('RegimenFiscal')
