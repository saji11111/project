from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} ({'Available' if self.available else 'Occupied'})"

class RoomAllocation(models.Model):
    patient_id = models.CharField(max_length=20)
    patient_name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    allocated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - Room {self.room.room_number}"