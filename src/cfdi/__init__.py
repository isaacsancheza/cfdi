from decimal import Decimal
from datetime import datetime

from lxml import etree

from cfdi.emisor import Emisor
from cfdi.receptor import Receptor
from cfdi.concepto import Concepto
from cfdi.impuesto import Impuesto
from cfdi.complemento import Complemento


class CFDI:
    def __init__(self, string: str) -> None:
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
    def version(self) -> str :
        return self._root.get('Version')

    @property
    def fecha(self) -> datetime:
        return datetime.strptime(self._root.get('Fecha'), '%Y-%m-%dT%H:%M:%S')

    @property
    def moneda(self) -> str:
        return self._root.get('Moneda')

    @property
    def tipo_cambio(self) -> Decimal | None:
        value = self._root.get('TipoCambio')
        if not value:
            return None
        return Decimal(value)

    @property
    def subtotal(self) -> Decimal:
        return Decimal(self._root.get('SubTotal'))

    @property
    def total(self) -> Decimal:
        return Decimal(self._root.get('Total'))

    @property
    def forma_pago(self) -> str:
        return self._root.get('FormaPago')

    @property
    def condiciones_de_pago(self) -> str:
        return self._root.get('CondicionesDePago')

    @property
    def tipo_de_comprobante(self) -> str:
        return self._root.get('TipoDeComprobante')

    @property
    def metodo_pago(self) -> str:
        return self._root.get('MetodoPago')

    @property
    def lugar_de_expedicion(self) -> str:
        return self._root.get('LugarExpedicion')

    @property
    def no_certificado(self) -> str:
        return self._root.get('NoCertificado')

    @property
    def exportacion(self) -> str:
        return self._root.get('Exportacion')

    @property
    def serie(self) -> str:
        return self._root.get('Serie')

    @property
    def folio(self) -> str:
        return self._root.get('Folio')

    @property
    def certificado(self) -> str:
        return self._root.get('Certificado')

    @property
    def sello(self) -> str:
        return self._root.get('Sello')
