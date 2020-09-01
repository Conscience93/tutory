from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
## API Routes ##
from tutory_api.blueprints.users.views import users_api_blueprint
from tutory_api.blueprints.sessions.views import sessions_api_blueprint
from tutory_api.blueprints.dashboard.views import dashboard_api_blueprint
from tutory_api.blueprints.grade.views import grade_api_blueprint


app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(sessions_api_blueprint, url_prefix='/api/v1/sessions')
app.register_blueprint(dashboard_api_blueprint, url_prefix='/api/v1/dashboard')
app.register_blueprint(grade_api_blueprint, url_prefix='/api/v1/grade')