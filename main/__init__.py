from flask import Flask

def init_app():
    app = Flask(__name__,
                instance_relative_config=False,
                static_url_path='/main/static')
    app.config.from_object('config.Config')

    with app.app_context():
        from .view import \
            routes_si, plotly_view, data_view

        # from plotlydash.dashboard import init_dashboard
        # app = init_dashboard(app)

        return app

