#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import UniqueConstraint
from config import *

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://www.phpgao.com
@software: PyCharm
@file: database.py
@time: 16/2/26 上午9:24
"""


engine = create_engine(global_dbcoon)
DBSession = sessionmaker(bind=engine)
Base = declarative_base()


class Reports(Base):
    """
        Embeded class for ORM map NmapReport to a
        simple three column table
    """
    __tablename__ = 'result_ports'

    id = Column('id', Integer, primary_key=True)
    taskid = Column('taskid', String(256))
    inserted = Column('inserted', DateTime(), default='now')
    address = Column('address', String(256))
    port = Column('port', Integer)
    service = Column('service', String(256))
    state = Column('state', String(12))
    protocol = Column('protocol', String(12))
    product = Column('product', String(64))
    product_version = Column('product_version', String(64))
    product_extrainfo = Column('product_extrainfo', String(128))
    # banner = Column('banner', String(256))
    scripts_results = Column('scripts_results', Text)
    scanned = Column('scanned', String(256))



class Resultip(Base):
    """
        Embeded class for ORM map NmapReport to a
        simple three column table
    """
    __tablename__ = 'result_ip'

    id = Column('id', Integer, primary_key=True)
    taskid = Column('taskid', String(256))
    inserted = Column('inserted', DateTime(), default='now')
    domain = Column('domain', String(256))
    address = Column('address', String(32))
    is_up = Column('is_up', Boolean)
    os = Column('os', String(256))
    scanned = Column('scanned', String(256))


class Subdomains(Base):
    """
        Embeded class for ORM map NmapReport to a
        simple three column table
    """
    __tablename__ = 'subdomains'

    id = Column('id', Integer, primary_key=True)
    ip = Column('ip', String(256))
    subdomain = Column('subdomain', String(255), unique=True)
    findby = Column('findby', String(256))
    ownedby = Column('ownedby', String(256))
    scaned = Column('scaned', String(256))
    vuls = Column('vuls', String(256))
    inserted = Column('inserted', DateTime(), default='now')


class Fmiddleware(Base):
    """
        Embeded class for ORM map NmapReport to a
        simple three column table
    """
    __tablename__ = 'middleware'

    id = Column('id', Integer, primary_key=True)
    ip = Column('ip', String(256))
    port = Column('port', String(256))
    taskid = Column('taskid', String(256))
    vul = Column('vuls', Text(5000))
    inserted = Column('inserted', DateTime(), default='now')



# class Ipblocks(Base):
#     """
#         Embeded class for ORM map NmapReport to a
#         simple three column table
#     """
#     __tablename__ = 'ipblocks'
#
#     id = Column('id', Integer, primary_key=True)
#     ownedby = Column('ownedby', String(256))
#     ipblock = Column('scaned', String(256))


class Whatweb(Base):
    """
        whatweb result table
    """
    __tablename__ = 'whatweb'

    id = Column('id', Integer, primary_key=True)
    taskid = Column('taskid', String(256))
    target = Column('target', String(256))
    http_status = Column('http_status', Integer)
    title = Column('title', String(2560))
    cms = Column('cms', String(256))
    http_server = Column('http_server', String(256))
    address = Column('address', String(256))
    plugins = Column('plugins', Text)
    inserted = Column('inserted', DateTime(), default='now')
    scanned = Column('scanned', String(256))



class BBscan(Base):
    """
        whatweb result table
    """
    __tablename__ = 'bbscan'

    id = Column('id', Integer, primary_key=True)
    taskid = Column('taskid', String(256))
    host = Column('host', String(256))
    http_status = Column('http_status', Integer)
    weakfile = Column('weakfile', Text(25600))
    inserted = Column('inserted', DateTime(), default='now')

    # protocol = Column('protocol', String(12))
    # product = Column('product', String(64))
    # product_version = Column('product_version', String(64))
    # product_extrainfo = Column('product_extrainfo', String(128))
    # # banner = Column('banner', String(256))
    # scripts_results = Column('scripts_results', Text)


class Domains(Base):
    # 表的名字:
    __tablename__ = 'domains'
    # 表的结构:
    id = Column(Integer(), primary_key=True)
    # scheme = Column(String(20))
    subdomain = Column(String(255))
    findby = Column(String(255))
    ownedby = Column(String(255))
    # cookies = Column(Text(20000))
    scaned = Column(String(255))
    # query = Column(Text(20000))
    vuls = Column(String(255))

class Ipblocks(Base):
    # 表的名字:
    __tablename__ = 'ipblocks'
    # 表的结构:
    id = Column(Integer(), primary_key=True)
    # scheme = Column(String(20))
    ipblock = Column(String(255),unique=True)
    findby = Column(String(255))
    ownedby = Column(String(255))
    # cookies = Column(Text(20000))
    scaned = Column(String(255))
    # query = Column(Text(20000))
    # vuls = Column(String(255))
    inserted = Column('inserted', DateTime(), default='now')



class Requests(Base):
    # 表的名字:
    __tablename__ = 'requests'
    # 表的结构:
    id = Column(String(200), primary_key=True)
    # urlhash = Column(String(200),)
    # scheme = Column(String(20))
    method = Column(String(200))
    url = Column(String(2000))
    headers = Column(Text(20000))
    # cookies = Column(Text(20000))
    content = Column(Text(20000))
    # query = Column(Text(20000))
    timestamp_start = Column(String(2000))
    urlencoded_form=Column(Text(20000))
    multipart_form=Column(Text(20000))
    sqlmap=Column(String(2000))
    xss=Column(String(2000))
    scanned = Column(String(200))


class Resultsall(Base):
    # 表的名字:
    __tablename__ = 'resultsall'
    # 表的结构:
    id = Column(Integer(), primary_key=True)
    vul = Column(String(2000))
    url = Column(String(2000))
    # scheme = Column(String(20))
    method = Column(String(200))
    headers = Column(Text(20000))
    # cookies = Column(Text(20000))
    content = Column(Text(200000))
    # query = Column(Text(20000))
    urlencoded_form=Column(Text(200000))
    multipart_form=Column(Text(200000))
    response = Column(Text(200000))
    scanner=Column(String(2000))
    inserted = Column('inserted', DateTime(), default='now')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
