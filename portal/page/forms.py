from django import forms
from ckeditor.widgets import CKEditorWidget
from page.models import Page

class NewPageForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
	content = forms.CharField(widget=CKEditorWidget())
	files = forms.FileField(widget=forms.ClearableFileInput(), required=False)
	# To handle multiple files, process request.FILES.getlist('files') in your view.

	class Meta:
		model = Page
		fields = ('title', 'content', 'files')