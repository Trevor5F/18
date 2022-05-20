from dao.model.author import Author

class AuthorDAO:
    def __int__(self,session):
        self.session = session

    def get_one(self, aid):
        return self.get_one(aid)

    def get_all(self):
        return self.session.query(Author).all()

    def create(self, data):
        author = Author(**data)

        self.session.add(author)
        self.session.commit()


    def update(self, author):
        self.session.add(author)
        self.session.commit()

        return author


    def delete(self, aid):
        author = self.get_one(aid)

        self.session.delete(author)
        self.session.commit()














