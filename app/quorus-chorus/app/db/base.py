# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa: F401
from app.models.payout import Payout  # noqa: F401
from app.models.song import Song  # noqa: F401
from app.models.user import User  # noqa: F401
