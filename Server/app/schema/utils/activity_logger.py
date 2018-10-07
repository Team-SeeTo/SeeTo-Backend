from app.models.user import UserLog
from datetime import datetime


def todo_activity_logger(user: object, type: str):
    log = UserLog.objects(user=user, date=datetime.now().date()).first()

    if log is None:
        log = UserLog(user=user)
        log.save()

    if type == "new":
        log.update(inc__todo__new_create=1, inc__todo__total_point=50)
    elif type == "todo":
        log.update(inc__todo__todo_complete=1, inc__todo__total_point=70)
    elif type == "milestone":
        log.update(inc__todo__milestone_complete=1, inc__todo__total_point=10)


def idea_activity_logger(user: object, type: str):
    log = UserLog.objects(user=user, date=datetime.now().date()).first()

    if log is None:
        log = UserLog(user=user)
        log.save()

    if type == "new":
        log.update(inc__idea__new_create=1, inc__idea__total_point=50)
    elif type == "comment":
        log.update(inc__idea__new_comment=1, inc__idea__total_point=20)
    elif type == "vote":
        log.update(inc__idea__new_vote=1, inc__idea__total_point=10)