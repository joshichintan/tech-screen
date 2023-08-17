# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.payout import Payout
from app.models.song import Song
from app.models.user import User  # noqa
