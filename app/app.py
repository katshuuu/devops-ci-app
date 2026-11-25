"""Учебное приложение Flask для демонстрации CI."""

from flask import Flask, jsonify


def health():
    """Проверка работоспособности службы."""
    return jsonify(status="ok")


def index():
    """Сведения о службе."""
    return jsonify(service="devops-ci-app", version="1.1.0-shustalova", status="running")


def create_app():
    """Создать и настроить приложение Flask."""
    application = Flask(__name__)
    application.add_url_rule("/health", "health", health)
    application.add_url_rule("/", "index", index)
    return application


app = create_app()  # pylint: disable=invalid-name
