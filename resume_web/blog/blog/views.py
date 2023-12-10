from django.views import generic



class HomePageView(generic.TemplateView):
    template_name = 'home/home.html'


class AboutPageView(generic.TemplateView):
    template_name = 'home/about.html'

class HobbyPageView(generic.TemplateView):
    template_name = 'home/hobby_base.html'


class ExperiencePageView(generic.TemplateView):
    template_name = 'home/experience.html'

class SkillsPageView(generic.TemplateView):
    template_name = 'home/skills.html'
