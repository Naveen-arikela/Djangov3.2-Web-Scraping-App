from django import forms

class ScraperForm(forms.Form):
    domain_url = forms.CharField(label='Enter your website url', required=True)
    container_tag = forms.CharField(label='Enter your container tag', required=True)
    tags = forms.CharField(label='Enter your tags', required=True)
    output_filename = forms.CharField(label='Enter your output filename', required=True)
