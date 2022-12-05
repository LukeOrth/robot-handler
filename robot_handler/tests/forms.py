from django import forms

class RefreshTests(forms.Form):
    refresh_tests = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class RobotLocation(forms.Form):
    robot_location = forms.CharField(widget=forms.HiddenInput)