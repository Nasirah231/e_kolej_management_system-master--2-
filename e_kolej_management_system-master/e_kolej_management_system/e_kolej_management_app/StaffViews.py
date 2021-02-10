import json
from datetime import datetime
from uuid import uuid4
import requests

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from e_kolej_management_app.forms import EditStudentForm, ApplyForm
from e_kolej_management_app.models import Students, Staffs, FeedBackStaffs, CustomUser, NotificationStaffs, ApplyException

def staff_home(request):
    
    #Fetch All Approve apply
    staff=Staffs.objects.get(admin=request.user.id)
    apply = ApplyException.objects.all()
    return render(request, "staff_template/staff_home_template.html", {"apply": apply})

def staff_manage_student(request):
    students = Students.objects.all()
    return render(request, "staff_template/staff_manage_student_template.html", {"students": students})

def staff_edit_student(request, student_id):
    request.session['student_id'] = student_id
    student = Students.objects.get(admin=student_id)
    form = EditStudentForm()
    form.fields['email'].initial = student.admin.email
    form.fields['first_name'].initial = student.admin.first_name
    form.fields['last_name'].initial = student.admin.last_name
    form.fields['username'].initial = student.admin.username
    form.fields['address'].initial = student.address
    form.fields['gender'].initial = student.gender
    return render(request, "staff_template/staff_edit_student_template.html", {"form": form, "id": student_id, "username": student.admin.username})

def staff_edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id = request.session.get("student_id")
        if student_id == None:
            return HttpResponseRedirect(reverse("staff_manage_student"))

        form = EditStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            gender = form.cleaned_data["gender"]

            if request.FILES.get('profile_pic', False):
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

            try:
                user = CustomUser.objects.get(id=student_id)
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                user.save()

                student = Students.objects.get(admin=student_id)
                student.address = address
                student.gender = gender
                if profile_pic_url != None:
                    student.profile_pic = profile_pic_url
                student.save()
                del request.session['student_id']
                messages.success(request, "Successfully Edited Student")
                return HttpResponseRedirect(reverse("staff_edit_student", kwargs={"student_id": student_id}))
            except:
                messages.error(request, "Failed to Edit Student")
                return HttpResponseRedirect(reverse("staff_edit_student", kwargs={"student_id": student_id}))
        else:
            form = EditStudentForm(request.POST)
            student = Students.objects.get(admin=student_id)
            return render(request, "staff_template/staff_edit_student_template.html", {"form": form, "id": student_id, "username": student.admin.username})


def list_applicant(request):

    #apply = ApplyException.objects.values_list('student_id', flat=True)
    #students = Students.objects.filter(
        #student_id__in=ApplyException.values_list(apply, flat=True))
    #students = Students.objects.all()
    apply = ApplyException.objects.all()
    return render(request, "staff_template/list_applicant.html", {"apply": apply})

def view_applicant(request, student_id):
    request.session['student_id'] = student_id
    student = Students.objects.get(admin=student_id)
    form = ApplyForm()
    form.fields['email'].initial = student.admin.email
    form.fields['first_name'].initial = student.admin.first_name
    form.fields['last_name'].initial = student.admin.last_name
    form.fields['address'].initial = student.address
    form.fields['gender'].initial = student.gender
    return render(request, "staff_template/view_applicant.html", {"form": form, "id": student_id, "username": student.admin.username})

def view_applicant_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id = request.session.get("student_id")
        if student_id == None:
            return HttpResponseRedirect(reverse("view_applicant"))

        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            gender = form.cleaned_data["gender"]
            address = form.cleaned_data["address"]
            level = form.cleaned_data["level"]
            scholarship = form.cleaned_data["scholarship"]
            family_income = form.cleaned_data["family_income"]
            family_dependent = form.cleaned_data["family_dependent"]
            family_problem = form.cleaned_data["family_problem"]
            health_problem = form.cleaned_data["health_problem"]

        try:
            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            student = Students.objects.get(admin=student_id)
            student.gender = gender
            student.address = address
            student.level = level
            student.scholarship = scholarship
            student.family_income = family_income
            student.family_dependent = family_dependent
            student.family_problem = family_problem
            student.health_problem = health_problem
            student.save()
            del request.session['student_id']
            messages.success(request, "Successfully View Student")
            return HttpResponseRedirect(reverse("view_applicant", kwargs={"student_id": student_id}))
        except:
            messages.error(request, "Failed to View Student")
            return HttpResponseRedirect(reverse("view_applicant", kwargs={"student_id": student_id}))
        else:
            form=ApplyForm(request.POST)
            student=Students.objects.get(admin=student_id)
            return render(request, "staff_template/view_applicant.html", {"form": form, "id": student_id, "username": student.admin.username})

@csrf_exempt
def get_students(request):
    
    list_data=[]

def student_approve_apply(request, apply_id):
    apply = ApplyException.objects.get(id=apply_id)
    apply.apply_status = 1
    apply.save()
    return HttpResponseRedirect(reverse("list_applicant"))


def student_disapprove_apply(request, apply_id):
    apply = ApplyException.objects.get(id=apply_id)
    apply.apply_status = 2
    apply.save()
    return HttpResponseRedirect(reverse("list_applicant"))

def staff_feedback(request):
    staff_id=Staffs.objects.get(admin=request.user.id)
    feedback_data=FeedBackStaffs.objects.filter(staff_id=staff_id)
    return render(request,"staff_template/staff_feedback.html",{"feedback_data":feedback_data})

def staff_feedback_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("staff_feedback_save"))
    else:
        feedback_msg=request.POST.get("feedback_msg")

        staff_obj=Staffs.objects.get(admin=request.user.id)
        try:
            feedback=FeedBackStaffs(staff_id=staff_obj,feedback=feedback_msg,feedback_reply="")
            feedback.save()
            messages.success(request, "Successfully Sent Feedback")
            return HttpResponseRedirect(reverse("staff_feedback"))
        except:
            messages.error(request, "Failed To Send Feedback")
            return HttpResponseRedirect(reverse("staff_feedback"))

def staff_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    staff=Staffs.objects.get(admin=user)
    return render(request,"staff_template/staff_profile.html",{"user":user,"staff":staff})

def staff_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("staff_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        address=request.POST.get("address")
        password=request.POST.get("password")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            staff=Staffs.objects.get(admin=customuser.id)
            staff.address=address
            staff.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("staff_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("staff_profile"))

@csrf_exempt
def staff_fcmtoken_save(request):
    token=request.POST.get("token")
    try:
        staff=Staffs.objects.get(admin=request.user.id)
        staff.fcm_token=token
        staff.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def staff_all_notification(request):
    staff=Staffs.objects.get(admin=request.user.id)
    notifications=NotificationStaffs.objects.filter(staff_id=staff.id)
    return render(request,"staff_template/all_notification.html",{"notifications":notifications})

def returnHtmlWidget(request):
    return render(request,"widget.html")
