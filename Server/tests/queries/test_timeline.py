from tests import BasicTestCase
import datetime


class TestTimeLine(BasicTestCase):
    def test_timeline(self):
        response = self.request(type="query",
                     call='timeline(token: "{0}")'.format(self.access_token),
                     body='''
                     date
                     todo{
                        totalPoint
                     }
                     ideas{
                        totalPoint
                     }
                     totalPoint
                     ''')

        self.assertEqual(type(response['timeline']['totalPoint']), int)
        self.assertEqual(type(response['timeline']['todo']['totalPoint']), int)
        self.assertEqual(type(response['timeline']['ideas']['totalPoint']), int)

