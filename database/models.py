from sqlalchemy import Column, Integer, Table, String, ForeignKey, create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

association_table = Table(
    'association_table', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('book_id', Integer, ForeignKey('books.id'))
)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    author = Column(String(30), nullable=False)
    readers = relationship('User', secondary=association_table, back_populates='books', lazy=True)
    reviews = relationship('Reviews', backref='book', lazy=True)
    film = relationship('Film', back_populates='book', uselist=False, lazy=True)
    
    def __repr__(self):
        return self.title
    
class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    text = Column(String(2000), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'От {self.reviewer}'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    books = relationship('Book', secondary=association_table, back_populates='readers', lazy=True)
    reviews = relationship('Reviews', backref='reviewer', lazy=True)

    def __repr__(self):
        return self.name

class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    producer = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship('Book', back_populates='film', uselist=False, lazy=True)
    
engine = create_engine('postgresql://postgres:Ulyana06112003@localhost:5432/postgres', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

book1 = session.query(Book).filter_by(title='Робинзон Крузо').first()
film1 = Film(name='Невероятные приключения Робинзона', producer='Квентин Тарантино', book_id=book1.id)
session.add(film1)
session.commit()







