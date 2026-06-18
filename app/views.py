from django.shortcuts import render,redirect,get_object_or_404
from .models import BlogApp,TopAnime,TopMovies
from .models import UserFormModel

def home(request):
    all_posts = BlogApp.objects.filter(status="Published")
    slider_posts = BlogApp.objects.filter(status="Published").order_by('-id')[:3]
    context = {
        'ratul':all_posts,
        'sliders':slider_posts
        
    }
  
    
    return render(request, 'Anime.html',context)


# new function for different pages details.It can get data to database and send to url link




def post_detail(request,slug):
    
      # ডাটাবেস থেকে নির্দিষ্ট আইডির পোস্টটি তুলে আনা হচ্ছে
      
    current_post = get_object_or_404(BlogApp, slug=slug)
    
    
    # ২. টাইটেল থেকে সিরিজ বা নাম আলাদা করার একদম সেফ লজিক
    title_words = current_post.title.split()
    series_name = ""
    
    # যদি টাইটেলে ২ বা তার বেশি শব্দ থাকে (যেমন: "One Piece Chapter 1184")
    if len(title_words) >= 2:
        series_name = f"{title_words[0]} {title_words[1]}"
        
    # যদি টাইটেলে মাত্র ১টি শব্দ থাকে (যেমন: "Naruto")
    elif len(title_words) == 1:
        series_name = title_words[0]
        
    # যদি টাইটেল একদম খালি থাকে
    else:
        series_name = "Anime"

    # ৩. ডাটাবেস থেকে আগের চ্যাপ্টার বা রিলেটেড পোস্ট ফিল্টার করা
    previous_chapters = BlogApp.objects.filter(
        pk__lt=current_post.pk, 
        category=current_post.category,
        title__icontains=series_name, 
        status="Published"
    ).order_by('-pk')[:2]
    
    # ৪. ব্যাকআপ প্ল্যান: মিল না পাওয়া গেলে একই ক্যাটাগরির লেটেস্ট ২টি পোস্ট দেখানো
    if not previous_chapters:
        previous_chapters = BlogApp.objects.filter(
            category=current_post.category,
            status="Published"
        ).exclude(slug=slug).order_by('-pk')[:2]

    context = {
        'post': current_post,
        'previous_chapters': previous_chapters
    }
    return render(request, 'post_detail.html', context)


def category_view(request,cat_name):
        # ডাটাবেস থেকে শুধু ওই নির্দিষ্ট ক্যাটাগরির পোস্টগুলো ফিল্টার করে আনা হচ্ছে
        
        filtered_posts = BlogApp.objects.filter(category = cat_name,status="Published")
        context = {
            'category_name': cat_name,
            'posts': filtered_posts
        }
        return render(request, 'category_posts.html', context)



def about_view(request):
    return render(request,'about.html',)


def top_anime(request):
    # ডাটাবেস থেকে র্যাংক অনুযায়ী সিরিয়ালি সব টপ এনিমে নিয়ে আসা হলো
    top_list = TopAnime.objects.all().order_by('rank')
    
    # আপনার টেমপ্লেটের নাম যেহেতু 'top_anime.html' এবং আমরা ডাটা পাঠাচ্ছি 'top_list' নামে
    return render(request, 'top_anime.html', {'top_list': top_list})


def top_movies(request):
    # ডাটাবেস থেকে র্যাংক অনুযায়ী সিরিয়ালি সব টপ movies নিয়ে আসা হলো
    top_movies = TopMovies.objects.all().order_by('rank')
    
    # আপনার টেমপ্লেটের নাম যেহেতু 'top_movies.html' এবং আমরা ডাটা পাঠাচ্ছি 'top_list' নামে
    return render(request, 'top_movies.html', {'top_movies': top_movies})




def submit_form(request):
    if request.method =="POST":
        
        # data get from user from
        
        user_name = request.POST.get('fName')
        user_email = request.POST.get('fEmail')
        user_pass = request.POST.get('fPassword')
        
        # make object to save data
        UserFormModel.objects.create(
            name = user_name,
            email = user_email, 
            password =  user_pass 
        )

        return redirect('/')
    return render(request,'form.html')

