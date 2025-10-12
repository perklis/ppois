import unittest
from social.SMM import SMM
from social.TikTok import Tiktok
from social.Instagram import Instagram
from employees.Doctor import Doctor
from exceptions import SocialMediaConnectError


class TestSMM(unittest.TestCase):
    def setUp(self):
        self.smm = SMM("SMM Specialist", "Alice", 28, 5, 3000)
        self.doctor = Doctor(
            job_title="Doctor",
            name="Bob",
            age=40,
            work_experience=15,
            salary=12000,
            specialisation="Cardiology",
            department="Heart Department",
        )

    def test_connect_tiktok_and_instagram(self):
        tiktok_account = Tiktok("alice_tiktok")
        instagram_account = Instagram("alice_insta")

        msg1 = self.smm.connect_tiktok(tiktok_account)
        self.assertIn("connected TikTok", msg1)

        msg2 = self.smm.connect_instagram(instagram_account)
        self.assertIn("connected Instagram", msg2)

    def test_publish_post_on_tiktok(self):
        tiktok_account = Tiktok("alice_tiktok")
        self.smm.connect_tiktok(tiktok_account)
        result = self.smm.publish_post("tiktok", "New video!")
        self.assertIn("uploaded 'New video!'", result)

    def test_publish_post_on_instagram(self):
        instagram_account = Instagram("alice_insta")
        self.smm.connect_instagram(instagram_account)
        result = self.smm.publish_post("instagram", "New photo!")
        self.assertIn("posted 'New photo!'", result)

    def test_publish_post_without_connection_raises_error(self):
        with self.assertRaises(SocialMediaConnectError):
            self.smm.publish_post("tiktok", "Hello world")
        with self.assertRaises(SocialMediaConnectError):
            self.smm.publish_post("instagram", "Hello world")

    def test_publish_story_requires_instagram(self):
        instagram_account = Instagram("alice_insta")
        self.smm.connect_instagram(instagram_account)
        result = self.smm.publish_story("My story")
        self.assertIn("posted a story", result)

        smm2 = SMM("SMM Specialist", "Charlie", 25, 3, 2500)
        with self.assertRaises(SocialMediaConnectError):
            smm2.publish_story("No insta story")

    def test_take_interview(self):
        text = self.smm.take_interview(self.doctor, "Heart health")
        self.assertIn("Interview with Bob", text)
        self.assertIn("Heart health", text)
