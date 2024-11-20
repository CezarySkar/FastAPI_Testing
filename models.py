from sqlalchemy import Boolean, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    first_name = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    password = Column(String(128))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
class Order(Base):
    __tablename__ = 'order'

    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey('user.user_id', ondelete='CASCADE'),
        nullable=False
    )
    company_id = Column(
        Integer,
        ForeignKey('company.company_id', ondelete='CASCADE'),
        nullable=False
    )

    company = relationship('Company', backref='order')
    user = relationship('User', backref='order')

class Company(Base):
    __tablename__ = 'company'

    company_id = Column(Integer, index=True, primary_key=True)
    name = Column(String(50), index=True)
    address = Column(String(50), index=True)
    country = Column(String(50), index=True)