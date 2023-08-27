import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm


# create url for database.py with our docker postgres db setup
DATABASE_URL = "postgresql://dataholic:mypass@localhost:4521/fastapi_database"

# connect to database
engine = _sql.create_engine(DATABASE_URL)

# create a session to enable interaction with database.py
SessionLocal = _orm.sessionmaker(autocommit= False, autoflush= False, bind=engine)

# initializing SQLAlchemy database built in Model.
Base = _declarative.declarative_base()