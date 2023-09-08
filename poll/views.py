from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from poll.models import Score, Article
# from .views update_view
# Create your views here.


def index(request):
    score_intsance = Score.objects.get(id=1)
    score_value = score_intsance.score
    all_posts = Article.objects.all()
    return render(request, 'poll/index.html', {'score' : score_value, 'all_posts': all_posts })

@login_required
def update_poll(request, id):
    if Score.objects.filter(voter=request.user).exists():
        return redirect('index')
    else:
        score_intsance = Score.objects.get(id=1)
        score_value = score_intsance.score


        if request.method == 'POST':
            action = request.POST.get('action')

            if action == 'increment_btn':
                score_intsance.increment(request.user)
                score_value = score_intsance.score
                return redirect("index")

            if action == 'decrement_btn':
                score_intsance.decrement(request.user)
                score_value = score_intsance.score
                return redirect("index")
            

        return render(request, 'poll/index.html', {'score' : score_value})



    