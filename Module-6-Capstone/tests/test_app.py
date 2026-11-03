def test_app_starts(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_dashboard_requires_login(client):
    response = client.get("/")

    assert response.status_code == 302
    assert "/login" in response.location


def test_registration_page_loads(client):
    response = client.get("/register")

    assert response.status_code == 200
    assert b"Create your account" in response.data
    assert b"Create Account" in response.data


def test_login_page_loads(client):
    response = client.get("/login")

    assert response.status_code == 200
    assert b"Welcome back" in response.data
    assert b"Sign In" in response.data


def test_user_registration(client):
    response = client.post("/register", data={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "TestPassword123!",
        "confirm_password": "TestPassword123!"
    })

    assert response.status_code == 302
    assert "/login" in response.location


def test_successful_login(client):
    client.post("/register", data={
        "username": "loginuser",
        "email": "loginuser@example.com",
        "password": "TestPassword123!",
        "confirm_password": "TestPassword123!"
    })

    response = client.post("/login", data={
        "email": "loginuser@example.com",
        "password": "TestPassword123!"
    })

    assert response.status_code == 302
    assert response.location == "/"


def test_login_rejects_incorrect_password(client):
    client.post("/register", data={
        "username": "wrongpassuser",
        "email": "wrongpass@example.com",
        "password": "TestPassword123!",
        "confirm_password": "TestPassword123!"
    })

    response = client.post("/login", data={
        "email": "wrongpass@example.com",
        "password": "IncorrectPassword!"
    })

    assert response.status_code == 200
    assert b"Invalid email or password." in response.data


def test_authenticated_user_can_create_project(client):
    from app import db
    from app.models import Project

    client.post("/register", data={
        "username": "projectuser",
        "email": "projectuser@example.com",
        "password": "TestPassword123!",
        "confirm_password": "TestPassword123!"
    })

    client.post("/login", data={
        "email": "projectuser@example.com",
        "password": "TestPassword123!"
    })

    response = client.post("/projects/create", data={
        "name": "Automated Test Project",
        "description": "Created during automated testing."
    })

    assert response.status_code == 302

    project = db.session.execute(
        db.select(Project).filter_by(name="Automated Test Project")
    ).scalar_one_or_none()

    assert project is not None
    assert project.description == "Created during automated testing."


def test_user_can_create_task_and_update_status(client):
    from app import db
    from app.models import Project, Task

    # Register a test user
    client.post("/register", data={
        "username": "taskuser",
        "email": "taskuser@example.com",
        "password": "TestPassword123!",
        "confirm_password": "TestPassword123!"
    })

    # Log in
    client.post("/login", data={
        "email": "taskuser@example.com",
        "password": "TestPassword123!"
    })

    # Create a project
    client.post("/projects/create", data={
        "name": "Task Testing Project",
        "description": "Project for testing task management."
    })

    project = db.session.execute(
        db.select(Project).filter_by(name="Task Testing Project")
    ).scalar_one()

    # Create a task
    response = client.post(
        f"/tasks/project/{project.id}/create",
        data={
            "title": "Deploy Flask Application",
            "description": "Test task creation and status updates.",
            "due_date": ""
        }
    )

    assert response.status_code == 302

    task = db.session.execute(
        db.select(Task).filter_by(title="Deploy Flask Application")
    ).scalar_one()

    assert task.status == "To Do"

    # Update task status
    response = client.post(
        f"/tasks/{task.id}/status",
        data={"status": "In Progress"}
    )

    assert response.status_code == 302

    db.session.refresh(task)

    assert task.status == "In Progress"


def test_user_can_manage_project_lifecycle(client):
    from app import db
    from app.models import Project

    # Register and log in
    client.post("/register", data={
        "username": "lifecycleuser",
        "email": "lifecycle@example.com",
        "password": "TestPassword123!",
        "confirm_password": "TestPassword123!"
    })

    client.post("/login", data={
        "email": "lifecycle@example.com",
        "password": "TestPassword123!"
    })

    # Create a project
    client.post("/projects/create", data={
        "name": "Original Project",
        "description": "Original description."
    })

    project = db.session.execute(
        db.select(Project).filter_by(name="Original Project")
    ).scalar_one()

    # View the project list
    response = client.get("/projects/")
    assert response.status_code == 200
    assert b"Original Project" in response.data

    # View project details
    response = client.get(f"/projects/{project.id}")
    assert response.status_code == 200
    assert b"Original description." in response.data

    # Edit the project
    response = client.post(
        f"/projects/{project.id}/edit",
        data={
            "name": "Updated Project",
            "description": "Updated description."
        }
    )

    assert response.status_code == 302

    db.session.refresh(project)
    assert project.name == "Updated Project"
    assert project.description == "Updated description."

    # Delete the project
    response = client.post(f"/projects/{project.id}/delete")

    assert response.status_code == 302

    deleted_project = db.session.get(Project, project.id)
    assert deleted_project is None


def test_user_can_manage_task_lifecycle(client):
    from app import db
    from app.models import Project, Task

    # Register and log in
    client.post("/register", data={
        "username": "taskmanager",
        "email": "taskmanager@example.com",
        "password": "TestPassword123!",
        "confirm_password": "TestPassword123!"
    })

    client.post("/login", data={
        "email": "taskmanager@example.com",
        "password": "TestPassword123!"
    })

    # Create a project
    client.post("/projects/create", data={
        "name": "Task Lifecycle Project",
        "description": "Testing task management."
    })

    project = db.session.execute(
        db.select(Project).filter_by(name="Task Lifecycle Project")
    ).scalar_one()

    # Create a task
    client.post(
        f"/tasks/project/{project.id}/create",
        data={
            "title": "Original Task",
            "description": "Original task description.",
            "due_date": ""
        }
    )

    task = db.session.execute(
        db.select(Task).filter_by(title="Original Task")
    ).scalar_one()

    # View tasks
    response = client.get(f"/tasks/project/{project.id}")

    assert response.status_code == 200
    assert b"Original Task" in response.data

    # Edit the task
    response = client.post(
        f"/tasks/{task.id}/edit",
        data={
            "title": "Updated Task",
            "description": "Updated task description.",
            "due_date": ""
        }
    )

    assert response.status_code == 302

    db.session.refresh(task)

    assert task.title == "Updated Task"
    assert task.description == "Updated task description."

    # Reject an invalid task status
    response = client.post(
        f"/tasks/{task.id}/status",
        data={"status": "Invalid Status"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Invalid task status." in response.data

    db.session.refresh(task)
    assert task.status == "To Do"

    # Delete the task
    response = client.post(f"/tasks/{task.id}/delete")

    assert response.status_code == 302

    deleted_task = db.session.get(Task, task.id)

    assert deleted_task is None


def test_user_cannot_access_another_users_project(client):
    from app import db
    from app.models import Project, User
    from werkzeug.security import generate_password_hash

    # Create User A
    user_a = User(
        username="owner",
        email="owner@example.com",
        password_hash=generate_password_hash("OwnerPassword123!")
    )

    db.session.add(user_a)
    db.session.commit()

    # Create a project owned by User A
    project = Project(
        name="Private Project",
        description="This belongs to User A.",
        user_id=user_a.id
    )

    db.session.add(project)
    db.session.commit()

    project_id = project.id

    # Create User B
    user_b = User(
        username="visitor",
        email="visitor@example.com",
        password_hash=generate_password_hash("VisitorPassword123!")
    )

    db.session.add(user_b)
    db.session.commit()

    # Log in as User B
    client.post("/login", data={
        "email": "visitor@example.com",
        "password": "VisitorPassword123!"
    })

    # Attempt to access User A's project
    response = client.get(f"/projects/{project_id}")

    assert response.status_code == 404


def test_user_cannot_modify_another_users_task(client):
    from app import db
    from app.models import Project, Task, User
    from werkzeug.security import generate_password_hash

    # Create User A
    user_a = User(
        username="taskowner",
        email="taskowner@example.com",
        password_hash=generate_password_hash("OwnerPassword123!")
    )

    db.session.add(user_a)
    db.session.commit()

    # Create a project and task belonging to User A
    project = Project(
        name="Private Task Project",
        description="Owned by User A.",
        user_id=user_a.id
    )

    db.session.add(project)
    db.session.commit()

    task = Task(
        title="Private Task",
        description="This task belongs to User A.",
        status="To Do",
        project_id=project.id
    )

    db.session.add(task)
    db.session.commit()

    task_id = task.id

    # Create User B
    user_b = User(
        username="taskvisitor",
        email="taskvisitor@example.com",
        password_hash=generate_password_hash("VisitorPassword123!")
    )

    db.session.add(user_b)
    db.session.commit()

    # Log in as User B
    client.post("/login", data={
        "email": "taskvisitor@example.com",
        "password": "VisitorPassword123!"
    })

    # User B attempts to edit User A's task
    response = client.get(f"/tasks/{task_id}/edit")
    assert response.status_code == 404

    # User B attempts to update User A's task status
    response = client.post(
        f"/tasks/{task_id}/status",
        data={"status": "Completed"}
    )
    assert response.status_code == 404

    # User B attempts to delete User A's task
    response = client.post(f"/tasks/{task_id}/delete")
    assert response.status_code == 404

    # Confirm the task still exists and remains unchanged
    db.session.refresh(task)

    assert task.status == "To Do"
    assert task.title == "Private Task"
