from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#créer utilisateurs normaux et superutilisateurs
class CustomUserManager(BaseUserManager):
    #créer utilisateur
    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Crée et enregistre un utilisateur avec le numéro de téléphone et mot de passe donnés.
        """
        if not phone_number:  # Vérifie input telephone
            raise ValueError("Ecrivez votre numéro de téléphone !!!!")
        
        # crée & enregistre l'instance utilisateur
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)  #hash le mdp ( normalement ..)
        user.save(using=self._db)  # database saving
        return user

    #créer utilisateur admin (superuser)
    def create_superuser(self, phone_number, password=None, **extra_fields):
        # Définit automatiquement les droits admin
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        return self.create_user(phone_number, password, **extra_fields)

#on utilise ce modèle peros a la place du modele de Django fournie juste pour une 
#bonne structure
class CustomUser(AbstractBaseUser, PermissionsMixin):
#AbstractBaseUser et PermissionsMixin sont des modules Django qui gèrent les permissions et le login

    phone_number = models.CharField(max_length=15, unique=True)  
    is_active = models.BooleanField(default=True)  # si le compte est activé
    is_staff = models.BooleanField(default=False)  # si l'user a accès à l'admin

    # Champ utilisé pour la connexion
    USERNAME_FIELD = "phone_number"
    # SI on voulait créer d'autres superusers on les stock ici
    REQUIRED_FIELDS = []

    # Lie ce modèle à son gestionnaire personnalisé
    objects = CustomUserManager()

    def __str__(self):
        """Représentation de l'utilisateur"""
        return self.phone_number


# modèle pour stocker les contacts des utilisateurs
class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('domicile', 'Domicile'),
        ('professionnel', 'Professionnel'),
        ('mobile', 'Mobile'),
    ]
    # Lien vers l'utilisateur propriétaire du contact
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # nom 
    email = models.EmailField()  # email 
    phone_number = models.CharField(max_length=20)  # telephone
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  #categorie

    def __str__(self):
        """Affichage du contact"""
        return self.name