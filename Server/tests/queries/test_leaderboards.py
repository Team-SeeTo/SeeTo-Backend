from tests import BasicTestCase


class TestLeaderboards(BasicTestCase):
    def test_leaderboards(self):
        response = self.request(type="query",
                                call='leaderboards(token :"{0}")'.format(self.access_token),
                                body='''
                                ... on LeaderboardsField{
                                    rank
                                    name
                                    point
                                }
                                ''')

        for user in response['leaderboards']:
            self.assertEqual(type(user['rank']), int)
            self.assertEqual(type(user['name']), str)
            self.assertEqual(type(user['point']), int)
