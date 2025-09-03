from django.urls import path,re_path
from . import views
urlpatterns = [
    path('hello/',views.hello),
    path('home/',views.home),
    path('homepage/',views.homepage),
    path('dish/',views.menuitem),
    path('dishes/',views.menuitems),
    
    # Dynamic URLs (Route parameter)
    path('greet/<str:name>',views.greet),
    path('menuitems1/<str:dish>',views.menuitems1),
    path('menuitems5/<str:dish>',views.menuitems5),
    
    # Dynamic URLs (Query parameters)
    path('recipe/',views.recipe),
    path('addition/',views.addition),
    
    # http://127.0.0.1:8000/calculate/divide/15/3
    path('calculate/<str:operation>/<int:v1>/<int:v2>',views.calculate),
    # http://127.0.0.1:8000/calculator/?operation=add&v1=12&v2=15
    path('calculator/',views.calculator),
    
    # Regular Expression -regex
    
    # http://127.0.0.1:8000/user/khushi/
    # re_path(r'^user/(?P<username>[a-zA-Z]+)/$',views.user_profile) # paramter manadatory as + is used
    re_path(r'^user/(?P<username>[a-zA-Z]*)/?$',views.user_profile), # paramter manadatory as + is used
    
    # works same [0-9] or \d
    # re_path(r'item/(?P<item_id>[0-9]+)/$',views.item_detail),
    # re_path(r'item/(?P<item_id>\d+)/$',views.item_detail),
    
    # http://127.0.0.1:8000/item/3456/
    # re_path(r'item/(?P<item_id>\d{4})/$',views.item_detail), # ID should contain exactly 4 digits
    
    # re_path(r'item/(?P<item_id>\d{1,4})/$',views.item_detail), # ID should contain min 1 and max 4 digits {lowerLimit,upperLimit} => {1,4}
    
    # http://127.0.0.1:8000/item/31_ab-5/  
    re_path(r'item/(?P<item_id>[\w-]+)/$',views.item_detail), # ID can be both characters and digits with hypens ,underscores
    
    # http://127.0.0.1:8000/restarant/main-course/biyani
    re_path(r'restarant/(?P<category>[\w\s&-]+)/(?P<subcategory>[\w-]*)/?$',views.restro_detail),
    
    
    path('home1/',views.home1,name='home1'),
    path('menu/',views.menu),
    
    path('menu1/',views.menu1),

    path('home2/',views.home2,name='home2'),
    path('about/',views.about, name='about'),
    path('menuitems',views.menus, name='menuitems'),
    path('menuitems2/<str:item>',views.menuitems2,name='menuitems2'),
    
    
    # Returning form as HTTP response
    path('simpleform/',views.simpleform),
    # HTML forms with Django Templates
    path('templateform/',views.templateform),
    # Django forms
    path('djangoform/',views.formDjango),
    
    
    
    
]