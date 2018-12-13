from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, ListView
from home.models import Assignment, AssignmentImage
from .itertools_unique_chain import unique_chain
from django.core.paginator import Paginator


class AssignmentView(DetailView):
    template_name = 'assignments/view-assignment.html'
    model = Assignment
    context_object_name = 'get_assignment'

    def get_context_data(self, **kwargs):
        context = super(AssignmentView, self).get_context_data(**kwargs)
        context['images'] = AssignmentImage.objects.filter(assignment=self.object)
        return context


class AllAssignmentsView(ListView):
    template_name = 'assignments/view-all-assignments.html'
    model = Assignment
    context_object_name = 'assignments'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super(AllAssignmentsView, self).get_context_data(**kwargs)
        assignments = self.get_queryset()
        paginator = Paginator(assignments, 25)
        page = self.request.GET.get('page')
        assignments_page = paginator.get_page(page)
        context['assignments_page'] = assignments_page
        return context

    def get_queryset(self):
        queryset = Assignment.objects.get_all_assignments()
        return queryset


class SearchView(View):
    template_name = 'assignments/search.html'

    def get(self, request, *args, **kwargs):
        title_text = self.request.GET.get('title')
        class_name_text = self.request.GET.get('class-name')
        state_text = self.request.GET.get('state')

        query = None
        if title_text and state_text:
            query_one = Assignment.objects.filter(title__iexact=title_text,
                                                  class_name__iexact=class_name_text,
                                                  state__iexact=state_text
                                                  )
            query_two = Assignment.objects.filter(title__icontains=title_text,
                                                  class_name__icontains=class_name_text,
                                                  state__iexact=state_text
                                                  )
            query_three = Assignment.objects.filter(title__icontains=title_text,
                                                    class_name__icontains=class_name_text,
                                                    )
            query_four = Assignment.objects.filter(title__icontains=title_text,
                                                   state__iexact=state_text,
                                                   )
            query_five = Assignment.objects.filter(title__icontains=title_text)

            # combine all of the query sets into one list
            query = list(unique_chain(query_one, query_two, query_three, query_four, query_five))

        context = {
            'title': title_text,
            'class': class_name_text,
            'state': state_text,
            'query': query
        }
        return render(request, self.template_name, context)










