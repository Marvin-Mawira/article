from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm  
from django.core.paginator import Paginator

# List all articles
def article_list(request):
    articles = Article.objects.all()  # Get all articles
    paginator = Paginator(articles, 6)  # Show 6 articles per page

    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the page object

    return render(request, 'articles/article_list.html', {'page_obj': page_obj})

# Display article details
def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

# Create new article
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # Ensure request.FILES is included for image upload
        if form.is_valid():
            form.save()  # Save the new article
            return redirect('article_list')
    else:
        form = ArticleForm()

    return render(request, 'articles/article_form.html', {'form': form})

# Update existing article
def article_update(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)  # Handle file upload and update
        if form.is_valid():
            form.save()  # Save the updated article
            return redirect('article_detail', slug=article.slug)  # Redirect to the article detail page
    else:
        form = ArticleForm(instance=article)

    return render(request, 'articles/article_form.html', {'form': form, 'article': article})

# Delete an article
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()  # Delete the article
        return redirect('article_list')
    return render(request, 'articles/article_confirm_delete.html', {'article': article})
