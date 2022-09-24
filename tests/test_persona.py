import datetime
import unittest
from  src.pruebas_git_actions.modelo.persona import Persona

#comntario
class test_persona(unittest.TestCase):
    def setUp(self):
        self.persona1 = Persona( nombre= 'Alejandra' ,edad= 25 , apellido = "Wilches", tipo_doc=1 , nro_doc= "11448243" )
        self.persona2 = Persona(nombre='Diego', edad=22 ,  apellido = "wilches", tipo_doc=1 , nro_doc= "11448243" )
        self.persona3 = Persona(nombre='Alejandra', edad=25 ,  apellido = "wilches" , tipo_doc=1 , nro_doc= "11448243")
        self.persona4 = Persona(nombre='Diana', edad=25,  apellido = "wilches", tipo_doc=1 , nro_doc= "11448243" )
        self.grupo = [ self.persona1 , self.persona2 , self.persona3 ]
    
    def test_constructor(self):
        self.assertEqual( self.persona1.dar_nombre() , 'Alejandra')
        self.assertEqual( self.persona1.dar_edad() , 25)

    def test_anio_nacimiento(self):
        self.assertEqual(self.persona1.calcular_anio_nacimiento(True), datetime.datetime.now().year - 25)
        self.assertNotEqual(self.persona1.calcular_anio_nacimiento(False), datetime.datetime.now().year - 25)
        self.assertEqual(self.persona1.calcular_anio_nacimiento(False), datetime.datetime.now().year - 25 + 1)
        self.assertNotEqual(self.persona1.calcular_anio_nacimiento(True), datetime.datetime.now().year - 25 + 1)

    def test_asingacion(self):
        self.persona2.asignar_edad(28)
        self.persona2.asignar_nombre("Felipe")
        self.assertFalse(self.persona2.dar_nombre()=='Diego')
        self.assertFalse(self.persona2.dar_edad()==22)
        self.assertTrue(self.persona2.dar_nombre()=='Felipe')
        self.assertTrue(self.persona2.dar_edad()==28)

    def test_nombre_completo(self ):
        self.assertTrue(self.persona1.dar_nombre_completo()=='Alejandra Wilches')

    def test__recura_cedula_ok(self):
        tipo_doc , nro_doc = self.persona1.dar_info_documento()
        self.assertEquals( tipo_doc, 1   )
        self.assertEquals( nro_doc,"11448243" )

    def test_objetos_iguales(self):
        persona_nueva = self.persona1
        self.assertIsNot(self.persona1, self.persona3)
        self.assertIs(self.persona1, persona_nueva)

    def test_elemento_en_conjunto(self):
        self.assertIn(self.persona3, self.grupo)
        self.assertNotIn(self.persona4, self.grupo)

    def test_instancia_clase(self):
        self.assertIsInstance(self.persona1, Persona)
        self.assertNotIsInstance(self.grupo, Persona)