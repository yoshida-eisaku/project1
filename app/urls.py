from django.urls import path
from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView,ExcelFileUploadView,run_tests_view
#from .views import ItemSerchView

urlpatterns = [
    # 一覧画面
    path('',  ItemFilterView.as_view(), name='index'),
    # 詳細画面
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    # 登録画面
    path('create/', ItemCreateView.as_view(), name='create'),
    # 更新画面
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    # 削除画面
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    #商品入荷調査画面
    # path('inspection/',ItemInspectionView.as_view(),name='inspection'),
    path('upload/',ExcelFileUploadView.as_view(), name='upload'),
    #path('search/',ItemSerchView.as_view(),name='search')
    path('run_tests/', run_tests_view, name='run_tests'),
]

