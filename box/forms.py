from django import forms
'''
name = models.CharField(max_length=50)
bio = models.TextField(null=True, blank=True)

title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)
    time_required = models.CharField(max_length=30)
    instructions = models.TextField(null=False, blank=False)
'''


class AddAuthorForm(forms.Form):
    pass


class AddRecipeForm(forms.form):
    class AddRecipeForm(forms.Form):
        title = forms.CharField(max_length=50)
        author = forms.ModelChoiceField(queryset=Author.objects.all())
        description = forms.CharField(max_length=50)
        time_required = forms.CharField(max_length=30)
        instructions = forms.CharField(widget=forms.TextInput)
