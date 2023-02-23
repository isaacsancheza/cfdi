from cfdi import CFDI
from cfdi.utils import serialize


def test_serializer():
    with open('tests/invoice.xml', 'r') as f:
        string = f.read().encode('utf-8')
    cfdi = CFDI(string)
    serialize(cfdi)
