from .timbre_fiscal_digital import TimbreFiscalDigital


class Complemento:
    def __init__(self, node):
        self._node = node
        self.timbre_fiscal_digital = TimbreFiscalDigital(
            self._node.find('./{%s}TimbreFiscalDigital' % self._node.nsmap['tfd'])
        )
