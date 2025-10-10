class Tiktok:
    """TikTok аккаунт клиники (управляется только через SSM)"""

    def __init__(self, account_name: str):
        self.account_name = account_name
        self.__posts = []
        self.__likes = 0
        self.__followers = 0

    # ====== Приватные методы — доступны только SSM ======
    def _upload_post(self, author: str, content: str) -> str:
        self.__posts.append({"author": author, "content": content})
        self.__likes += 10
        return f"{author} uploaded '{content}' to TikTok."

    def _get_stats(self) -> str:
        return (
            f"TikTok ({self.account_name}): {len(self.__posts)} posts, "
            f"{self.__likes} likes, {self.__followers} followers."
        )

    # ====== Публичная информация ======
    def get_public_info(self) -> str:
        """Показывает только имя аккаунта и количество постов"""
        return f"TikTok page '{self.account_name}' — {len(self.__posts)} posts."
