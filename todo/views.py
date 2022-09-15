from django.shortcuts import render, redirect, get_object_or_404
from .models import Items
from .forms import ItemsForm

# Create your views here.


def get_todo_list(request):
    items = Items.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
        # name = request.POST.get('item_name')
        # done = 'done' in request.POST
        # Items.objects.create(name=name, done=done)

    form = ItemsForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):

    item = get_object_or_404(Items, id=item_id)
    if request.method == 'POST':
        form = ItemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemsForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    item.done = not item.done
    item.save()   
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    item.delete()
    return redirect('get_todo_list')
