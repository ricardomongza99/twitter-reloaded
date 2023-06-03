from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from tweets.models import Tweet

class ReplyToTweetTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.tweet = Tweet.objects.create(content='Test tweet', user=self.user)

    def test_reply_to_tweet(self):
        # Log in the user
        self.client.login(username=self.username, password=self.password)

        # Send a POST request to create a reply
        url = reverse('create-reply', args=[self.tweet.id])
        response = self.client.post(url, {'content': 'Test reply'})

        # Check if the reply was created successfully
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertEqual(self.tweet.replies.count(), 1)
        self.assertEqual(self.tweet.replies.first().content, 'Test reply')