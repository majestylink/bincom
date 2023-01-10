from django.db.models import Sum
from django.shortcuts import render, redirect

from src.models import AnnouncedPollingUnitResult, PollingUnit, LGA, Party


def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,
    }
    return redirect('/list_polls')

# @login_required
def list_pools(request):
    header = 'List of Polls'
    queryset = AnnouncedPollingUnitResult.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "lgas": LGA.objects.all()[::-1]
    }
    return render(request, "list_item.html", context)


def polling_unit_detail(request, polling_unit_unique_id):
    queryset = AnnouncedPollingUnitResult.objects.filter(polling_unit_unique_id=polling_unit_unique_id)
    context = {
        "queryset": queryset,
        "header": polling_unit_unique_id,
        "parties": Party.objects.all(),
        "pu_name": PollingUnit.objects.get(unique_id=polling_unit_unique_id)
    }
    return render(request, "polling_unit_detail.html", context)


def summed_results(request, lga_id):
    queryset = AnnouncedPollingUnitResult.objects.filter(polling_unit_unique_id=lga_id).values("party_abbreviation").annotate(Sum('party_score'))
    context = {
        "queryset": queryset,
        "header": "Summed results for local governments"
    }
    return render(request, "total_res_by_lga.html", context)
