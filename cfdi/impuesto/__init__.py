from decimal import Decimal
from traslado import Traslado


class Impuesto:
    def __init__(self, node):
        self._node = node
        self.traslados = [Traslado(node) for node in self._node.findall('.//{%s}Traslado' % self._node.nsmap['cfdi'])]

    @property
    def total_impuestos_trasladados(self):
        total_impuestos_traslados = self._node.get('TotalImpuestosTrasladados')
        if total_impuestos_traslados is not None:
            return Decimal()
