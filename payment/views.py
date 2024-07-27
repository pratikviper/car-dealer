
# Create your views here.
from django.shortcuts import render, redirect
from .forms import PaymentForm

def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('thank_you_page')  # Redirect to a thank-you page

    else:
        form = PaymentForm()

    return render(request, 'pages/payment_form.html', {'form': form})
