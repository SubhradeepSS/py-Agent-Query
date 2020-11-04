from django.db import models
from django.forms import ModelForm, TextInput
from django.contrib.admin import widgets

# Create your models here.
class Role(models.Model):
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.role

class Agent(models.Model):
    is_available = models.BooleanField(default=False)
    available_since = models.TimeField(blank=True, null=True)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return str(self.id)

class Agent_Form(ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
        widgets = {
            'available_since': TextInput(attrs={'placeholder': 'hr:min (24 hr)'})
        }
    
MODES = (
    ("available","available"), ("least_busy","least_busy"), ("random","random")
)

class Issue(models.Model):
    roles = models.ManyToManyField(Role)
    mode = models.CharField(choices=MODES, max_length=12)

    def __str__(self):
        return str(self.id)

class Issue_Form(ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'  
