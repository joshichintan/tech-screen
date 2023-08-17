from typing import Dict

import pytest
from app.core.config import settings
from fastapi.testclient import TestClient


@pytest.mark.skip
def test_celery_worker_test(
    client: TestClient, superuser_token_headers: Dict[str, str]
) -> None:
    data = {"msg": "test"}
    r = client.post(
        f"{settings.API_V1_STR}/utils/test-celery/",
        json=data,
        headers=superuser_token_headers,
    )
    response = r.json()
    assert response["msg"] == "Word received"
