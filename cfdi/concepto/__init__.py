from impuesto import Impuesto


class Concepto:
    def __init__(self, node):
        self._node = node
        self.impuestos = Impuesto(self._node.find('.//{%s}Impuestos' % self._node.nsmap['cfdi']))

    @property
    def clave_prod_serv(self):
        return self._node.get('ClaveProdServ')

    @property
    def no_identificacion(self):
        return self._node.get('NoIdentificacion')

    @property
    def cantidad(self):
        return self._node.get('Cantidad')

    @property
    def clave_unidad(self):
        return self._node.get('ClaveUnidad')

    @property
    def unidad(self):
        return  self._node.get('Unidad')

    @property
    def descripcion(self):
        return self._node.get('Descripcion')

    @property
    def valor_unitario(self):
        return self._node.get('ValorUnitario')

    @property
    def importe(self):
        return self._node.get('Importe')

    @property
    def objeto_imp(self):
        return self._node.get('ObjetoImp')

    @property
    def descuento(self):
        return self._node.get('Descuento')
