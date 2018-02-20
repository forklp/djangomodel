from django import forms

class ContactForm(forms.Form):
    CITY =(
        ('TP', 'Taipei'),
        ('TC', 'Taichung'),
    )
    user_name = forms.CharField(label='您的名字', max_length=50, initial='李四')
    user_city = forms.ChoiceField(label='居住城市', choices=CITY)
    user_school = forms.BooleanField(label='是否在学', required=False)
    user_email = forms.EmailField(label='您的电子邮件')
    user_message = forms.CharField(label='您的意见', widget=forms.Textarea)