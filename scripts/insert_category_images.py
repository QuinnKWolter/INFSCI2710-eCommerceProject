from app.models import Category
import os

for i, category in enumerate(Category.objects.all()):
    category.image = os.path.join('category_images', f'{i+1}.jpeg')
    category.save()
