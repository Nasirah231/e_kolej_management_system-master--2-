import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from e_kolej_management_app.forms import ApplyForm
from e_kolej_management_app.models import Students, CustomUser, \
    FeedBackStudent, NotificationStudent, ApplyException


def student_home(request):
    student_obj=Students.objects.get(admin=request.user.id)
    staff_obj = Students.objects.get(admin=request.user.id)
    apply_data = ApplyException.objects.filter(student_id=staff_obj)

    return render(request, "student_template/student_home_template.html", {"apply_data": apply_data})

def student_apply_exception(request):
    form = ApplyForm()
    return render(request, "student_template/student_apply_exception.html", {"form": form})

def student_apply_exception_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_apply_exception"))
    else:
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
            
        
        student_obj=Students.objects.get(admin=request.user.id)
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.save()

            student = Students.objects.get(admin=customuser)
            student.gender = gender
            student.address = address
            student.level = level
            student.scholarship = scholarship
            student.family_income = family_income
            student.family_dependent = family_dependent
            student.family_problem = family_problem
            student.health_problem = health_problem
            student.save()
            apply_report = ApplyException(
                student_id=student_obj, gender=gender, address=address, level=level, scholarship=scholarship, family_income=family_income, family_dependent=family_dependent, family_problem=family_problem, health_problem=health_problem, apply_status=0)
            apply_report.save()
            messages.success(request, "Successfully Applied for Exception")
            return HttpResponseRedirect(reverse("student_apply_exception"))
        except:
            messages.error(request, "Failed To Apply for Exception")
            return HttpResponseRedirect(reverse("student_apply_exception"))
        else:
            form = ApplyForm(request.POST)
            return render(request, "student_template/student_apply_exception.html", {"form": form})


def apply_history(request):
    staff_obj = Students.objects.get(admin=request.user.id)
    apply_data = ApplyException.objects.filter(student_id=staff_obj)
    return render(request, "student_template/apply_history.html", {"apply_data": apply_data})


def apply_history_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("apply_history"))
    else:
        apply_date = request.POST.get("apply_date")

        student_obj = Students.objects.get(admin=request.user.id)
        try:
            apply_report = ApplyException(
                student_id=student_obj, apply_date=apply_date, apply_status=0)
            apply_report.save()
            messages.success(request, "Successfully Applied for Exception")
            return HttpResponseRedirect(reverse("apply_history"))
        except:
            messages.error(request, "Failed To Apply for Exception")
            return HttpResponseRedirect(reverse("apply_history"))

def student_feedback(request):
    staff_id=Students.objects.get(admin=request.user.id)
    feedback_data=FeedBackStudent.objects.filter(student_id=staff_id)
    return render(request,"student_template/student_feedback.html",{"feedback_data":feedback_data})

def student_feedback_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_feedback"))
    else:
        feedback_msg=request.POST.get("feedback_msg")

        student_obj=Students.objects.get(admin=request.user.id)
        try:
            feedback=FeedBackStudent(student_id=student_obj,feedback=feedback_msg,feedback_reply="")
            feedback.save()
            messages.success(request, "Successfully Sent Feedback")
            return HttpResponseRedirect(reverse("student_feedback"))
        except:
            messages.error(request, "Failed To Send Feedback")
            return HttpResponseRedirect(reverse("student_feedback"))

def student_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    student=Students.objects.get(admin=user)
    return render(request,"student_template/student_profile.html",{"user":user,"student":student})

def student_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            student=Students.objects.get(admin=customuser)
            student.address=address
            student.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("student_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("student_profile"))

@csrf_exempt
def student_fcmtoken_save(request):
    token=request.POST.get("token")
    try:
        student=Students.objects.get(admin=request.user.id)
        student.fcm_token=token
        student.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def student_all_notification(request):
    student=Students.objects.get(admin=request.user.id)
    notifications=NotificationStudent.objects.filter(student_id=student.id)
    return render(request,"student_template/all_notification.html",{"notifications":notifications})


