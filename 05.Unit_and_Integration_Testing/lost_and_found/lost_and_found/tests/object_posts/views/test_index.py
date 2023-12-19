
from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    def test_index_when_no_posts_expect_empty_posts(self):
        response = self.client.get(
            reverse('index')
        )

        context = response.context

        self.assertEqual(200, response.status_code)
        self.assertEqual('index.html', context['template_name'])
        self.assertEqual(0, len(context['posts']))

