from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class UsersAuth(Base):
    __tablename__ = 'users_auth'
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_fullname = Column(String(255))
    user_birthdate = Column(DateTime)
    user_phonenumber = Column(String(20))
    user_email = Column(String(255))
    user_password = Column(String(255))

class Users2FA(Base):
    __tablename__ = 'users_2fa'
    user_id = Column(Integer, primary_key=True, index=True)
    ota_codes = Column(String(6))

    user = relationship('UsersAuth', back_populates='users_2fa')

class UsersClass(Base):
    __tablename__ = 'users_class'
    user_id = Column(Integer, primary_key=True, index=True)
    user_age = Column(Integer)
    user_proficiency_level = Column(String(50))
    user_pond_total = Column(Integer)
    user_pond_size_range = Column(String(50))
    user_fish_type = Column(String(255))
    user_fish_size_preference = Column(String(50))

    user = relationship('UsersAuth', back_populates='users_class')

class UsersMarket(Base):
    __tablename__ = 'users_market'
    user_id = Column(Integer, primary_key=True, index=True)
    user_production_capacity_n = Column(Integer)
    user_production_capacity_unit = Column(String(50))
    user_production_capacity_cycle = Column(String(50))
    user_market_capacity_n = Column(Integer)
    user_market_capacity_unit = Column(String(50))
    user_market_capacity_cycle = Column(String(50))
    user_market_preference = Column(String(255))

    user = relationship('UsersAuth', back_populates='market')

class UsersPondsAddress(Base):
    __tablename__ = 'users_ponds_address'
    pond_address_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users_auth.user_id'))
    user_address_full = Column(String(255))
    user_address_province = Column(String(255))
    user_address_city = Column(String(255))
    user_address_subdistrict = Column(String(255))
    user_address_zipcode = Column(String(20))
    user_address_coordinates = Column(String(100))

    user = relationship('UsersAuth', back_populates='ponds_addresses')

class UsersPrimaryAddress(Base):
    __tablename__ = 'users_primary_address'
    user_id = Column(Integer, ForeignKey('users_auth.user_id'), primary_key=True)
    pond_address_id = Column(Integer, ForeignKey('users_ponds_address.pond_address_id'))

    user = relationship('UsersAuth', back_populates='primary_address')
    pond_address = relationship('UsersPondsAddress', back_populates='primary_address')

class UsersHarvestPlan(Base):
    __tablename__ = 'users_harvest_plan'

    harvest_plan_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users_auth.user_id'))
    user_province = Column(String(255))
    user_city = Column(String(255))
    harvest_plan_start = Column(String(255))
    harvest_plan_end = Column(String(255))
    harvest_plan_dayofcultivation = Column(Integer)
    harvest_plan_readyonmonth = Column(Integer)
    harvest_plan_pond_total = Column(Integer)
    harvest_plan_pond_size = Column(Integer)
    harvest_plan_fish_type = Column(String(255))
    harvest_plan_target_capacity = Column(String(255))
    harvest_plan_target_size = Column(String(255))
    harvest_plan_total_fish = Column(String(255))

class CommunityCache(Base):
    __tablename__ = 'community_cache'

    community_id = Column(Integer, primary_key=True)
    community_province = Column(String(255))
    community_city = Column(String(255))
    community_month = Column(String(255))
    community_fish_type = Column(String(255))
    community_production_total = Column(Integer)
    community_user_total = Column(Integer)