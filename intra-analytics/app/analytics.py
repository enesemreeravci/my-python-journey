from typing import Any


def find_main_cursus(
    cursus_users: list[dict[str, Any]],
) -> dict[str, Any] | None:
    """
    Try to find the main 42 cursus.

    We prefer a cursus named '42cursus'. If it is not present,
    we use the latest active cursus.
    """
    for cursus_user in cursus_users:
        cursus = cursus_user.get("cursus", {})

        if cursus.get("slug") == "42cursus":
            return cursus_user

    active_cursus = [
        cursus
        for cursus in cursus_users
        if cursus.get("end_at") is None
    ]

    if active_cursus:
        return active_cursus[-1]

    if cursus_users:
        return cursus_users[-1]

    return None


def summarize_projects(
    projects_users: list[dict[str, Any]],
) -> dict[str, Any]:
    completed: list[dict[str, Any]] = []
    failed: list[dict[str, Any]] = []
    in_progress: list[dict[str, Any]] = []

    for project_user in projects_users:
        project = project_user.get("project", {})

        clean_project = {
            "id": project.get("id"),
            "name": project.get("name", "Unknown project"),
            "slug": project.get("slug"),
            "status": project_user.get("status"),
            "final_mark": project_user.get("final_mark"),
            "validated": project_user.get("validated?"),
            "updated_at": project_user.get("updated_at"),
        }

        if project_user.get("validated?") is True:
            completed.append(clean_project)
        elif project_user.get("status") == "finished":
            failed.append(clean_project)
        else:
            in_progress.append(clean_project)

    marks = [
        project["final_mark"]
        for project in completed
        if isinstance(project["final_mark"], int)
    ]

    average_mark = round(sum(marks) / len(marks), 2) if marks else 0

    return {
        "completed": completed,
        "failed": failed,
        "in_progress": in_progress,
        "completed_count": len(completed),
        "failed_count": len(failed),
        "in_progress_count": len(in_progress),
        "average_mark": average_mark,
    }


def extract_skills(
    cursus_user: dict[str, Any] | None,
) -> list[dict[str, Any]]:
    if cursus_user is None:
        return []

    skills = cursus_user.get("skills", [])

    cleaned_skills = [
        {
            "name": skill.get("name", "Unknown"),
            "level": round(float(skill.get("level", 0)), 2),
        }
        for skill in skills
    ]

    return sorted(
        cleaned_skills,
        key=lambda skill: skill["level"],
        reverse=True,
    )


def calculate_success_rate(
    completed_count: int,
    failed_count: int,
) -> float:
    finished_count = completed_count + failed_count

    if finished_count == 0:
        return 0.0

    return round(completed_count / finished_count * 100, 2)


def build_user_summary(user: dict[str, Any]) -> dict[str, Any]:
    main_cursus = find_main_cursus(user.get("cursus_users", []))
    project_summary = summarize_projects(user.get("projects_users", []))

    success_rate = calculate_success_rate(
        project_summary["completed_count"],
        project_summary["failed_count"],
    )

    image = user.get("image") or {}

    return {
        "id": user.get("id"),
        "login": user.get("login"),
        "display_name": user.get("displayname"),
        "email": user.get("email"),
        "image": image.get("link"),
        "wallet": user.get("wallet", 0),
        "correction_points": user.get("correction_point", 0),
        "location": user.get("location"),
        "active": user.get("active?", False),
        "level": (
            round(float(main_cursus.get("level", 0)), 2)
            if main_cursus
            else 0
        ),
        "cursus": (
            main_cursus.get("cursus", {}).get("name")
            if main_cursus
            else None
        ),
        "skills": extract_skills(main_cursus),
        "projects": project_summary,
        "success_rate": success_rate,
    }