from django.urls import path
from.import views
urlpatterns = [
    path('',views.regestraion_form ),
    path('log',views.login),
    path('newaccount',views.newaccount ),
    path('home',views.display_homepage),
    path('regestration',views.regestration_user),
    path('aboutus',views.aboutus),
    path('myjobs',views.myjobs_page),
    path('jobs',views.jobspage),
    path('postjob',views.postjob),
    path('logout',views.logout),
    path('addjob',views.addjobs),
    path('apply/<id2>',views.apply_job),
    path('del/<id>',views.deletejob),
    path('jobs/showmore/<id1>',views.showmore),
    path('edit/<num>',views.edit),
    path('editjob/<num1>',views.edit_job),
    path('addcom',views.addcompany),
    path('like/<id3>',views.likeajob),
    path('alljobs',views.alljob),
    path('addcat',views.addcat),
    
    
   
   
   
]