from django.templatetags.static import static

def static_urls(request):
    return {
        'STATIC_URLS': {
            'favicon_boys': static('assets/img/favicon_boys.ico?v=0.2'),
            'logo_boys': static('assets/img/blue_logo.png'),
            'favicon_girls': static('assets/img/favicon_girls.ico?v=0.2'),
            'logo_girls': static('assets/img/pink_logo.png')
        }
    }