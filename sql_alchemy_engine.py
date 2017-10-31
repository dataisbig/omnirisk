from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Base
from socket import gethostname

# checks the current host system and returns a properly configured sqlalchemy session
host_name = gethostname()
if host_name == 'lxpollara3':
    # configuration for alex's laptop
    engine = create_engine('mysql+pymysql://alex:tygrcnt@127.0.0.1/adas')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()


elif host_name == 'instance-1':
    # configuration for VM
    engine = create_engine ('mysql+pymysql://alex:tygrcnt@104.197.42.10/adas')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession ()

else:
    raise ValueError('No connection configuration for current host system')

