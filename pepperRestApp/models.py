from django.db import models

# Create your models here.

# POSSIBLE States for TODOs
# T = todo
# I = in-progress
# D = done

TodoStates = [ "T", "I", "D"]

class TODOs(models.Model):
    td_state = models.CharField(db_column="TD_state", max_length=1, blank=False, null=False)
    td_duedate = models.DateField(db_column="TD_duedate",blank=True, null=True)
    td_text = models.CharField(db_column="TD_text", max_length=300, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'TODO'

    def __str__(self):
        return "{} / {} / {}".format(self.td_state, self.td_duedate, self.td_text)
