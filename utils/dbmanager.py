from user.models import *
from application.models import *
from deployment.models import *
from django.core.paginator import Paginator
from ReleaseManagement.config import *
from django.utils import timezone as datetime

# Method for User models


def find_users_by_pagination():
    user_list = find_all_users()
    item_page = Paginator(user_list, DEFAULT_ITEM_PER_PAGE)
    return item_page


def find_all_users():
    all_users = User.objects.all().order_by("id")
    return all_users


def find_user_by_id(user_id):
    return User.objects.get(pk=user_id)


def find_user_by_username(username):
    user_list = User.objects.filter(user_name=username).order_by("id")
    if len(user_list) == 0:
        return None
    else:
        return user_list[0]


def find_user_by_realname(realname):
    user_list = User.objects.filter(real_name=realname).order_by("id")
    return user_list


def save_user(realname, username, password, email):
    # create new user
    new_user = User()
    new_user.user_name = username
    new_user.real_name = realname
    new_user.password = password
    new_user.email = email
    new_user.created_at = datetime.now()
    new_user.updated_at = datetime.now()
    # save new user into db.
    try:
        new_user.save()
    except Exception as e:
        print(e)
        return None

    return new_user.id


def update_user(user_id, realname, username, password, email):

    update_user = find_user_by_id(user_id)
    update_user.real_name = realname
    update_user.user_name = username
    update_user.password = password
    update_user.email = email
    update_user.updated_at = datetime.now()
    try:
        update_user.save()
    except Exception as e:
        print(e)
        return False

    return True


def delete_user_by_id(user_id):
    delete_user = find_user_by_id(user_id)
    try:
        delete_user.delete()
    except Exception as e:
        print(e)
        return False

    return True


# Method for Role models


def find_all_roles():
    return Role.objects.all().order_by("id")


def find_role_by_id(role_id):
    return Role.objects.get(PK=role_id)


def find_role_by_name(role_name):
    return Role.objects.filter(role_name=role_name).order_by("id")


def save_role(role_name, comment="None"):
    # create new role
    new_role = Role()
    new_role.role_name = role_name
    new_role.comment = comment
    try:
        new_role.save()
    except Exception as e:
        print(e)
        return None

    return new_role.id


def update_role(role_id, role_name, comment):
    # update role
    update_role = find_role_by_id(role_id)
    update_role.role_name = role_name
    update_role.comment = comment
    try:
        update_role.save()
    except Exception as e:
        print(e)
        return False

    return True


def delete_role_by_id(role_id):
    delete_role = find_role_by_id(role_id)
    try:
        delete_role.delete()
    except Exception as e:
        print(e)
        return False

    return True


# Methods of  UserRoleMapping


def find_role_by_user(user_id):
    return UserRoleMapping.objects.filter(user_id=user_id).order_by("id")


def find_role_by_user_pagination(user_id):
    return Paginator(find_role_by_user(user_id), DEFAULT_ITEM_PER_PAGE)


def find_user_by_role(role_id):
    return UserRoleMapping.objects.filter(role_id=role_id).order_by("id")


def find_user_by_role_pagination(role_id):
    return Paginator(find_user_by_role(role_id), DEFAULT_ITEM_PER_PAGE)


def find_user_role_mapping_by_id(mapping_id):
    return UserRoleMapping.objects.get(pk=mapping_id)


def save_user_role_mapping(user_id, role_id):
    # create new user -> role mapping
    u_r_mapping = UserRoleMapping()
    u_r_mapping.user_id = user_id
    u_r_mapping.role_id = role_id
    try:
        u_r_mapping.save()
    except Exception as e:
        print(e)
        return None

    return u_r_mapping.id


def update_user_role_mapping(mapping_id, user_id, role_id):
    update_u_r_mapping = find_user_role_mapping_by_id(mapping_id)
    update_u_r_mapping.user_id = user_id
    update_u_r_mapping.role_id = role_id
    try:
        update_u_r_mapping.save()
    except Exception as e:
        print(e)
        return False

    return True


def delete_user_role_mapping(mapping_id):
    delete_u_r_mapping = find_user_role_mapping_by_id(mapping_id)
    try:
        delete_u_r_mapping.delete()
    except Exception as e:
        print(e)
        return False

    return True

# Methods of Application models


