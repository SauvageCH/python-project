from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, ContactForm
from .models import Contact, CustomUser
from django.contrib.auth.decorators import login_required

# vue de connexion


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        phone = form.cleaned_data["phone_number"]
        password = form.cleaned_data["password"]
        user = authenticate(request, phone_number=phone, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            form.add_error(None, "Numéro ou mot de passe incorrect")
    return render(request, "contacts/login.html", {"form": form})

# vue principale après connexion
@login_required
def dashboard(request):
    contacts = Contact.objects.filter(user=request.user)
    category = request.GET.get('category')
    search = request.GET.get('search')

    # filtrage
    if category:
        contacts = contacts.filter(category=category)

    # recherche
    if search:
        contacts = contacts.filter(phone_number__icontains=search)

    return render(request, 'contacts/dashboard.html', {'contacts': contacts})

# ajout ou édition de contact
@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('dashboard')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

# suppression de contact
@login_required
def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id, user=request.user)
    if request.method == 'POST':
        contact.delete()
        return redirect('dashboard')
    return render(request, 'contacts/delete_confirm.html', {'contact': contact})
