from django import forms


class StockSearchForm(forms.Form):
    export_to_CSV = forms.BooleanField(required=False)
