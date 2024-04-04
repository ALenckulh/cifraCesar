from src.main import criptografa
from src.main import descriptografa

originalCrip = 'AÇaí bom'
originalDes = 'DcdA erp'
indice = 3
alfabeto = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'


class TestCriptografa:

    def test_criptografa(self):
        assert criptografa(originalCrip, indice, alfabeto) == 'DcdA erp'

    def test_descriptografa(self):
        assert descriptografa(originalDes, indice, alfabeto) == 'AÇaí bom'
