from django.shortcuts import render, redirect
from django.views.generic import View
from django.forms import modelformset_factory
from .models import Assignment, AssignmentImage
from .forms import AssignmentForm, ImageForm
from django.utils import timezone


class IndexView(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        latest_assignments = Assignment.objects.get_latest_assignments()[:3]
        context = {
            'latest_assignments': latest_assignments
        }
        return render(request, self.template_name, context)


def upload(request):
    ImageFormSet = modelformset_factory(
                                        AssignmentImage, form=ImageForm,
                                        min_num=1, validate_min=True, extra=4
                                        )
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=AssignmentImage.objects.none())

        if form.is_valid and formset.is_valid():
            instance = form.save(commit=False)
            instance.email_confirmed=True
            instance.timestamp = timezone.now()
            instance.save()

            assignment_pk = instance.pk

            for form in formset.cleaned_data:
                try:
                    image = form['image']
                except:
                    image = None
                if image is not None:
                    image = form['image']
                    image_obj = AssignmentImage(assignment=instance, image=image)
                    image_obj.save()
            return redirect('/assignments/view/'+str(assignment_pk)+'/')
    else:
        form = AssignmentForm()
        formset = ImageFormSet(queryset=AssignmentImage.objects.none())

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'home/upload.html', context)









