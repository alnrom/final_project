from django.db import models

# Create your models here.
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(help_text="Current stock amount")
    unit = models.CharField(max_length=20, help_text="e.g., grams, liters, units, tbsp")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='menu_items/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class RecipeRequirement(models.Model):
    # Links the MenuItem to its Ingredients
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="requirements")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(help_text="Amount needed for this specific dish")

    def __str__(self):
        return f"{self.quantity} {self.ingredient.unit} of {self.ingredient.name} for {self.menu_item.title}"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=True, default=1)

    def __str__(self):
        return f"{self.menu_item.title} purchased at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"