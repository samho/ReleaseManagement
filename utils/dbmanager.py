from user.models import *
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



    

