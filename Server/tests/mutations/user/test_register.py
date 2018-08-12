from tests import BasicTestCase


class TestRegister(BasicTestCase):
    def setUp(self):
        pass

    def test_register(self):
        response = self.request(type="mutation",
                                call='register(email:"test@seeto.services", username: "lewis", password:"admin1234")',
                                body='''
                                message
                                ''')

        self.assertEqual(response['register']['message'], 'Successfully registered')