"""Модульные тесты приложения."""

import pytest

from app import create_app


@pytest.fixture(name="client")
def client_fixture():
    """Тестовый клиент Flask."""
    application = create_app()
    application.config.update(TESTING=True)
    return application.test_client()


def test_health(client):
    """Маршрут /health возвращает status=ok."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_index(client):
    """Маршрут / возвращает сведения о службе."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {
        "service": "devops-ci-app",
        "version": "1.0.0",
        "status": "running",
    }
