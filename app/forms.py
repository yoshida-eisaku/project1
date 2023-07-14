from django import forms
from .models import Item

# 入力フォームの形作り
class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'phone', 'jan','product', 'staff','setcardID','memo')
        width = {
                    'name':forms.TextInput(attrs={'placeholder':'記入例：山田　太郎'}),
                    'phone':forms.TextInput(attrs={'placeholder':'0x0xxxxxxxx'}),
                    'jan':forms.TextInput(attrs={'placeholder':'janコード4996774000000'}),
                    'product':forms.TextInput(attrs={'placeholder':'商品名'}),
                    'staff':forms.TextInput(attrs={'placeholder':'担当者名'}),
                    'setcardID':forms.TextInput(attrs={'placeholder':'カードID'}),
                    'memo':forms.TextInput(attrs={'placeholde':'備考欄'}),
        }

class ExcelFileUploadForm(forms.Form):
    excel_file = forms.FileField()


class RunTestsForm(forms.Form):
    # Add form fields here as needed
    test_input = forms.CharField(label='Test Input', max_length=100)