
class Post:
    # 建構式
    def __init__(self):
        self.titles = []

    # 新增文章
    def add_post(self, title):
        self.titles.append(title)

    # 刪除文章
    def delete_post(self, title):
        self.titles.remove(title)