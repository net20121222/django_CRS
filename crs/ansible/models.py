from django.db import models
from django.db.models import SET_NULL


class BasicInfo(models.Model):
    class Meta:
        abstract = True
    description   = models.TextField(blank=True, default='')
    created_by    = models.ForeignKey('auth.User', on_delete=SET_NULL, null=True, related_name='%s(class)s_created', editable=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    active        = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode("%s-%s"% (self.name, self.id))

class CommonInfoUniName(BasicInfo):
	class Meta:
		abstract = True
	name = models.CharField(max_length = 128,unique = True)

class CommonInfoUnuniName(BasicInfo):
	class Meta:
		abstract = True
	name = models.CharField(max_length = 128,unique = False)

class Credential(CommonInfoUnuniName):
	user = models.ForeignKey('auth.user',null = True,default = None,blank = True,on_delete = SET_NULL,related_name = 'credentials')
	ssh_username = models.CharField(blank = True,default = '',max_length = 1024,verbose_name = 'SSH username')
	ssh_password = models.CharField(blank = True,default = '',max_length = 1024,verbose_name = 'SSH password')
	ssh_key_data = models.TextField(blank = True,default = '',verbose_name= 'SSH privite key')
	ssh_key_unlock = models.CharField(blank = True,default = '',max_length = 1024,verbose_name = 'SSH key unlock')
	sudo_username = models.CharField(blank = True,default = '',max_length = 1024)
	sudo_password = models.CharField(blank = True,default = '',max_length = 1024)

class Project(CommonInfoUniName):
	scmtype = models.CharField(max_length = 1024)
	scmurl = models.CharField(blank = True,null = True,max_length = 1024)
	group = models.CharField(max_length = 128,null = True,blank = True)
	class Meta:
		permissions = (
			('access_pro','Access Project'),
			('config_pro','Config Project'),
			('execute_pro','Execute Project'),
			('manager_pro','Manager Project'),
			)

		
