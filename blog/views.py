from django.shortcuts import render,redirect,HttpResponse
from .models import Post,Comment
from django.contrib import messages
from django.urls import reverse
from .forms import PostForm
# Create your views here.
def blogHome(request):
    allpost = Post.objects.all()
    context = {"allposts": allpost}
    return render(request, "blog/home.html",context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    Comments = Comment.objects.filter(post=post).all()
    context = {"post": post,
               'comments': Comments}
    return render(request, "blog/post.html",context)

def postComment(request):
    if request.method == "POST":
        content = request.POST.get('content')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.filter(sno=postSno).first()
        if user.is_authenticated:
            if content:
                comment = Comment(commentContent=content, user=user, post=post)
                comment.save()
                messages.success(request,"Your comment has been posted")
            else:
                messages.error(request,"Cannot post empty comment")
        else:
            messages.error(request,"Create or  Log-in to a Account to post a comment")
    return redirect(f'/blog/{post.slug}')

def postblog(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.slug = post.title.replace(" ","-").lower()
           post.save()
           messages.success(request,"Your post has been posted successfully")
           return redirect('blogHome')
        else:
            messages.error(request,"Unable to post your Blog")
    else:
        form = PostForm()
    return render(request,'blog/postblog.html',{'form':form})