from django import forms

class ContactForm(forms.Form):
	"""docstring for ContactForm"""
	full_name = forms.CharField()
	email = forms.EmailField()
	content = forms.CharField(widget=forms.Textarea)

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		print(email)
		if email.endswith(".edu"):
			raise forms.ValidationError("This is not a valid email. Please dont use .edu")
		return email
