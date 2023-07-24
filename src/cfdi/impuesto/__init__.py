from decimal import Decimal

from lxml.etree import _Element

from cfdi.impuesto.traslado import Traslado


class Impuesto:
    def __init__(self, node: _Element) -> None:
        self._node = node
        self.traslados = [
            Traslado(node) for node in self._node.findall(
                './{%s}Traslados/{%s}Traslado' % (self._node.nsmap['cfdi'], self._node.nsmap['cfdi'])
            )
        ]

    @property
    def total_impuestos_trasladados(self) -> Decimal | None:
        total_impuestos_traslados = self._node.get('TotalImpuestosTrasladados')
        if total_impuestos_traslados is not None:
            return Decimal(total_impuestos_traslados)
