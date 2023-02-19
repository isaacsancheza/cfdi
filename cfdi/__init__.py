from lxml import etree
from decimal import Decimal
from datetime import datetime
from .emisor import Emisor
from .receptor import Receptor
from .concepto import Concepto
from .impuesto import Impuesto
from .complemento import Complemento


class CFDI:
    def __init__(self, string):
        self._root = etree.fromstring(string)

        self.emisor = Emisor(self._root.find('./{%s}Emisor' % self._root.nsmap['cfdi']))
        self.receptor = Receptor(self._root.find('./{%s}Receptor' % self._root.nsmap['cfdi']))
        self.impuestos = Impuesto(self._root.find('./{%s}Impuestos' % self._root.nsmap['cfdi']))
        self.conceptos = [
            Concepto(node) for node in self._root.findall(
                './{%s}Conceptos/{%s}Concepto' % (self._root.nsmap['cfdi'], self._root.nsmap['cfdi'])
            )
        ]
        self.complemento = Complemento(self._root.find('./{%s}Complemento' % self._root.nsmap['cfdi']))

    @property
    def version(self):
        return self._root.get('Version')

    @property
    def fecha(self):
        return datetime.strptime(self._root.get('Fecha'), '%Y-%m-%dT%H:%M:%S')

    @property
    def moneda(self):
        return self._root.get('Moneda')

    @property
    def tipo_cambio(self):
        value = self._root.get('TipoCambio')
        if not value:
            return None
        return Decimal(value)

    @property
    def subtotal(self):
        return Decimal(self._root.get('SubTotal'))

    @property
    def total(self):
        return Decimal(self._root.get('Total'))

    @property
    def forma_pago(self):
        return self._root.get('FormaPago')

    @property
    def condiciones_de_pago(self):
        return self._root.get('CondicionesDePago')

    @property
    def tipo_de_comprobante(self):
        return self._root.get('TipoDeComprobante')

    @property
    def metodo_pago(self):
        return self._root.get('MetodoPago')

    @property
    def lugar_de_expedicion(self):
        return self._root.get('LugarExpedicion')

    @property
    def no_certificado(self):
        return self._root.get('NoCertificado')

    @property
    def exportacion(self):
        return self._root.get('Exportacion')

    @property
    def serie(self):
        return self._root.get('Serie')

    @property
    def folio(self):
        return self._root.get('Folio')

    @property
    def certificado(self):
        return self._root.get('Certificado')

    @property
    def sello(self):
        return self._root.get('Sello')
