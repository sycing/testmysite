from django.db import models
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30)
    headImg = models.FileField(upload_to = './upload/')
    def __unicode__(self):
        return self.username
class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class VqTestcase(models.Model):
    tcno = models.CharField(db_column='TCNO', max_length=20)  # Field name made lowercase.
    interfacename = models.CharField(db_column='InterfaceName', max_length=32)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=40)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=15)  # Field name made lowercase.
    introduce = models.TextField(db_column='Introduce')  # Field name made lowercase.
    priorty = models.CharField(db_column='Priorty', max_length=10)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.
    parameter = models.TextField(db_column='Parameter')  # Field name made lowercase.
    expected_result = models.CharField(db_column='Expected Result', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    testresult = models.CharField(db_column='TestResult', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    interfaceid = models.CharField(db_column='interfaceId', max_length=200, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.interfaceid
    class Meta:
        managed = False
        db_table = 'vq_testcase'
