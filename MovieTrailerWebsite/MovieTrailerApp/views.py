from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class vwIndex(TemplateView):
    """Create the view vwIndex that loads index.html."""

    # Start the Home view that loads index.html
    def get(self, request, **kwargs):
        """Create the view vwIndex that loads index.html."""
        return render(request, 'index.html', context=None)
