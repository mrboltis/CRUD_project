from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ("emp_code", "position", "fullname", "mobile")
        labels = {
            
            'fullname':'Фамилия Имя Отчество',
            'emp_code' : 'Код сотрудника',
            'position':'Должность',
            'mobile':'Телефон'
            
            
        }
        
    def __init__(self,*args,**kwargs):
        super(EmployeeForm, self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "- Выберите -"
        self.fields['emp_code'].required = False