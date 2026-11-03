from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os


# Initialise SQLAlchemy
db = SQLAlchemy()

# Initialise Flask-Login
login_manager = LoginManager()

# Initialise CSRF protection
csrf = CSRFProtect()


def create_app(test_config=None):
    # Load environment variables
    load_dotenv()

    app = Flask(__name__)

    # Apply test configuration before checking the secret key
    if test_config is not None:
        app.config.update(test_config)

    # Application security configuration
    secret_key = app.config.get("SECRET_KEY") or os.getenv("SECRET_KEY")

    if not secret_key:
        raise RuntimeError("SECRET_KEY is missing. Configure it in the environment.")

    app.config["SECRET_KEY"] = secret_key

    # Build the PostgreSQL connection URL
    database_url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.getenv("POSTGRES_DB")
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url.render_as_string(
        hide_password=False
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Allow automated tests to override the default configuration
    if test_config is not None:
        app.config.update(test_config)

    # Initialise database
    db.init_app(app)

    # Initialise Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Initialise CSRF protection
    csrf.init_app(app)

    # Load authenticated users
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User

        try:
            return db.session.get(User, int(user_id))
        except (ValueError, TypeError):
            return None

    # Register authentication routes
    from app.auth import auth
    app.register_blueprint(auth)

    # Register project management routes
    from app.projects import projects
    app.register_blueprint(projects)

    # Register task management routes
    from app.tasks import tasks
    app.register_blueprint(tasks)

    # Main dashboard - authentication required
    @app.route("/")
    @login_required
    def home():
        from app.models import Project, Task

        # Count projects belonging to the logged-in user
        total_projects = Project.query.filter_by(
            user_id=current_user.id
        ).count()

        # Base query for tasks belonging to the user's projects
        user_tasks = Task.query.join(Project).filter(
            Project.user_id == current_user.id
        )

        # Calculate total task count
        total_tasks = user_tasks.count()

        # Calculate each task status independently
        todo_tasks = user_tasks.filter(
            Task.status == "To Do"
        ).count()

        in_progress_tasks = user_tasks.filter(
            Task.status == "In Progress"
        ).count()

        completed_tasks = user_tasks.filter(
            Task.status == "Completed"
        ).count()

        # Retrieve the five most recent projects
        recent_projects = Project.query.filter_by(
            user_id=current_user.id
        ).order_by(
            Project.created_at.desc()
        ).limit(5).all()

        return render_template(
            "index.html",
            total_projects=total_projects,
            total_tasks=total_tasks,
            todo_tasks=todo_tasks,
            in_progress_tasks=in_progress_tasks,
            completed_tasks=completed_tasks,
            recent_projects=recent_projects
        )

    # Application health check
    @app.route("/health")
    def health():
        return {
            "status": "healthy"
        }, 200

    return app
