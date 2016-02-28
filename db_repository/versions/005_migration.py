from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
task = Table('task', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=500)),
    Column('repeats', VARCHAR(length=32)),
    Column('timeframe', VARCHAR(length=32)),
    Column('last_completed', DATETIME),
    Column('created_at', DATETIME),
    Column('archived_at', DATETIME),
    Column('deleted_at', DATETIME),
)

task = Table('task', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=500)),
    Column('repeat_interval', Integer),
    Column('repeat_unit', String(length=32)),
    Column('last_completed', DateTime),
    Column('created_at', DateTime),
    Column('archived_at', DateTime),
    Column('deleted_at', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['task'].columns['repeats'].drop()
    pre_meta.tables['task'].columns['timeframe'].drop()
    post_meta.tables['task'].columns['repeat_interval'].create()
    post_meta.tables['task'].columns['repeat_unit'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['task'].columns['repeats'].create()
    pre_meta.tables['task'].columns['timeframe'].create()
    post_meta.tables['task'].columns['repeat_interval'].drop()
    post_meta.tables['task'].columns['repeat_unit'].drop()
