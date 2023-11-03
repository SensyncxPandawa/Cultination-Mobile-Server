from sqlalchemy import Column, DateTime, Date, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class UsersAuth(Base):
    __tablename__ = 'users_auth'
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_fullname = Column(String(255))
    user_birthdate = Column(DateTime)
    user_phonenumber = Column(String(25))
    user_email = Column(String(255))
    user_password = Column(String(255))

    users_2fa = relationship('Users2FA', back_populates='users_auth')
    users_class = relationship('UsersClass', back_populates='users_auth')
    users_market = relationship('UsersMarket', back_populates='users_auth')
    users_ponds_address = relationship('UsersPondsAddress', back_populates='users_auth')
    users_primary_address = relationship('UsersPrimaryAddress', back_populates='users_auth')
    users_harvest_plan = relationship('UsersHarvestPlan', back_populates='users_auth')
    users_ponds = relationship('UsersPonds', back_populates='users_auth')

class Users2FA(Base):
    __tablename__ = 'users_2fa'
    user_id = Column(Integer, ForeignKey('users_auth.user_id'), primary_key=True, index=True)
    ota_code = Column(Integer)

    users_auth = relationship('UsersAuth', back_populates='users_2fa')

class UsersClass(Base):
    __tablename__ = 'users_class'
    user_id = Column(Integer, ForeignKey('users_auth.user_id'), primary_key=True, index=True)
    user_age = Column(Integer)
    user_proficiency_level = Column(String(50))
    user_pond_total = Column(String(50))
    user_pond_size_range = Column(String(255))
    user_fish_type = Column(String(255))
    user_fish_size_preference = Column(String(255))

    users_auth = relationship('UsersAuth', back_populates='users_class')

class UsersMarket(Base):
    __tablename__ = 'users_market'
    user_id = Column(Integer, ForeignKey('users_auth.user_id'), primary_key=True, index=True)
    user_production_capacity_n = Column(Integer)
    user_production_capacity_unit = Column(String(50))
    user_production_capacity_cycle = Column(String(50))
    user_market_capacity_n = Column(Integer)
    user_market_capacity_unit = Column(String(50))
    user_market_capacity_cycle = Column(String(50))
    user_market_preference = Column(String(255))

    users_auth = relationship('UsersAuth', back_populates='users_market')

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

    users_auth = relationship('UsersAuth', back_populates='users_ponds_address')
    users_primary_address = relationship('UsersPrimaryAddress', back_populates='users_ponds_address')

class UsersPrimaryAddress(Base):
    __tablename__ = 'users_primary_address'
    user_id = Column(Integer, ForeignKey('users_auth.user_id'), primary_key=True)
    pond_address_id = Column(Integer, ForeignKey('users_ponds_address.pond_address_id'))

    users_auth = relationship('UsersAuth', back_populates='users_primary_address')
    users_ponds_address = relationship('UsersPondsAddress', back_populates='users_primary_address')

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
    
    users_auth = relationship('UsersAuth', back_populates='users_harvest_plan')

class UsersPonds(Base):
    __tablename__ = 'users_ponds'

    pond_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users_auth.user_id'))
    user_ponds_pond_name = Column(String(255))
    user_ponds_fish_type = Column(String(255))
    user_ponds_start_date = Column(Date)
    user_ponds_pond_diameter = Column(Integer)
    user_ponds_pond_density = Column(String(255))
    user_ponds_target_size = Column(String(255))
    
    users_auth = relationship('UsersAuth', back_populates='users_ponds')

class CommunityCache(Base):
    __tablename__ = 'community_cache'

    community_id = Column(Integer, primary_key=True)
    community_province = Column(String(255))
    community_city = Column(String(255))
    community_month = Column(String(255))
    community_fish_type = Column(String(255))
    community_production_total = Column(Integer)
    community_user_total = Column(Integer)