from django.utils import timezone

from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    create_date = models.DateTimeField(
        'Created',
        auto_now_add=True,
        editable=False
    )
    modified_date = models.DateTimeField(
        'Modified',
        auto_now_add=True,
        editable=True
    )

    def save(self, *args, **kwargs):
        try:
            if self.id:
                self.modified_date = timezone.now()
            else:
                self.create_date = timezone.now()
                
        except Exception as e:
            print(e)
                
                            
        super(BaseModel, self).save(*args, **kwargs)



class BaseModelBalance(models.Model):
    class Meta:
        abstract = True

    create_date = models.DateTimeField(
        'Created',
        auto_now_add=True,
        editable=False
    )
    modified_date = models.DateTimeField(
        'Modified',
        auto_now_add=True,
        editable=True
    )

    def save(self, *args, **kwargs):                
        try:        
            if self.operation:
                self.modified_date = timezone.now()
            else:
                self.create_date = timezone.now()
        except Exception as e:
            print(e)
                            
        super(BaseModelBalance, self).save(*args, **kwargs)
