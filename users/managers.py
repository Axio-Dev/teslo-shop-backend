from django.contrib.auth.models import UserManager

class UserManager(UserManager):
    use_in_migrations = True

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        
        extra_fields.setdefault("role", "user")
        email = self.normalize_email(email)

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("role", "superuser")
        return self.create_user(username=username, email=email, password=password, **extra_fields)