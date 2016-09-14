from django.core import mail
from django.test import TestCase


class MailSubscribe(TestCase):
    def setUp(self):
        data = dict(name='Flávio Henrique Ferreira', cpf='11111111120',
                    email='flaviometalvale@gmail.com', phone='16 99208-4635')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_to(self):
        expect = ['contato@eventex.com.br', 'flaviometalvale@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_body(self):
        contents = (
            'Flávio Henrique Ferreira',
            '11111111120',
            'flaviometalvale@gmail.com',
            '16 99208-4635'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
