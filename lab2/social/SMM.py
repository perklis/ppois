from employees.Employee import Employee
from social.TikTok import Tiktok
from social.Instagram import Instagram
from employees.Doctor import Doctor
from typing import List, Optional


class SMM(Employee):
    def __init__(
        self, job_title: str, name: str, age: int, work_experience: int, salary: float
    ):
        super().__init__(job_title, name, age, work_experience, salary)
        self.__interviewed_doctors: List[Doctor] = []
        self.__posts_archive: List[str] = []
        self.__tiktok: Optional[Tiktok] = None
        self.__instagram: Optional[Instagram] = None

    def connect_tiktok(self, account: Tiktok):
        self.__tiktok = account
        return f"{self.name} connected TikTok account '{account.account_name}'"

    def connect_instagram(self, account: Instagram):
        self.__instagram = account
        return f"{self.name} connected Instagram account '{account.account_name}'"

    def take_interview(self, doctor: Doctor, topic: str) -> str:
        self.__interviewed_doctors.append(doctor)
        text = f"Interview with {doctor.name} on topic: '{topic}'"
        return text

    def publish_post(self, platform: str, content: str) -> str:
        if platform.lower() == "tiktok":
            if not self.__tiktok:
                raise PermissionError("TikTok account not connected")
            result = self.__tiktok._upload_post(self.name, content)
        elif platform.lower() == "instagram":
            if not self.__instagram:
                raise PermissionError("Instagram account not connected")
            result = self.__instagram._upload_post(self.name, content)
        else:
            raise ValueError("Unknown platform")

        self.__posts_archive.append(content)
        return result

    def publish_story(self, content: str) -> str:
        if not self.__instagram:
            raise PermissionError("Instagram not connected")
        return self.__instagram._upload_story(self.name, content)