def find_all_applications():
    return Application.objects.all().order_by("id")


def find_all_applications_pagination():
    return Paginator(find_all_applications(), DEFAULT_ITEM_PER_PAGE)


def find_application_by_id(app_id):
    return Application.objects.get(pk=app_id)


def find_application_by_name(app_name):
    return Application.objects.filter(name=app_name).order_by("id")


def save_application(app_name, comment="None"):
    # create new application
    new_app = Application()
    new_app.name = app_name
    new_app.comment = comment
    new_app.created_at = datetime.now()
    # try to save
    try:
        new_app.save()
    except Exception as e:
        print(e)
        return None

    return new_app.id


def update_application(app_id, app_name, comment):
    update_app = find_application_by_id(app_id)
    update_app.name = app_name
    update_app.comment = comment
    # try to update
    try:
        update_app.save()
    except Exception as e:
        print(e)
        return False

    return True


def delete_application(app_id):
    delete_app = find_application_by_id(app_id)
    # try to delete
    try:
        delete_app.delete()
    except Exception as e:
        print(e)
        return False

    return True

# Method of ApplicationPort model


def find_application_by_port(app_port):
    return ApplicationPort.objects.filter(port=app_port).order_by("id")


def find_port_by_application(app_id):
    return ApplicationPort.objects.filter(app_id=app_id).order_by("id")


def find_application_port_by_id(mapping_id):
    return ApplicationPort.objects.get(pk=mapping_id)


def save_application_port_mapping(app_id, port, comment="None"):
    # create new application -> port mapping
    a_p_mapping = ApplicationPort()
    a_p_mapping.app_id = app_id
    a_p_mapping.port = port
    a_p_mapping.comment = comment
    # try to save
    try:
        a_p_mapping.save()
    except Exception as e:
        print(e)
        return None

    return a_p_mapping.id


def update_application_port_mapping(mapping_id, app_id, port, comment):
    update_a_p_mapping = find_application_port_by_id(mapping_id)
    update_a_p_mapping.app_id = app_id
    update_a_p_mapping.port = port
    update_a_p_mapping.comment = comment
    # try to update
    try:
        update_a_p_mapping.save()
    except Exception as e:
        print(e)
        return False

    return True


def delete_application_port_mapping(mapping_id):
    delete_a_p_mapping = find_application_port_by_id(mapping_id)
    # try to delete
    try:
        delete_a_p_mapping.delete()
    except Exception as e:
        print(e)
        return False

    return True


# Method of ApplicationFeatures


def find_application_feature_by_app_pagination(app_id):
    return Paginator(ApplicationFeatures.objects.filter(app_id=app_id).order_by("id"), DEFAULT_ITEM_PER_PAGE)


def find_application_feature_by_feature(f_id):
    return Paginator(ApplicationFeatures.objects.filter(feature_id=f_id).order_by("id"), DEFAULT_ITEM_PER_PAGE)


def find_application_feature_by_id(af_id):
    return ApplicationFeatures.objects.get(pk=af_id)


def save_application_feature(app_id, f_id, comment="None"):
    # create new object
    new_af = ApplicationFeatures()
    new_af.app_id = app_id
    new_af.feature_id = f_id
    new_af.comment = comment
    # try to save
    try:
        new_af.save()
    except Exception as e:
        print(e)
        return None

    return new_af.id


def update_application_feature(af_id, app_id, f_id, comment):
    # get existed item
    update_af = find_application_feature_by_id(af_id)
    update_af.app_id = app_id
    update_af.feature_id = f_id
    update_af.comment = comment
    # try to update
    try:
        update_af.save()
    except Exception as e:
        print(e)
        return False

    return True


def delete_application_feature(af_id):
    # get existed item
    delete_af = find_application_feature_by_id(af_id)
    # try to delete
    try:
        delete_af.delete()
    except Exception as e:
        print(e)
        return False

    return True


# Method of Task


def find_all_task():
    return Task.objects.all().order_by("id")


def find_all_task_pagination():
    return Paginator(Task.objects.all().order_by("id"), DEFAULT_ITEM_PER_PAGE)


def find_task_by_id(task_kd):
    return Task.objects.get(pk=task_kd)


def find_task_by_method(method):
    return Task.objects.filter(task_method=method).order_by("id")


