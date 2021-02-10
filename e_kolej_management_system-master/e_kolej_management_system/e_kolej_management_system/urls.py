"""e_kolej_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from e_kolej_management_app import views, HodViews, StaffViews, StudentViews
from e_kolej_management_system import settings

urlpatterns = [
    path('demo', views.showDemoPage),
    path('signup_admin', views.signup_admin, name="signup_admin"),
    path('signup_student', views.signup_student, name="signup_student"),
    path('signup_staff', views.signup_staff, name="signup_staff"),
    path('do_admin_signup', views.do_admin_signup, name="do_admin_signup"),
    path('do_staff_signup', views.do_staff_signup, name="do_staff_signup"),
    path('do_signup_student', views.do_signup_student, name="do_signup_student"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.ShowLoginPage, name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user, name="logout"),
    path('doLogin', views.doLogin, name="do_login"),
    path('admin_home', HodViews.admin_home, name="admin_home"),
    path('manage_staff', HodViews.manage_staff, name="manage_staff"),
    path('manage_student', HodViews.manage_student, name="manage_student"),
    path('edit_staff/<str:staff_id>', HodViews.edit_staff, name="edit_staff"),
    path('edit_staff_save', HodViews.edit_staff_save, name="edit_staff_save"),
    path('edit_student/<str:student_id>',
         HodViews.edit_student, name="edit_student"),
    path('edit_student_save', HodViews.edit_student_save, name="edit_student_save"),
    path('check_email_exist', HodViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist', HodViews.check_username_exist,
         name="check_username_exist"),
    path('student_feedback_message', HodViews.student_feedback_message,
         name="student_feedback_message"),
    path('student_feedback_message_replied', HodViews.student_feedback_message_replied,
         name="student_feedback_message_replied"),
    path('staff_feedback_message', HodViews.staff_feedback_message,
         name="staff_feedback_message"),
    path('staff_feedback_message_replied', HodViews.staff_feedback_message_replied,
         name="staff_feedback_message_replied"),
    path('admin_profile', HodViews.admin_profile, name="admin_profile"),
    path('admin_profile_save', HodViews.admin_profile_save,
         name="admin_profile_save"),
    path('admin_send_notification_staff', HodViews.admin_send_notification_staff,
         name="admin_send_notification_staff"),
    path('admin_send_notification_student', HodViews.admin_send_notification_student,
         name="admin_send_notification_student"),
    path('send_student_notification', HodViews.send_student_notification,
         name="send_student_notification"),
    path('send_staff_notification', HodViews.send_staff_notification,
         name="send_staff_notification"),

    #     Staff URL Path
    path('staff_home', StaffViews.staff_home, name="staff_home"),
    path('staff_manage_student', StaffViews.staff_manage_student,
         name="staff_manage_student"),
    path('staff_edit_student/<str:student_id>',
         StaffViews.staff_edit_student, name="staff_edit_student"),
    path('staff_edit_student_save', StaffViews.staff_edit_student_save,
         name="staff_edit_student_save"),

    path('list_applicant', StaffViews.list_applicant,
         name="list_applicant"),
    path('view_applicant/<str:student_id>', 
         StaffViews.view_applicant, name="view_applicant"),
    path('view_applicant_save', StaffViews.view_applicant_save,
         name="view_applicant_save"),

    path('student_approve_apply/<str:apply_id>',
         StaffViews.student_approve_apply, name="student_approve_apply"),
    path('student_disapprove_apply/<str:apply_id>',
         StaffViews.student_disapprove_apply, name="student_disapprove_apply"),
    path('staff_feedback', StaffViews.staff_feedback, name="staff_feedback"),
    path('staff_feedback_save', StaffViews.staff_feedback_save,
         name="staff_feedback_save"),
    path('staff_profile', StaffViews.staff_profile, name="staff_profile"),
    path('staff_profile_save', StaffViews.staff_profile_save,
         name="staff_profile_save"),
    path('staff_fcmtoken_save', StaffViews.staff_fcmtoken_save,
         name="staff_fcmtoken_save"),
    path('staff_all_notification', StaffViews.staff_all_notification,
         name="staff_all_notification"),

    #student#
    path('student_home', StudentViews.student_home, name="student_home"),
    path('student_apply_exception', StudentViews.student_apply_exception,
         name="student_apply_exception"),
    path('student_apply_exception_save',
         StudentViews.student_apply_exception_save, name="student_apply_exception_save"),
    path('apply_history', StudentViews.apply_history,
         name="apply_history"),
    path('apply_history_save',
         StudentViews.apply_history_save, name="apply_history_save"),
   
    path('student_feedback', StudentViews.student_feedback, name="student_feedback"),
    path('student_feedback_save', StudentViews.student_feedback_save,
         name="student_feedback_save"),
    path('student_profile', StudentViews.student_profile, name="student_profile"),
    path('student_profile_save', StudentViews.student_profile_save,
         name="student_profile_save"),
    path('student_fcmtoken_save', StudentViews.student_fcmtoken_save,
         name="student_fcmtoken_save"),
    path('firebase-messaging-sw.js', views.showFirebaseJS, name="show_firebase_js"),
    path('student_all_notification', StudentViews.student_all_notification,
         name="student_all_notification"),

    path('node_modules/canvas-designer/widget.html',
         StaffViews.returnHtmlWidget, name="returnHtmlWidget"),
    path('testurl/', views.Testurl)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
