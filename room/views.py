from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, RoomAllocation
from .forms import RoomForm, RoomAllocationForm

def room_main(request):
    """
    Renders the main room management page, which will contain links
    to other room-related functionalities.
    """
    # No POST handling needed here, as it's just a navigation page
    return render(request, 'room_main.html', {}) # Pass an empty context dictionary for now

def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('available_rooms')
    else:
        form = RoomForm()
    return render(request, 'add_room.html', {'form': form})

def available_rooms(request):
    rooms = Room.objects.filter(available=True)
    return render(request, 'available_rooms.html', {'rooms': rooms})

def allocate_room(request):
    if request.method == 'POST':
        form = RoomAllocationForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room']
            if room.available:
                room.available = False
                room.save()
                form.save()
                return redirect('available_rooms')
    else:
        form = RoomAllocationForm()
    return render(request, 'allocate_room.html', {'form': form})

def discharge_patient(request, pk):
    allocation = get_object_or_404(RoomAllocation, pk=pk)
    room = allocation.room
    room.available = True
    room.save()
    allocation.delete()
    return redirect('available_rooms')

def allocated_rooms(request):
    allocations = RoomAllocation.objects.select_related('room').all()
    return render(request, 'allocated_rooms.html', {'allocations': allocations})
