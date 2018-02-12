from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

# http://docs.sqlalchemy.org/en/latest/core/engines.html

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Delete Categories if exisitng.
session.query(Category).delete()

# Delete Items if exisitng.
session.query(Items).delete()

# Delete Users if exisitng.
session.query(User).delete()

# Create fake users
User1 = User(name="Sarabeth Jaffe",
              email="sarabethjaffe@gmail.com",
              picture='https://media.licdn.com/mpr/mpr/shrinknp_200_200/p/6/005/020/01d/18b03dd.jpg')
session.add(User1)
session.commit()

# Create fake categories
Category1 = Category(name="Personal",
                      user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Technology",
                      user_id=1)
session.add(Category2)
session.commit

Category3 = Category(name="Random",
                      user_id=1)
session.add(Category3)
session.commit()

# Populate a category with items for testing
# Using different users for items also
Item1 = Items(name="New Year",
               date=datetime.datetime.now(),
               description="My goals for 2018 are as follows...",
               picture="https://res.cloudinary.com/simpleview/image/upload/crm/rockford/2018-new-year_f643b39b-5056-a36a-06e721e7517957c8.png",
               category_id=1,
               user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="React",
               date=datetime.datetime.now(),
               description="ReactJS is a web framework...",
               picture="http://blog-assets.risingstack.com/2016/Jan/react_best_practices-1453211146748.png",
               category_id=2,
               user_id=1)
session.add(Item2)
session.commit()

Item3 = Items(name="Food",
               date=datetime.datetime.now(),
               description="Cheese",
               picture="https://www.greatlakescheese.com/Data/Sites/24/images/homepage/hp-hero-quality.jpg",
               category_id=3,
               user_id=1)
session.add(Item3)
session.commit()

print "Database initialized"