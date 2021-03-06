from django import forms


# 글자 수 세는 위젯
class CounterTextInput(forms.TextInput):
    template_name = 'widgets/counter_text.html'

# 별점
class RateitjsWidget(forms.TextInput):
    input_type = 'rating'
    template_name = 'widgets/rateitjs_number.html'

    class Meta:
        css = {
            'all': [
                'widgets/rateit.js/rateit.css',
            ],
        }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            'widgets/rateit.js/jquery.rateit.min.js',
        ]

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs.update({
            'min': 0,
            'max': 5,
            'step': 1,
        })

class AutoCompleteWidget(forms.Select):
    template_name = 'widgets/autocomplete_select.html'

    class Meta:
        css = {
            'all': [
                '// cdnjs.cloudflare.com / ajax / libs / select2 / 4.0.5 / css / select2.min.css',
            ],
        }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.5/js/select2.min.js',
        ]

    def build_attrs(self, *args, **kwargs):
        context = super().build_attrs(*args, **kwargs)
        context['style'] = 'min-width :200px;'
        return context