# coding: utf-8
from app.database.database import Base
from sqlalchemy import CheckConstraint, Column, Float, Integer, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2.types import Geometry

metadata = Base.metadata


class Diadiem(Base):
    __tablename__ = 'diadiem'

    id = Column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    trangthai = Column(String(40))
    diachi = Column(String(255))
    tenxa = Column(String(255))
    tenhuyen = Column(String(255))
    tentinh = Column(String(255))
    matinh = Column(String(10))
    mahuyen = Column(String(10))
    maxa = Column(String(10))
    thongtinlienhe = Column(Text)
    sodienthoai = Column(String(40))
    thoigianhoatdong = Column(String(40))
    giaohangtructuyen = Column(Text)
    status = Column(SmallInteger, server_default=text("1"))
    geom = Column(Geometry(from_text='ST_GeomFromEWKT', name='geometry'))
    lat = Column(Float(53))
    lng = Column(Float(53))
    ten = Column(String(255))


class Fastmodel(Base):
    __tablename__ = 'fastmodel'

    id = Column(Integer, primary_key=True, server_default=text("nextval('fastmodel_id_seq'::regclass)"))
    name = Column(String)


t_geography_columns = Table(
    'geography_columns', metadata,
    Column('f_table_catalog', String),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geography_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', Text)
)


t_geometry_columns = Table(
    'geometry_columns', metadata,
    Column('f_table_catalog', String(256)),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geometry_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', String(30))
)


class SpatialRefSy(Base):
    __tablename__ = 'spatial_ref_sys'
    __table_args__ = (
        CheckConstraint('(srid > 0) AND (srid <= 998999)'),
    )

    srid = Column(Integer, primary_key=True)
    auth_name = Column(String(256))
    auth_srid = Column(Integer)
    srtext = Column(String(2048))
    proj4text = Column(String(2048))
