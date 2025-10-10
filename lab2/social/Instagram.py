class Instagram:
    def __init__(self, account_name: str):
        self.account_name = account_name
        self.__posts = []
        self.__stories = 0

    def _upload_post(self, author: str, content: str) -> str:
        self.__posts.append({"author": author, "content": content})
        return f"{author} posted '{content}' on Instagram."

    def _upload_story(self, author: str, content: str) -> str:
        self.__stories += 1
        return f"{author} posted a story: '{content}'."

    def get_public_info(self) -> str:
        """Только общее описание — без доступа к постам"""
        return f"Instagram account '{self.account_name}' — {len(self.__posts)} posts."
