from decimal import Decimal

from lxml.etree import _Element


class Traslado:
    def __init__(self, node: _Element) -> None:
        self._node = node

    @property
    def impuesto(self) -> str:
        return self._node.get('Impuesto')

    @property
    def tipo_factor(self) -> str:
        return self._node.get('TipoFactor')

    @property
    def tasa_o_cuota(self) -> Decimal:
        return Decimal(self._node.get('TasaOCuota'))

    @property
    def importe(self) -> Decimal:
        return Decimal(self._node.get('Importe'))

    @property
    def base(self) -> Decimal | None:
        value = self._node.get('Base', None)
        if not value:
            return None
        return Decimal(value)
