from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, Textarea
from .models import Profile

class MySignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'email']

    biography = CharField(label='Biography', widget=Textarea(attrs={'placeholder':'Tell us your story with movies'}), min_length=40)


    @atomic
    def save(self, commit=True):
        # self.instance.is_active = False
        result = super().save(commit)
        written_bio = self.cleaned_data['biography']
        profile = Profile(biography=written_bio, user=result)
        if commit:
            profile.save()
        return result