from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
goal = Table('goal', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=500)),
    Column('description', String(length=5000)),
    Column('target', Integer),
    Column('complete_by', DateTime),
    Column('created_at', DateTime),
    Column('archived_at', DateTime),
    Column('deleted_at', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['goal'].columns['complete_by'].create()
    post_meta.tables['goal'].columns['target'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['goal'].columns['complete_by'].drop()
    post_meta.tables['goal'].columns['target'].drop()
