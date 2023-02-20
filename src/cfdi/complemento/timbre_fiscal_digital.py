from datetime import datetime


class TimbreFiscalDigital:
    def __init__(self, node):
        self._node = node

    @property
    def uuid(self):
        return self._node.get('UUID')

    @property
    def version(self):
        return self._node.get('Version')

    @property
    def rfc_prov_certif(self):
        return self._node.get('RfcProvCertif')

    @property
    def fecha_timbrado(self):
        return datetime.strptime(self._node.get('FechaTimbrado'), '%Y-%m-%dT%H:%M:%S')

    @property
    def sello_cfd(self):
        return self._node.get('SelloCFD')

    @property
    def no_certificado_sat(self):
        return self._node.get('NoCertificadoSAT')

    @property
    def sello_sat(self):
        return self._node.get('SelloSAT')
