import unittest
from app import app, maxwells_equations, quark_mass_energy, gluon_strength, lepton_oscillation_probability, boson_mass, higgs_coupling

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Helper function tests
    def test_quark_mass_energy(self):
        self.assertAlmostEqual(quark_mass_energy(1e-30), 9e-14)
    
    def test_gluon_strength(self):
        self.assertAlmostEqual(gluon_strength(0.2, 0.1), 2.0)
    
    def test_boson_mass(self):
        self.assertAlmostEqual(boson_mass(1e-15), 6.626e-34 / (1e-15 * 3e8), places=20)
    
    def test_higgs_coupling(self):
        self.assertAlmostEqual(higgs_coupling(125, 246), 125 / (246 * (2**0.5)), places=4)

    # Route tests
    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Quantum Physics Calculators', response.data)

    def test_maxwell_route_get(self):
        response = self.app.get('/maxwell')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Maxwell\'s Equations Calculator', response.data)

    def test_maxwell_calculation(self):
        response = self.app.post('/maxwell', data=dict(
            E=1e3, B=0.5, rho=1e-6, J=100
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Gauss&#39;s Law for Electricity', response.data)

    def test_quark_route(self):
        response = self.app.get('/quantum/quark')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Quark Mass-Energy Calculator', response.data)

    def test_quark_calculation(self):
        response = self.app.post('/quantum/quark', data={'mass': 1e-30})
        self.assertIn(b'9.00e-14 J', response.data)

    def test_gluon_calculation(self):
        response = self.app.post('/quantum/gluon', data={
            'alpha_s': 0.3, 'distance': 0.15
        })
        self.assertIn(b'2.00e+00 GeV/fm', response.data)

    def test_lepton_calculation(self):
        response = self.app.post('/quantum/lepton', data={
            'theta': 0.785, 'L': 295, 'E': 2.5
        })
        self.assertIn(b'Oscillation probability:', response.data)

    def test_invalid_input_handling(self):
        response = self.app.post('/quantum/quark', data={'mass': 'not_a_number'})
        self.assertIn(b'Invalid input', response.data)

    def test_boson_route(self):
        response = self.app.get('/quantum/boson')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Boson Mass Calculator', response.data)

    def test_higgs_route(self):
        response = self.app.get('/quantum/higgs')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Higgs Coupling Calculator', response.data)

    def test_higgs_calculation(self):
        response = self.app.post('/quantum/higgs', data={
            'mass': 125, 'vev': 246
        })
        self.assertIn(b'Yukawa coupling: 0.359', response.data)

if __name__ == '__main__':
    unittest.main()