import unittest
from main import database, buscar_datos

class TestDatabase(unittest.TestCase):
    def test_buscar_datos_Franco(self):
        self.assertEqual(buscar_datos("Franco", "José", "Vaccarezza", "Toro", **database), "persona1")
    def test_buscar_datos_Josias(self):    
        self.assertEqual(buscar_datos("Josias", "Lautaro", "Vilches", "Nuñez", **database), "persona6")
    def test_buscar_datos_Candela(self):       
        self.assertEqual(buscar_datos("Candela", "Victoria", "Gonzalez", **database), "persona7")
    def test_buscar_datos_Franco_Pepito(self):
        self.assertEqual(buscar_datos("Franco", "Aporta", "Barzola", **database), "persona5")
    def test_buscar_datos_Maxi(self):
        self.assertEqual(buscar_datos("Maximo", "José", "Lucentini", "Sanchez", **database), "persona4")
    def test_buscar_datos_Alejandro(self):
        self.assertEqual(buscar_datos("Castellino", "Alejandro", "Sanchez", **database), "persona3")
    def test_buscar_datos_Nahuel(self):
        self.assertEqual(buscar_datos("Lionel", "Andres", "Messi", **database), None)


unittest.main()