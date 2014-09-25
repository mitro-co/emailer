import sqlalchemy
import sqlalchemy.exc
import sqlalchemy.ext.declarative
import sqlalchemy.orm
from sqlalchemy.pool import NullPool
from .email_queue_model import EmailQueueModel

_session = None


def get_session(config):
    global _session

    if _session is not None:
        return _session

    url = _create_connection_url(config)
    engine = sqlalchemy.create_engine(url, poolclass=sqlalchemy.pool.NullPool, echo=False)
    _session = sqlalchemy.orm.sessionmaker()
    _session.configure(bind=engine)
    _session = _session()

    return _session


def close_connection():
    global _session

    if _session is not None:
        _session.close()


def _create_connection_url(config):
    hostname = config.get('hostname')
    port = config.get('port', '5432')
    username = config.get('username')
    password = config.get('password')
    database = config.get('database', 'mitro')

    conn = 'postgres://'

    if username:
        conn += username

    if password and username:
        conn += ':' + password

    if password or username:
        conn += '@'

    if hostname:
        conn += hostname

    if port and hostname:
        conn += ':' + port

    conn += '/' + database

    return conn