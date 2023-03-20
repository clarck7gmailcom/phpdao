from django.shortcuts import render, redirect, HttpResponse ,get_object_or_404
from phpdao1 import models
from utils.bootstrap import BootStrapModeForm
from django import forms
from phpdao1.models import DiseaseDict, DrugDict, VaccineDict, ManuDict, HidMain, HidRecord
from django.http import JsonResponse
from utils.pagination import Pagination


# Define 3 model forms to collect each data separately
class uploadliteModelForm(forms.ModelForm):
    class Meta:
        model = models.UploadFormlite
        fields = [
            'userinfo',
            'hidmain_index',
            'disease_name',
            'duration_disease',
            'drug_name',
            'drug_manuf',
            'vaccine_name',
            'vaccine_manuf',
            'covid_status',
            'covid_treatment_name',
        ]


def audit(request):
    title = 'Data Audition'
    form = uploadliteModelForm

    queryset = models.UploadFormlite.objects.all().order_by('-id')
    # for i in queryset:
        # print('audit queryset:', i.get_audit_display())

    pager = Pagination(request, queryset.count())
    queryset = queryset[pager.start:pager.end]
    context = {
        "title": title,
        "queryset": queryset,
        "pager_string": pager.html(),
        "form": form,
    }
    return render(request, 'audit.html', context)


def audit_rejected(request, pk):
    # 页面通过AJAX的url拼接 pass pk 进来，然后update models
    if request.method == 'POST':
        try:
            content = request.POST.get('reject_reason')
            models.UploadFormlite.objects.filter(id=pk).update(audit='rejected', reject_reason=content)
            # get the data record according to the id, save in data_record
            data_record = models.UploadFormlite.objects.get(id=pk)
            # extract the userinfo_id from the data_record (above) to save in the userid
            userid = data_record.userinfo_id
            # create a new message saving the content and how can see the message (userinfo_id)
            models.Message.objects.filter(id=pk).create(content="Your submitted data was rejected. The probably reason: " + content, userinfo_id=userid)
            return JsonResponse({"status": True})
        except Exception as e:
            print(f"Error creating Message instance: {e}")
            return JsonResponse({"status": False})


def audit_approved(request, pk):
    # 页面通过AJAX的url拼接 pass pk 进来，然后update models
    try:
        models.UploadFormlite.objects.filter(id=pk).update(audit='approved')

        # get the data record according to the id, save in data_record
        data_record = models.UploadFormlite.objects.get(id=pk)
        # extract the userinfo_id from the data_record (above) to save in the userid
        userid = data_record.userinfo_id
        # create a new message saving the content and how can see the message (userinfo_id)
        models.Message.objects.filter(id=pk).create(content="Your data has been approved!", userinfo_id=userid)

        return JsonResponse({"status": True})
    except Exception as e:
        return JsonResponse({"status": False})
