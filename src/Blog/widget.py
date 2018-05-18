import re
from django import forms
from django.conf import settings
from django.template.loader import render_to_string

class CountTextInput(forms.TextInput):
    template_name = 'widgets/count_text.html'

# 텍스트 자동생성 위젯
class AutoCompleteWidget(forms.Select):
    template_name = 'widgets/autocomplete_select.html'

    class Media:
        css = {
            'all': [
                'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/css/select2.min.css'
            ],
        }
        js = [
            'https://code.jquery.com/jquery-3.3.1.js',
            'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/js/select2.min.js'
        ]

    # ajax_url 파라미터를 받아오기
    def __init__(self, ajax_url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ajax_url = ajax_url

    # ajax_url을 템플릿으로 넘겨주기
    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        context['ajax_url'] = self.ajax_url
        return context

    # 관리자 페이지에 초기 리스트를 불러오는 것 방지
    def optgroups(self, name, value, attrs=None):
        existed_ids = [_id for _id in value if _id]
        self.choices.queryset = self.choices.queryset.filter(id__in=existed_ids)
        return super().optgroups(name, value, attrs=None)

    # 스타일 정해주기
    def build_attrs(self, *args, **kwargs):
        context = super().build_attrs(*args, **kwargs);
        context['style'] = 'min-width:250px;'
        return context

# 네이버 지도 위젯

class NaverMapPointWidget(forms.TextInput):
    BASE_LAT, BASE_LNG = '37.497921', '127.027636' # 강남역
    class Media:
        css = {
            'all': [
                "https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"
            ],
        }
    def render(self, name, value, attrs):
        width = str(self.attrs.get('width', 600))
        height = str(self.attrs.get('height', 600))
        if width.isdigit() : width += 'px'
        if height.isdigit() : height += 'px'

        context = {'naver_client_id' : settings.NAVER_CLIENT_ID,
                   'id':attrs['id'], # 현재 formfield의 html id
                   'width':width, 'height':height,
                   'base_lat':self.BASE_LAT, 'base_lng':self.BASE_LNG}

        if value:
            try:
                lng, lat = re.findall(r'[+-]?[\d\.]',value)
                context.update({'base_lat':lat, 'base_lng':lng})
            except (IndexError, ValueError):
                pass

        attrs['readonly'] = 'readonly'
        parent_html = super().render(name, value, attrs)

        html = render_to_string('widgets/naver_map_point_widget.html', context)

        return parent_html + html