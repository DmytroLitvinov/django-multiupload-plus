Django Multiupload Plus ⏩
==========================

**🍴 This is a forked and updated version based on original library [django-multiupload](https://github.com/Chive/django-multiupload).**

> *As for 31.12.2024 nobody took responsibility, so I decided to take it since we need that fix in one of our project.*

Dead simple drop-in multi file upload field for django forms using HTML5's ``multiple`` attribute.

To keep Django ecosystem fresh and updated, please share your love and support, click `Star` 🫶

## Installation

* Install the package using `pip` 

```bash
$ pip install django-multiupload-plus
```

## Usage

Add the form field to your form and make sure to save the uploaded files in the form's ``save`` method.

For more detailed examples visit the [examples section](https://github.com/DmytroLitvinov/django-multiupload-plus/tree/master/examples).


```python
# forms.py
from django import forms
from multiupload_plus.fields import MultiFileField, MultiMediaField, MultiImageField

class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    # If you need to upload media files, you can use this:
    attachments = MultiMediaField(
        min_num=1,
        max_num=3,
        max_file_size=1024*1024*5,
        media_type='video'  # 'audio', 'video' or 'image'
    )

    # For images (requires Pillow for validation):
    attachments = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)
```

The latter two options just add fancy attributes to HTML's `<input>`, restricting the scope to corresponding filetypes.

```python
# models.py
from django.db import models

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments')

```

```python
# views.py
from django.views.generic.edit import FormView
from .forms import UploadForm
from .models import Attachment

class UploadView(FormView):
    template_name = 'form.html'
    form_class = UploadForm
    success_url = '/done/'

    def form_valid(self, form):
        for each in form.cleaned_data['attachments']:
            Attachment.objects.create(file=each)
        return super().form_valid(form)

```
