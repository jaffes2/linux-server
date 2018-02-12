from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref

Base = declarative_base() # returns base class for which all mapped classes will inherit

# http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/basic_use.html

# Store Users
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
    picture = Column(String(250))
    
# Store Categories
class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key = True)
    name = Column(String(255), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="category") # keep track of who created it

    @property
    def serialize(self):
        return {
            'name'      : self.name,
            'id'        : self.id
        }

# Store individual items
class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    date = Column(DateTime, nullable=False)
    description = Column(String(250))
    picture = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category, backref=backref('items', cascade='all, delete')) 
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="items") # keep track of who created it

    @property
    def serialize(self):
        return {
            'name'       : self.name,
            'id'         : self.id,
            'description': self.description,
            'picture'    : self.picture,
            'category'   : self.category.name
        }

# Create sqlite Database
engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)