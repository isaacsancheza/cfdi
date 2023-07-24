from lxml.etree import _Element

from cfdi.complemento.timbre_fiscal_digital import TimbreFiscalDigital


class Complemento:
    def __init__(self, node: _Element) -> None:
        self._node = node

        # extract namespaces
        children = list(node)
        namespaces = dict()
        
        for child in children:
            namespaces.update(child.nsmap)

        self.timbre_fiscal_digital = TimbreFiscalDigital(
            self._node.find('./{%s}TimbreFiscalDigital' % namespaces['tfd'])
        )
