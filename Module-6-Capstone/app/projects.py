from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models import Project


# Create projects blueprint
projects = Blueprint("projects", __name__, url_prefix="/projects")


# Retrieve a project only if it belongs to the logged-in user
def get_user_project(project_id):
    return Project.query.filter_by(
        id=project_id,
        user_id=current_user.id
    ).first_or_404()


# Display projects belonging to the logged-in user
@projects.route("/")
@login_required
def list_projects():
    user_projects = Project.query.filter_by(
        user_id=current_user.id
    ).order_by(Project.created_at.desc()).all()

    return render_template(
        "projects.html",
        projects=user_projects
    )


# Create a new project
@projects.route("/create", methods=["GET", "POST"])
@login_required
def create_project():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()

        if not name:
            flash("Project name is required.", "danger")
            return redirect(url_for("projects.create_project"))

        new_project = Project(
            name=name,
            description=description,
            user_id=current_user.id
        )

        db.session.add(new_project)
        db.session.commit()

        flash("Project created successfully.", "success")
        return redirect(url_for("projects.list_projects"))

    return render_template("create_project.html")


# View an individual project
@projects.route("/<int:project_id>")
@login_required
def view_project(project_id):
    project = get_user_project(project_id)

    return render_template(
        "project_detail.html",
        project=project
    )


# Edit an existing project
@projects.route("/<int:project_id>/edit", methods=["GET", "POST"])
@login_required
def edit_project(project_id):
    project = get_user_project(project_id)

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()

        if not name:
            flash("Project name is required.", "danger")
            return redirect(
                url_for("projects.edit_project", project_id=project.id)
            )

        project.name = name
        project.description = description

        db.session.commit()

        flash("Project updated successfully.", "success")
        return redirect(
            url_for("projects.view_project", project_id=project.id)
        )

    return render_template(
        "edit_project.html",
        project=project
    )


# Delete an existing project
@projects.route("/<int:project_id>/delete", methods=["POST"])
@login_required
def delete_project(project_id):
    project = get_user_project(project_id)

    db.session.delete(project)
    db.session.commit()

    flash("Project and its associated tasks deleted successfully.", "success")
    return redirect(url_for("projects.list_projects"))
