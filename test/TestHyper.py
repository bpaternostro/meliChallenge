from src.apiManager import Tableau as tableau
#NOTA. No es una prueba unitaria. Es para validar el resultado.
ta= tableau.Tableau()
ta.read_data_from_hyper("results")
