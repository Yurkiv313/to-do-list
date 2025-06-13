from django import forms
from tasks.models import Tag, Task


class TaskCreationForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        exclude = ["is_done"]
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "What needs to be done?"
            }),
        }
        help_texts = {
            "deadline": "Format: YYYY-MM-DD HH:MM (e.g. 2025-04-15 14:30)",
        }
