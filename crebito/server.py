import os

from waitress import serve

from .app import create_app


def main() -> None:
    app = create_app()

    serve(
        app,
        host=os.getenv("SERVER_HOST", "0.0.0.0"),
        port=os.getenv("SERVER_PORT", 8080)
    )


if __name__ == "__main__":
    main()