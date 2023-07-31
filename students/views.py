from django.shortcuts import render, redirect
from students.forms import StudentsForm
from students.models import Students


# Create your views here.
def home(request):
    return render(request, "home.html")


def std(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/view")
            except:
                pass
    else:
        form = StudentsForm()
    return render(request, "index.html", {"form": form})


def view(request):
    students = Students.objects.all()
    return render(request, "view.html", {"students": students})


def delete(request, id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect("/view")


def edit(request, id):
    students = Students.objects.get(id=id)
    return render(request, "edit.html", {"students": students})


def update(request, id):
    f_name = request.POST.get("f_name")
    l_name = request.POST.get("l_name")
    email = request.POST.get("email")

    students = Students.objects.get(id=id)
    students.f_name = f_name
    students.l_name = l_name
    students.email = email

    students.save()
    return redirect("/view")
