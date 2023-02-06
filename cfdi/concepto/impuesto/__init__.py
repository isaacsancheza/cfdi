from .traslado import Traslado


class Impuesto:
    def __init__(self, node):
        self._node = node
        self.traslados = [Traslado(node) for node in self._node.findall('.//{%s}Traslado' % self._node.nsmap['cfdi'])]
