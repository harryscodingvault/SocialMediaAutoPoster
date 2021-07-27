from .models import Social

def footer_nav(request):
    social_data = Social.objects.all()
    context = {
        'social': social_data,
    }
    return context