def find_task_by_date(create_date):
    return Task.objects.filter(created_at=create_date).order_by("id")


def find_task_by_name(task_name):
    return Task.objects.filter(name=task_name).order_by("id")


def save_task(name, method, comment="None"):
    # Create a task
    new_task = Task()
    new_task.name = name
    new_task.comment = comment
    new_task.task_method = method
    new_task.created_at = datetime.now()
    # try to save
    try:
        new_task.save()
    except Exception as e:
        print(e)
        return None

    return new_task.id


def update_task(task_id, name, method, comment):
    update_task = find_task_by_id(task_id)
    update_task.name = name
    update_task.task_method = method
    update_task.comment = comment
    # try to update
    try:
        update_task.save()
    except Exception as e:
        print(e)
        return False

    return True


def delete_task(task_id):
    delete_task = find_task_by_id(task_id)
    # try to delete
    try:
        delete_task.delete()
    except Exception as e:
        print(e)
        return False

    return True

# Method of TaskAnsible


def find_task_ansible_by_id(ta_id):
    return TaskAnsible.objects.get(pk=ta_id)


def find_task_ansible_by_task_id(task_id):
    return TaskAnsible.objects.get(task_id=task_id)


def save_task_ansible(task_id, playbook_path, playbook_name):
    new_ta = TaskAnsible()
    new_ta.task_id = task_id
    new_ta.playbook_path = playbook_path
    new_ta.playbook_name = playbook_name
    # try to save
    try:
        new_ta.save()
    except Exception as e:
        print(e)
        return None

    return new_ta.id


def update_task_ansible(ta_id, task_id, playbook_path, playbook_name):
    update_ta = find_task_ansible_by_id(ta_id)
    update_ta.task_id = task_id
    update_ta.playbook_path = playbook_path
    update_ta.playbook_name = playbook_name
    # try to update
    try:
        update_ta.save()
    except Exception as e:
        print(e)
        return False

    return True


def delete_task_ansible(ta_id):
    delete_ta = find_task_ansible_by_id(ta_id)
    # try to delete
    try:
        delete_ta.delete()
    except Exception as e:
        print(e)
        return False

    return True

# Method of TaskHostMapping


def find_all_task_host_mapping():
    return TaskHostMapping.objects.all().order_by("id")


def find_task_host_mapping_by_id(th_id):
    return TaskHostMapping.objects.get(pk=th_id)


def find_task_host_mapping_by_task_pagination(task_id):
    return Paginator(TaskHostMapping.objects.filter(task_id=task_id).order_by("id"), DEFAULT_ITEM_PER_PAGE)


def find_task_host_mapping_by_host_pagination(host_id):
    return Paginator(TaskHostMapping.objects.filter(host_id=host_id).order_by("id"), DEFAULT_ITEM_PER_PAGE)


def save_task_host_mapping(task_id, host_id):
    new_th_mapping = TaskHostMapping()
    new_th_mapping.task_id = task_id
    new_th_mapping.host_id = host_id
    # try to save
    try:
        new_th_mapping.save()
    except Exception as e:
        print(e)
        return None

    return new_th_mapping.id


def update_task_host_mapping(th_id, task_id, host_id):
    update_th_mapping = find_task_host_mapping_by_id(th_id)
    update_th_mapping.task_id = task_id
    update_th_mapping.host_id = host_id
    # try to save
    try:
        update_th_mapping.save()
    except Exception as e:
        print(e)
        return False

    return True


def delete_task_host_mapping(th_id):
    delete_th_mapping = find_task_host_mapping_by_id(th_id)
    # try to delete
    try:
        delete_th_mapping.delete()
    except Exception as e:
        print(e)
        return False

    return True


# Method of TaskAppMapping


def find_all_app_host_mapping():
    return TaskAppMapping.objects.all().order_by("id")


def find_task_app_mapping_by_id(ta_id):
    return TaskAppMapping.objects.get(pk=ta_id)


def find_task_app_mapping_by_task_pagination(task_id):
    return Paginator(TaskAppMapping.objects.filter(task_id=task_id).order_by("id"), DEFAULT_ITEM_PER_PAGE)


def find_task_app_mapping_by_host_pagination(app_id):
    return Paginator(TaskAppMapping.objects.filter(app_id=app_id).order_by("id"), DEFAULT_ITEM_PER_PAGE)


