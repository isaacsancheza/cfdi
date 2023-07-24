from decimal import Decimal

from lxml.etree import _Element

from cfdi.concepto.impuesto import Impuesto


class Concepto:
    def __init__(self, node: _Element) -> None:
        self._node = node
        self.impuestos = Impuesto(self._node.find('./{%s}Impuestos' % self._node.nsmap['cfdi']))

    @property
    def clave_prod_serv(self) -> str:
        return self._node.get('ClaveProdServ')

    @property
    def no_identificacion(self) -> str:
        return self._node.get('NoIdentificacion')

    @property
    def cantidad(self) -> str:
        return self._node.get('Cantidad')

    @property
    def clave_unidad(self) -> str:
        return self._node.get('ClaveUnidad')

    @property
    def unidad(self) -> str:
        return  self._node.get('Unidad')

    @property
    def descripcion(self) -> str:
        return self._node.get('Descripcion')

    @property
    def valor_unitario(self) -> Decimal:
        return Decimal(self._node.get('ValorUnitario'))

    @property
    def importe(self) -> Decimal:
        return Decimal(self._node.get('Importe'))

    @property
    def objeto_imp(self) -> str:
        return self._node.get('ObjetoImp')

    @property
    def descuento(self) -> str:
        return self._node.get('Descuento')
