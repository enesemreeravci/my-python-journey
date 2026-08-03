from flask import Blueprint, current_app, jsonify, request

from app.analytics import build_user_summary
from app.api_client import FortyTwoAPIError, FortyTwoClient


main = Blueprint("main", __name__)


def create_api_client() -> FortyTwoClient:
    return FortyTwoClient(
        client_id=current_app.config["FT_CLIENT_ID"],
        client_secret=current_app.config["FT_CLIENT_SECRET"],
    )


@main.get("/")
def index():
    return jsonify(
        {
            "application": "ft_dashboard",
            "message": "42 API dashboard is running",
            "usage": "/api/users/<login>",
        }
    )


@main.get("/api/users/<string:login>")
def user_profile(login: str):
    try:
        client = create_api_client()
        raw_user = client.get_user(login)
        summary = build_user_summary(raw_user)

        return jsonify(summary), 200

    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    except FortyTwoAPIError as error:
        return jsonify({"error": str(error)}), 502


@main.get("/api/search")
def search_user():
    login = request.args.get("login", "").strip()

    if not login:
        return jsonify(
            {"error": "The login query parameter is required"}
        ), 400

    try:
        client = create_api_client()
        raw_user = client.get_user(login)

        return jsonify(build_user_summary(raw_user)), 200

    except FortyTwoAPIError as error:
        return jsonify({"error": str(error)}), 502