def save_task_app_mapping(task_id, app_id):
    new_ta_mapping = TaskHostMapping()
    new_ta_mapping.task_id = task_id
    new_ta_mapping.app_id = app_id
    # try to save
    try:
        new_ta_mapping.save()
    except Exception as e:
        print(e)
        return None

    return new_ta_mapping.id


def update_task_app_mapping(ta_id, task_id, app_id):
    update_ta_mapping = find_task_app_mapping_by_id(ta_id)
    update_ta_mapping.task_id = task_id
    update_ta_mapping.host_id = app_id
    # try to save
    try:
        update_ta_mapping.save()
    except Exception as e:
        print(e)
        return False

    return True


def delete_task_app_mapping(ta_id):
    delete_ta_mapping = find_task_app_mapping_by_id(ta_id)
    # try to delete
    try:
        delete_ta_mapping.delete()
    except Exception as e:
        print(e)
        return False

    return True


# Method of TaskServiceMapping


def find_all_task_service_mapping():
    return TaskServiceMapping.objects.all().order_by("id")


def find_task_service_mapping_by_id(ts_id):
    return TaskServiceMapping.objects.get(pk=ts_id)


def find_task_service_mapping_by_task_pagination(task_id):
    return Paginator(TaskServiceMapping.objects.filter(task_id=task_id).order_by("id"), DEFAULT_ITEM_PER_PAGE)


def find_task_service_mapping_by_service_pagination(service_id):
    return Paginator(TaskServiceMapping.objects.filter(service_id=service_id).order_by("id"), DEFAULT_ITEM_PER_PAGE)


def save_task_service_mapping(task_id, service_id):
    new_ts_mapping = TaskServiceMapping()
    new_ts_mapping.task_id = task_id
    new_ts_mapping.service_id = service_id
    # try to save
    try:
        new_ts_mapping.save()
    except Exception as e:
        print(e)
        return None

    return new_ts_mapping.id


def update_task_service_mapping(ts_id, task_id, service_id):
    update_ts_mapping = find_task_service_mapping_by_id(ts_id)
    update_ts_mapping.task_id = task_id
    update_ts_mapping.service_id = service_id
    # try to save
    try:
        update_ts_mapping.save()
    except Exception as e:
        print(e)
        return False

    return True


def delete_task_service_mapping(ts_id):
    delete_ts_mapping = find_task_service_mapping_by_id(ts_id)
    # try to delete
    try:
        delete_ts_mapping.delete()
    except Exception as e:
        print(e)
        return False

    return True


# Method of TaskRunResult


def find_all_task_run_result_pagination():
    return Paginator(TaskRunResult.objects.all().order_by("id"), DEFAULT_ITEM_PER_PAGE)


def find_task_run_result_by_id(trr_id):
    return TaskRunResult.objects.get(pk=trr_id)


def find_task_run_result_by_status_pagination(status):
    return Paginator(TaskRunResult.objects.filter(status=status).order_by("id"), DEFAULT_ITEM_PER_PAGE)


def find_task_run_result_by_task(task_id):
    return TaskRunResult.objects.filter(task_id=task_id).order_by("id")


def save_task_run_result(task_id, status, start_datetime, end_datetime, result_content="None"):
    new_trr = TaskRunResult()
    new_trr.task_id = task_id
    new_trr.status = status
    new_trr.result_content = result_content
    new_trr.started_at = start_datetime
    new_trr.end_at = end_datetime
    # try to save
    try:
        new_trr.save()
    except Exception as e:
        print(e)
        return None

    return new_trr.id


def update_task_run_result(trr_id, task_id, status, start_datetime, end_datetime, result_content):
    update_trr = TaskRunResult()
    update_trr.task_id = task_id
    update_trr.status = status
    update_trr.result_content = result_content
    update_trr.started_at = start_datetime
    update_trr.end_at = end_datetime
    # try to update
    try:
        update_trr.save()
    except Exception as e:
        print(e)
        return False

    return True


def delete_task_run_result(trr_id):
    delete_trr = find_task_run_result_by_id(trr_id)
    # try to delete
    try:
        delete_trr.delete()
    except Exception as e:
        print(e)
        return False

    return True
