#from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render

#def devtool_list(request):
 #   return render(request, 'devtools/list.html')

#def devtool_detail(request, pk):
  #  return render(request, 'devtools/detail.html', {'pk': pk})

#def devtool_create(request):
  #  return render(request, 'devtools/create.html')

#def devtool_update(request, pk):
  #  return render(request, 'devtools/update.html', {'pk': pk})

#def devtool_delete(request, pk):
   # return render(request, 'devtools/delete.html', {'pk': pk})


from django.shortcuts import render, get_object_or_404, redirect
from devtools.models import DevTool
from devtools.forms import DevToolForm

def devtool_list(request):
    devtools = DevTool.objects.all()
    return render(request, 'devtools/list.html', {'devtools': devtools})

def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    return render(request, 'devtools/detail.html', {'devtool': devtool})

def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devtool_list')
    else:
        form = DevToolForm()
    return render(request, 'devtools/create.html', {'form': form})

def devtool_update(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            form.save()
            return redirect('devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm(instance=devtool)
    return render(request, 'devtools/update.html', {'form': form})

def devtool_delete(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        devtool.delete()
        return redirect('devtool_list')
    return render(request,  {'devtool': devtool})
