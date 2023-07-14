from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views import View

import pandas as pd
import os
import shutil
from .models import Item
from .filters import ItemFilter
from .forms import ItemForm
from.forms import ExcelFileUploadForm
from.forms import RunTestsForm


# Create your views here.
# 検索一覧画面
class ItemFilterView(LoginRequiredMixin, FilterView):
    model = Item
    filterset_class = ItemFilter
    # デフォルトの並び順を新しい順とする
    queryset = Item.objects.all().order_by('-created_at')

    # クエリ未指定の時に全件検索を行うために以下のオプションを指定（django-filter2.0以降）
    strict = False

    # 1ページあたりの表示件数
    paginate_by = 10

    # 検索条件をセッションに保存する or 呼び出す
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)


# 詳細画面
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


# 登録画面
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('index')



#エクセルファイルを読み込むようなクラスを作成したい作成したクラスの中ではwebアプリ上で
#エクエルファイルを読み込むフォームからフォルダにエクセルファイルを格納するコードを書きたい

class ExcelFileUploadView(View):
    form_class = ExcelFileUploadForm
    template_name = 'upload.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['excel_file']
            # アップロードされたファイルを指定のフォルダに保存
            file_path = os.path.join(settings.MEDIA_ROOT, excel_file.name)
            
            # フォルダ内のファイルをクリアする
            clear_folder(settings.MEDIA_ROOT)
            
            with open(file_path, 'wb') as f:
                for chunk in excel_file.chunks():
                    f.write(chunk)
            
            # ファイルの保存パスを結果として返す
            return render(request, 'result.html', {'file_path': file_path})
        
        return render(request, self.template_name, {'form': form})

def clear_folder(folder_path):
    # フォルダ内のファイルを削除する
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


import subprocess

def upload_view(request):
    return render(request, 'upload.html')

# class RunTestsView(View):
#     form_class = RunTestsForm
    
#     def get(self, request):
#         form = self.form_class()
#         return render(request, 'upload.html', {'form': form})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             result = self.run_tests()
#             return render(request, 'results.html', {'results': result})
#         else:
#             return render(request, 'upload.html', {'form': form})

    
#     def run_tests(self):
#         cmd = r"python C:\\Users\\222061\\Desktop\\practice\\prac\\project1\\tests.py"
#         result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
#         return result.stdout
def run_tests_view(request):
    cmd = "python tests.py"  # 実行したいコマンド
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return render(request, 'results.html', {'results': result.stdout})