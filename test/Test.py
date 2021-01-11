from src.apiManager import Tableau as tableau
from src.apiManager import Meli as meli
from src.util import Global as glo

import unittest

class TestChallenge(unittest.TestCase):
    # Test-Unitarios
    def test_meli_get_results_valores_entrada(self):
        api = meli.Meli()
        assert api.get_results("####%$&##$#%%#") == None, "No debe aceptar caracteres especiales y ser Null."
        assert api.get_results(None) == None, "No debe aceptar un Null como parametro."

    def test_tableau_extract_search_results(self):
        ta = tableau.Tableau()
        assert ta.extract_search_results(None) == None, "No debe aceptar Null como parametro."
        assert ta.read_data_from_hyper("results") == True, "Debe devolver True."
        assert ta.read_data_from_hyper(None) == False, "No debe aceptar Null como parametro."

    def test_global_send_request(self):
        g = glo.Global()
        assert g.send_request("https:/dsddssjdksjks","{dsdsdsdsds}") == None, "Ante parametros errones debe devolver None."



if __name__ == '__main__':
    unittest.main()
