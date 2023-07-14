from django_filters import filters
from django_filters import FilterSet
from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s (降順) '

# フィルター設定　フォーム内検索の設定
class ItemFilter(FilterSet):

    name = filters.CharFilter(label='氏名',lookup_expr='contains')
    memo = filters.CharFilter(label='備考',lookup_expr='contains')
    product = filters.CharFilter(label='商品名',lookup_expr='contains')
    phone = filters.CharFilter(label='電話番号',lookup_expr='contains')
    staff = filters.CharFilter(label='担当者名',lookup_expr='contains')
    cardID = filters.CharFilter(label='カードID',lookup_expr='contains')
    jan = filters.CharFilter(label='janコード',lookup_expr='contains')

    order_by = MyOrderingFilter(

        fields=(
            ('name', 'name'),
            ('memo'),('memo'),
            ('product'),('product'),
            ('phone'), ('phone'),
            ('staff'), ('staff'),
            ('cardID'), ('cardID'),
            ('jan'), ('jan'),
        ),
        field_labels={
            'name': '氏名',
            'product': '商品名',
            'memo': '備考',
            'phone': '電話番号',
            'staff': '担当者',
            'cardID': 'カードID',
            'jan':'janコード',
        },
        label='並び順'
    )
    


    class Meta:
        model = Item
        fields = ('name','phone','product','memo','jan','staff','cardID')