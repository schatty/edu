from datetime import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse


class Project(models.Model):
    """Project links several hypothesis. """
    name = models.CharField(max_length=64, default="base")
    # Author is left for future
    # author = models.ForeignKey(         # Not sure about this
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE
    # )
    start_dt = models.DateTimeField(default=datetime.now)
    description = models.TextField(blank=True)


class Hypothesis(models.Model):
    """Hypothesis links several runs. """
    name = models.CharField(max_length=64, null=False)
    # Author is left for future
    # author = models.ForeignKey(         # Not sure about this
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE
    # )
    desciption = models.TextField(blank=True)
    confirmed = models.BooleanField(null=True)
     
    

class Run(models.Model):
    """General experimental run. """
    name = models.CharField(max_length=64, default="base")
    datetime = models.DateTimeField(default=datetime.now)
    # Author is left for future
    # author = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=CASCADE
    # )
    hypothesis = models.ForeignKey("experiments.Hypothesis", on_delete=models.CASCADE)
    system = models.JSONField(default=dict)
    scalars = models.JSONField(default=dict)
    artifacts = models.JSONField(default=dict)
    checkpoints = models.JSONField(default=dict)

    def __str__(self):
        return f"run_{self.name}"

    def get_tags(self):
        return list(sorted(self.scalars.keys()))

    def get_absolute_url(self):
        return reverse("run_detail", args=[str(self.id)])


class RLRun(Run):
    """RL experimental run. """
    env = models.CharField(max_length=64, null=False)
    algo = models.CharField(max_length=64, null=False)
    seed = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.env}_{self.algo}_{self.name}_seed_{self.seed:02}"