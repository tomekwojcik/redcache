# -*- coding: utf-8 -*-
"""Example of using CacheManager to store and retrieve SQLAlchemy objects.

Requires SQLAlchemy>=0.7.9"""

from datetime import datetime
import logging
import random
import os
import time
import uuid

from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from redcache import CacheManager, use_connection

Base = declarative_base()


class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer(), primary_key=True)
    uuid = Column(String(36))
    created_at = Column(DateTime())

    def __repr__(self):
        return '<Record("%d", "%s", "%s")>' % (
            self.id, self.uuid, self.created_at.isoformat()
        )


class DBCacheManager(CacheManager):
    def after_load(self, data, f_args=None, f_kwargs=None):
        obj = super(DBCacheManager, self).after_load(data, f_args=f_args,
                                                     f_kwargs=f_kwargs)

        if f_kwargs and 'session' in f_kwargs:
            session = f_kwargs.get('session')
            session.merge(obj, load=False)

        return obj


def main():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.db')
    engine = create_engine('sqlite:///' + db_path, echo=False)
    Session = sessionmaker(bind=engine)

    use_connection()

    logging.info('Nuking and creating the table.')
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    logging.info('Filling the table with 5000 records.')
    session = Session()
    for i in xrange(1, 5001):
        if i % 500 == 0:
            logging.info('%d records created' % i)

        record = Record(uuid=str(uuid.uuid4()), created_at=datetime.now())
        session.add(record)

    session.commit()
    session.close()

    cache_manager = DBCacheManager(key_base=u'sql_ex', ttl=5)

    @cache_manager.cache
    def get_record_by_id(id_, session=session):
        return session.query(Record).filter_by(id=id_).first()

    def load(ids):
        session = Session()
        for id_ in ids:
            logging.debug('Loading record with ID = %d' % id_)
            loaded = get_record_by_id(id_, session=session)
            logging.debug('Loaded record = %s' % loaded)

        session.close()

    sample = random.sample(xrange(1, 5001), 1000)

    logging.info('Loading %d records...' % len(sample))
    start_time = time.time()
    load(sample)
    end_time = time.time()
    logging.info('Elapsed time: %.5f seconds' % (end_time - start_time, ))

    logging.info('Loading the same records again...')
    start_time = time.time()
    load(sample)
    end_time = time.time()
    logging.info('Elapsed time: %.5f seconds' % (end_time - start_time, ))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
