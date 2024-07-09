# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Booking

# class UserSignupForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# class BookingForm(forms.ModelForm):
#     start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
#     end_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

#     class Meta:
#         model = Booking
#         fields = ['slot', 'start_time', 'end_time']


from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class BookingForm(forms.ModelForm):
    start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Booking
        fields = ['slot', 'start_time', 'end_time']

    def clean(self):
        cleaned_data = super().clean()
        slot = cleaned_data.get('slot')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time:
            # Check if there is any existing booking for the same slot and overlapping time range
            conflicting_bookings = Booking.objects.filter(
                slot=slot,
                start_time__lt=end_time,
                end_time__gt=start_time
            )
            if conflicting_bookings.exists():
                raise ValidationError("This slot is already booked for the selected time range.")

        return cleaned_data
