from django.db import models


class BaseModel(models.Model):
    
    id=models.AutoField(primary_key=True)
    state=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    
    class Meta:
        
        abstract = True
        verbose_name = "modelo base"
        verbose_name_plural ="Modelos bases"
