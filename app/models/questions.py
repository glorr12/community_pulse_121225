from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, ForeignKey

from app.models import db


class Category(db.Model):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    questions: Mapped[list['Question']] = relationship(back_populates='category')


    def __str__(self):
        return self.name

    def __repr__(self):
        return f'id={self.id}, name={self.name}'


class Question(db.Model):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(100))
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=False)

    statistics: Mapped['Statistics'] = relationship(back_populates='question', uselist=False, cascade='all, delete-orphan')
    responses: Mapped[list['Response']] = relationship(back_populates='question', cascade='all, delete-orphan')
    category: Mapped['Category'] = relationship(back_populates='questions')


    def __str__(self):
        return self.text

    def __repr__(self):
        return f'id={self.id}, text={self.text}'


