from rest_framework import viewsets

from .models import Books
from .serializers import BooksSerializer
# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('title', 'author','description')
    serializer_class = BooksSerializer