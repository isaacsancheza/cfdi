from decimal import Decimal


class Traslado:
    def __init__(self, node):
        self._node = node

    @property
    def impuesto(self):
        return self._node.get('Impuesto')

    @property
    def tipo_factor(self):
        return self._node.get('TipoFactor')

    @property
    def tasa_o_cuota(self):
        return Decimal(self._node.get('TasaOCuota'))

    @property
    def importe(self):
        return Decimal(self._node.get('Importe'))

    @property
    def base(self):
        return Decimal(self._node.get('Base'))
