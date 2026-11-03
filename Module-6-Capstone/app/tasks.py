from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models import Project, Task


# Create task management blueprint
tasks = Blueprint("tasks", __name__, url_prefix="/tasks")


# Allowed task statuses
TASK_STATUSES = ["To Do", "In Progress", "Completed"]


# Retrieve a project only if it belongs to the logged-in user
def get_user_project(project_id):
    return Project.query.filter_by(
        id=project_id,
        user_id=current_user.id
    ).first_or_404()


# Retrieve a task only if its project belongs to the logged-in user
def get_user_task(task_id):
    return Task.query.join(Project).filter(
        Task.id == task_id,
        Project.user_id == current_user.id
    ).first_or_404()


# Display tasks belonging to a project
@tasks.route("/project/<int:project_id>")
@login_required
def list_tasks(project_id):
    project = get_user_project(project_id)

    project_tasks = Task.query.filter_by(
        project_id=project.id
    ).order_by(Task.created_at.desc()).all()

    return render_template(
        "tasks.html",
        project=project,
        tasks=project_tasks
    )


# Create a task inside a project
@tasks.route("/project/<int:project_id>/create", methods=["GET", "POST"])
@login_required
def create_task(project_id):
    project = get_user_project(project_id)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        due_date_value = request.form.get("due_date", "").strip()

        if not title:
            flash("Task title is required.", "danger")
            return redirect(
                url_for("tasks.create_task", project_id=project.id)
            )

        due_date = None

        if due_date_value:
            try:
                due_date = datetime.strptime(
                    due_date_value, "%Y-%m-%d"
                ).date()
            except ValueError:
                flash("Please enter a valid due date.", "danger")
                return redirect(
                    url_for("tasks.create_task", project_id=project.id)
                )

        new_task = Task(
            title=title,
            description=description,
            status="To Do",
            due_date=due_date,
            project_id=project.id
        )

        db.session.add(new_task)
        db.session.commit()

        flash("Task created successfully.", "success")
        return redirect(
            url_for("tasks.list_tasks", project_id=project.id)
        )

    return render_template(
        "create_task.html",
        project=project
    )


# Edit an existing task
@tasks.route("/<int:task_id>/edit", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    task = get_user_task(task_id)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        due_date_value = request.form.get("due_date", "").strip()

        if not title:
            flash("Task title is required.", "danger")
            return redirect(
                url_for("tasks.edit_task", task_id=task.id)
            )

        due_date = None

        if due_date_value:
            try:
                due_date = datetime.strptime(
                    due_date_value, "%Y-%m-%d"
                ).date()
            except ValueError:
                flash("Please enter a valid due date.", "danger")
                return redirect(
                    url_for("tasks.edit_task", task_id=task.id)
                )

        task.title = title
        task.description = description
        task.due_date = due_date

        db.session.commit()

        flash("Task updated successfully.", "success")
        return redirect(
            url_for("tasks.list_tasks", project_id=task.project_id)
        )

    return render_template(
        "edit_task.html",
        task=task
    )


# Update task status
@tasks.route("/<int:task_id>/status", methods=["POST"])
@login_required
def update_status(task_id):
    task = get_user_task(task_id)
    new_status = request.form.get("status", "")

    if new_status not in TASK_STATUSES:
        flash("Invalid task status.", "danger")
        return redirect(
            url_for("tasks.list_tasks", project_id=task.project_id)
        )

    task.status = new_status
    db.session.commit()

    flash("Task status updated successfully.", "success")
    return redirect(
        url_for("tasks.list_tasks", project_id=task.project_id)
    )


# Delete an existing task
@tasks.route("/<int:task_id>/delete", methods=["POST"])
@login_required
def delete_task(task_id):
    task = get_user_task(task_id)
    project_id = task.project_id

    db.session.delete(task)
    db.session.commit()

    flash("Task deleted successfully.", "success")
    return redirect(
        url_for("tasks.list_tasks", project_id=project_id)
    )
