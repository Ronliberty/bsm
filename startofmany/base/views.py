from django.contrib.auth.decorators import login_required
from users.decorators import role_required
from django.shortcuts import render, redirect
from .forms import HeroContentForm, GalleryItemForm, PricingPlanForm, AboutSectionForm, ContactInfoForm
from .models import HeroContent, GalleryItem, PricingPlan, AboutSection, ContactInfo
from django.shortcuts import get_object_or_404

def index(request):
    # Fetching data from each model
    hero_content = HeroContent.objects.first()
    gallery_items = GalleryItem.objects.all()
    pricing_plans = PricingPlan.objects.all()
    about_content = AboutSection.objects.first()  # Assuming only one about section content
    contact_info = ContactInfo.objects.all()  # If multiple, otherwise `.first()`

    # Context dictionary to pass data to template
    context = {
        'hero_content': hero_content,
        'gallery_items': gallery_items,
        'pricing_plans': pricing_plans,
        'about_content': about_content,
        'contact_info': contact_info,
    }

    return render(request, 'base/index.html', context)

@login_required
@role_required('manager')
def section_view(request, section_name):
    sections = {
        'hero': {'form': HeroContentForm, 'model': HeroContent, 'prefix': "hero"},
        'gallery': {'form': GalleryItemForm, 'model': GalleryItem, 'prefix': "gallery"},
        'pricing': {'form': PricingPlanForm, 'model': PricingPlan, 'prefix': "pricing"},
        'about': {'form': AboutSectionForm, 'model': AboutSection, 'prefix': "about"},
        'contact': {'form': ContactInfoForm, 'model': ContactInfo, 'prefix': "contact"},
    }

    if section_name not in sections:
        return redirect('base:index')  # Redirect if invalid section name

    FormClass = sections[section_name]['form']
    ModelClass = sections[section_name]['model']
    prefix = sections[section_name]['prefix']

    # Handle POST requests for form submission
    if request.method == 'POST':
        form = FormClass(request.POST, request.FILES, prefix=prefix)
        if form.is_valid():
            form.save()
            return redirect('base:section', section_name=section_name)
    else:
        form = FormClass(prefix=prefix)

    # Fetch existing items for the section
    items = ModelClass.objects.all()

    context = {
        'form': form,
        'items': items,
        'section_name': section_name,  # To dynamically render based on section
    }

    return render(request, 'base/admin_post_data.html', context)


@login_required
@role_required('manager')
def delete_item(request, section_name, item_id):
    sections = {
        'hero': HeroContent,
        'gallery': GalleryItem,
        'pricing': PricingPlan,
        'about': AboutSection,
        'contact': ContactInfo,
    }

    if section_name in sections:
        ModelClass = sections[section_name]
        item = get_object_or_404(ModelClass, id=item_id)
        item.delete()

    return redirect('base:section', section_name=section_name)


def landing(request):
    return render(request, 'base/landing.html')