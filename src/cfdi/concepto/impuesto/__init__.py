from lxml.etree import _Element

from cfdi.concepto.impuesto.traslado import Traslado


class Impuesto:
    def __init__(self, node: _Element) -> None:
        self._node = node
        self.traslados = [
            Traslado(node) for node in self._node.findall(
                './{%s}Traslados/{%s}Traslado' % (self._node.nsmap['cfdi'], self._node.nsmap['cfdi'])
            )
        ]
