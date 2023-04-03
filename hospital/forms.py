from django import forms

from .models import Booking, Contact

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


        widgets = {
            'booking_date': DateInput()
        }

        labels ={
            'doc_name': "Doctor Name: ",
            'p_name': "Patient Name: ",
            'p_phone': "Patient Phone: ",
            'p_email' : "Patient Email:",
            'booking_date' : "Booking Date"
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
                    