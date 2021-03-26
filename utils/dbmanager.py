from user.models import *
from django.utils import timezone as datetime

# Method for User models


def find_all_users():
    all_users = User.objects.all()
    return all_users


def find_user_by_id(user_id):
    return User.objects.get(pk=user_id)


def find_user_by_username(username):
    user_list = User.objects.filter(user_name=username)
    if len(user_list) == 0:
        return None
    else:
        return user_list[0]


def find_user_by_realname(realname):
    user_list = User.objects.filter(real_name=realname)
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
        return False

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
    delete_user.delete()

    


    

