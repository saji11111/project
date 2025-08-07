from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hms.views import *
from booking.views import *
from billing.views import *
from room.views import *
# from .api import router
from .apirep import routerep

urlpatterns = [
    # path('api/sensoviz/', include(router.urls)),
    path('api/v1/', include(routerep.urls)),
    path('admin/', admin.site.urls),
    path('', Home, name="home"),
    path('patient_home', User_Home, name="patient_home"),
    path('doctor_home', Doctor_Home, name="doctor_home"),
    path('admin_home', Admin_Home, name="admin_home"),

    path('our_doctors', Our_Doctors, name="our_doctors"),
    path('contact', Contact, name="contact"),
    path('login', Login_User, name="login"),
    path('login_admin', Login_admin, name="login_admin"),
    path('signup', Signup_User, name="signup"),
    path('logout', Logout, name="logout"),
    path('change_password', Change_Password, name="change_password"),
    path('add_heartdetail', add_heartdetail, name="add_heartdetail"),
    path('view_search_pat', view_search_pat, name="view_search_pat"),

    path('view_doctor', View_Doctor, name="view_doctor"),
    path('add_doctor', add_doctor, name="add_doctor"),
    path('change_doctor/<int:pid>/', add_doctor, name="change_doctor"),
    path('view_patient', View_Patient, name="view_patient"),
    path('view_feedback', View_Feedback, name="view_feedback"),
    path('edit_profile', Edit_My_deatail, name="edit_profile"),
    path('profile_doctor', View_My_Detail, name="profile_doctor"),
    path('sent_feedback', sent_feedback, name="sent_feedback"),

    path('delete_searched/<int:pid>', delete_searched, name="delete_searched"),
    path('delete_doctor<int:pid>', delete_doctor, name="delete_doctor"),
    path('assign_status<int:pid>', assign_status, name="assign_status"),
    path('delete_patient<int:pid>', delete_patient, name="delete_patient"),
    path('delete_feedback<int:pid>', delete_feedback, name="delete_feedback"),
    path('predict_desease/<str:pred>/<str:accuracy>/',
         predict_desease, name="predict_desease"),




    path('index', index, name='index'),
    path('booking', booking, name='booking'),
    path('booking-submit', bookingSubmit, name='bookingSubmit'),
    path('user-panel', userPanel, name='userPanel'),
    path('user-update/<int:id>', userUpdate, name='userUpdate'),
    path('user-update-submit/<int:id>',
         userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel', staffPanel, name='staffPanel'),

    path('login_userx', login_userx, name='loginx'),
    path('logout_userx', logout_userx, name='logoutx'),
    path('register_user', register_user, name='register'),
     #billing

    path('create_bill', create_bill, name='create_bill'),
    path('view_bills', view_bills, name='view_bills'),
    path('billing_main', billing_main, name='billing_main'),

      #room

    
    path('add_room', add_room, name='add_room'),
    path('available_rooms', available_rooms, name='available_rooms'),
    path('allocate_room', allocate_room, name='allocate_room'),
    path('allocated_rooms', allocated_rooms, name='allocated_rooms'),
    path('discharge_patient/<int:pk>', discharge_patient, name='discharge_patient'),
    path('room_main', room_main, name='room_main'),

    # email
    path('confirm-booking', send_confirmation, name='send_confirmation'),
    # email
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
