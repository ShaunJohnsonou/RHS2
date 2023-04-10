from django.db import models

#'Is staff' can tell you if a user is a viewer, or if they can actively change data.


Users = (
    ('Shaun', 'Shaun'),
)

Reporting_Period_Choices = (
    ('This Week', 'This Week'),
    ('Next Week', 'Next Week'),
    ('Upcoming', 'Upcoming'),
    ('N/A', 'N/A'),
)
type = (
    ('Problem', 'Problem'),
    ('Action', 'Action'),
    ('Event', 'Event'),
    ('Comment', 'Comment'),
)
Priority = (
    ('High', 'High'),
    ('Normal', 'Normal'),
    ('Low', 'Low'),
)
Status = (
    ('Complete', 'Complete'),
    ('In Progress', 'In Progress'),
    ('Pending', 'Pending'),
    ('Paused', 'Paused'),
    ('Due', 'Due'),
)

Users = (
    ('Shaun', 'Shaun'),
)


class Task(models.Model):

    Project_Name = models.CharField(max_length=20)
    Reporting_Period = models.CharField(max_length=20, choices=Reporting_Period_Choices, default= 'N/A')
    Type = models.CharField(max_length=500, choices=type)
    Type_Description = models.CharField(max_length=200)
    Priority = models.CharField(max_length=40, choices=Priority)
    Status = models.CharField(max_length=15, choices=Status)
    Logged_By = models.CharField(max_length=50, choices=Users)
    Responsible = models.CharField(max_length=50, choices=Users)
    Start_Date = models.DateField(max_length=50)
    Target_Date = models.DateField(max_length=50)
    FeedBack = models.CharField(max_length=200)


    def __str__(self):
        return self.Project_Name
# Create your models here.


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class HomeTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_name = models.CharField(db_column='Project_Name', max_length=20)  # Field name made lowercase.
    reporting_period = models.CharField(db_column='Reporting_Period', max_length=20)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=500)  # Field name made lowercase.
    type_description = models.CharField(db_column='Type_Description', max_length=200)  # Field name made lowercase.
    priority = models.CharField(db_column='Priority', max_length=40)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15)  # Field name made lowercase.
    logged_by = models.CharField(db_column='Logged_By', max_length=50)  # Field name made lowercase.
    responsible = models.CharField(db_column='Responsible', max_length=50)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_Date')  # Field name made lowercase.
    target_date = models.DateField(db_column='Target_Date')  # Field name made lowercase.
    feedback = models.CharField(db_column='FeedBack', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Home_task'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
