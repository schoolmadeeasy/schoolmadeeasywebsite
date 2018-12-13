from django.db import models
from localflavor.us.us_states import US_STATES


class AssignmentManager(models.Manager):
    def get_all_assignments(self):
        return self.filter(email_confirmed=True).all()

    def get_latest_assignments(self):
        return self.filter(email_confirmed=True).all().order_by('-timestamp')


class Assignment(models.Model):
    email = models.EmailField(blank=True, null=True)
    state = models.CharField(choices=US_STATES, max_length=75, blank=True, null=True)
    school_name = models.CharField(max_length=75, blank=True, null=True)
    title = models.CharField(max_length=150)
    class_name = models.CharField(max_length=50)
    notes = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=False)

    email_confirmed = models.BooleanField(default=False)  # whether email is confirmed or not

    objects = AssignmentManager()  # manager for queries

    def __str__(self):
        return str(self.title)


class AssignmentImageManager(models.Manager):
    def get_for_assignment(self, assignment_obj):
        return self.filter(assignment=assignment_obj)


class AssignmentImage(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    image = models.FileField(upload_to='media/uploads/')
    order = models.PositiveIntegerField(default=False)

    objects = AssignmentImageManager()  # manager for queries

    def __str__(self):
        return str(self.assignment)



'''
This model was going to be used for a email confirmation for when someone upload an assignment, but I was having too
many problems with it.
'''
'''
class EmailConfirmation(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    user_email = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.assignment) + ' - ' + str(self.user_email)
'''








