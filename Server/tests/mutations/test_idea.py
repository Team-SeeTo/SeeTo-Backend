from tests import BasicTestCase


class TestIdea(BasicTestCase):

    def test_new_idea(self):
        response = self.request(type="mutation",
                                call='newIdea(token: "{0}", title: "{1}", body: "{2}", category: "{3}")'
                                .format(self.access_token, "idea title", "idea body", "TEST"),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['newIdea']['result']['message'], 'Idea upload success')

    def test_edit_idea(self):
        response = self.request(type="mutation",
                                call='editIdea(token: "{0}", id: "{1}", update: "{2}")'
                                .format(self.access_token, str(self.idea_id), "updated body"),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['editIdea']['result']['message'], 'Idea update success')

    def test_new_comment(self):
        response = self.request(type="mutation",
                                call='newComment(token: "{0}", id: "{1}", comment: "{2}")'
                                .format(self.access_token, str(self.idea_id), "new comment"),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['newComment']['result']['message'], 'Comment upload success')

    def test_delete_idea(self):
        response = self.request(type="mutation",
                                call='deleteIdea(token: "{0}", id: "{1}")'
                                .format(self.access_token, str(self.idea_id)),
                                body='''
                                      result{
                                      ... on ResponseMessageField{
                                      isSuccess
                                      message
                                      }
                                      }
                                      ''')

        self.assertEqual(response['deleteIdea']['result']['message'], 'Idea delete success')

    def test_vote_idea(self):
        response = self.request(type="mutation",
                                call='voteIdea(token: "{0}", id: "{1}")'
                                .format(self.access_token, str(self.idea_id)),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['voteIdea']['result']['message'], 'Vote cancel success')

    def test_vote_cancel_idea(self):
        self.request(type="mutation",
                                call='voteIdea(token: "{0}", id: "{1}")'
                                .format(self.access_token, str(self.idea_id)),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        response = self.request(type="mutation",
                                call='voteIdea(token: "{0}", id: "{1}")'
                                .format(self.access_token, str(self.idea_id)),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['voteIdea']['result']['message'], 'Vote success')