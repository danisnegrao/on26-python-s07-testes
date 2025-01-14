def soma(a, b):
    return a + b

import unittest

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertAlmostEqual(soma(4,4),8)

    def test_soma_negativos(self):
        self.assertAlmostEqual(soma(-4,-4),-8)
    
    def test_soma_zeros(self):
        self.assertAlmostEqual(soma(0,0),0)

    def  test_soma_de_sinais_diferentes(self):
        self.assertAlmostEqual(soma(-5,1), -4)   


if __name__ == '__main__':
    unittest.main()