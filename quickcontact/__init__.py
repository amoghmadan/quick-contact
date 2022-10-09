from flask import Flask

from quickcontact.views.qr import QuickResponseVCFView


def create_application():
    app = Flask(__name__)
    app.add_url_rule(
        "/", view_func=QuickResponseVCFView.as_view("qr"), methods=["GET", "POST"]
    )
    return app


application = create_application()
