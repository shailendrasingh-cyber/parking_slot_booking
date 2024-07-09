# # from django.shortcuts import render, redirect
# # from django.contrib.auth import login, authenticate
# # from django.contrib.auth.forms import AuthenticationForm
# # from .forms import UserSignupForm, BookingForm
# # from .models import Slot, Booking
# # from django.http import HttpResponse

# # def index(request):
# #     return render(request, 'index.html')

# # def signup(request):
# #     if request.method == 'POST':
# #         form = UserSignupForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             username = form.cleaned_data.get('username')
# #             raw_password = form.cleaned_data.get('password1')
# #             user = authenticate(username=username, password=raw_password)
# #             login(request, user)
# #             return redirect('booking')
# #     else:
# #         form = UserSignupForm()
# #     return render(request, 'signup.html', {'form': form})

# # def user_login(request):
# #     if request.method == 'POST':
# #         form = AuthenticationForm(request, data=request.POST)
# #         if form.is_valid():
# #             username = form.cleaned_data.get('username')
# #             password = form.cleaned_data.get('password')
# #             user = authenticate(username=username, password=password)
# #             if user is not None:
# #                 login(request, user)
# #                 return redirect('booking')
# #     else:
# #         form = AuthenticationForm()
# #     return render(request, 'login.html', {'form': form})

# # def booking(request):
# #     if request.method == 'POST':
# #         form = BookingForm(request.POST)
# #         if form.is_valid():
# #             booking = form.save(commit=False)
# #             booking.user = request.user
# #             booking.save()
# #             return redirect('ticket', booking_id=booking.id)
# #     else:
# #         form = BookingForm()
# #     return render(request, 'booking.html', {'form': form})

# # def ticket(request, booking_id):
# #     booking = Booking.objects.get(id=booking_id)
# #     return render(request, 'ticket.html', {'booking': booking})


# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import AuthenticationForm
# from .forms import UserSignupForm, BookingForm
# from .models import Slot, Booking
# from django.http import HttpResponse

# def index(request):
#     return render(request, 'index.html')

# def signup(request):
#     if request.method == 'POST':
#         form = UserSignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('booking')
#     else:
#         form = UserSignupForm()
#     return render(request, 'signup.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('booking')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def booking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.user = request.user
#             booking.save()
#             return redirect('ticket', booking_id=booking.id)
#     else:
#         form = BookingForm()
#     return render(request, 'booking.html', {'form': form})

# def ticket(request, booking_id):
#     booking = Booking.objects.get(id=booking_id)
#     return render(request, 'ticket.html', {'booking': booking})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserSignupForm, BookingForm
from .models import Slot, Booking

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('booking')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('booking')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('ticket', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def ticket(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'ticket.html', {'booking': booking})
