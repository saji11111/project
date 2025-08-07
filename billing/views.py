from django.shortcuts import render, redirect
from .forms import BillForm, BillFilterForm
from .models import Bill

def billing_main(request):
    """
    Renders the main room management page, which will contain links
    to other room-related functionalities.
    """
    # No POST handling needed here, as it's just a navigation page
    return render(request, 'billing_main.html', {}) # Pass an empty context dictionary for now

def create_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_bills')
    else:
        form = BillForm()
    return render(request, 'create_bill.html', {'form': form})

def view_bills(request):
    bills = Bill.objects.all().order_by('-date_created')
    form = BillFilterForm(request.GET or None)

    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        paid_status = form.cleaned_data.get('paid_status')

        if start_date:
            bills = bills.filter(date_created__date__gte=start_date)
        if end_date:
            bills = bills.filter(date_created__date__lte=end_date)
        if paid_status == 'paid':
            bills = bills.filter(paid=True)
        elif paid_status == 'unpaid':
            bills = bills.filter(paid=False)

    return render(request, 'view_bills.html', {'bills': bills, 'form': form})
