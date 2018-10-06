from tests import BasicTestCase



class TestMilestone(BasicTestCase):

    def test_new_milestone(self):
        response = self.request(type="mutation",
                                call='appendMilestone(token: "{0}", id: "{1}", newMilestone: "{2}")'
                                .format(self.access_token, str(self.todo_id), "new milestone"),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['appendMilestone']['result']['message'], 'Milestone append success')

    def test_complete_milestone(self):
        response = self.request(type="mutation",
                                call='completeMilestone(token: "{0}", todoId: "{1}", milestoneId: "{2}")'
                                .format(self.access_token, str(self.todo_id), str(self.milestone_id)),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['completeMilestone']['result']['message'], 'Milestone complete success')

    def test_delete_milestone(self):
        response = self.request(type="mutation",
                                call='deleteMilestone(token: "{0}", todoId: "{1}", milestoneId: "{2}")'
                                .format(self.access_token, str(self.todo_id), str(self.milestone_id)),
                                body='''
                                     result{
                                     ... on ResponseMessageField{
                                     isSuccess
                                     message
                                     }
                                     }
                                     ''')

        self.assertEqual(response['deleteMilestone']['result']['message'], 'Milestone delete success')
