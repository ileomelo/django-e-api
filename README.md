# Recipe Recipe

Recipe Recipe is a comprehensive web application where users can register, share, and discover recipes. Built using Django and Django REST Framework (DRF), RecipeHub provides a seamless experience for users to create, authenticate, and manage their recipes, while administrators can oversee recipe submissions and maintain the integrity of the platform.

## Key Features:

- **User Registration and Authentication:** Users can register accounts securely and authenticate using JSON Web Tokens (JWT), ensuring a smooth and secure login process.

- **Recipe Creation and Submission:** Registered users can create and submit their own recipes to be reviewed by administrators before being published on the platform.

- **Admin Approval Workflow:** Administrators have the ability to review and approve recipe submissions, ensuring quality control and adherence to community guidelines before recipes are published.

- **Permission Management:** Only the creator of a recipe has permission to update or delete their own recipes, providing users with control over their content.

- **Search and Discovery:** Users can easily search for recipes using keywords, categories, or ingredients, facilitating the discovery of new and exciting dishes.

## Technologies Used:

- **Django:** A high-level Python web framework that provides a clean and pragmatic design for building web applications.

- **Django REST Framework (DRF):** A powerful toolkit for building web APIs in Django, offering serialization, authentication, and permission management capabilities.

- **JSON Web Tokens (JWT):** A standard for securely transmitting information between parties as a JSON object, used for authentication in RecipeHub.

## Setup:

1. Clone the repository from GitHub:
```
git clone https://github.com/ileomelo/django-recipe.git
```

2. Navigate to the project directory:
```
cd django-recipe
```

3. Create a new virtual environment using `venv` (or your preferred virtual environment manager):
```
python -m venv venv
```

4. Activate the virtual environment. On Windows, use:
```
venv\Scripts\activate
```
On macOS/Linux, use:
```
source venv/bin/activate
```

5. Install the required dependencies using pip:
```
pip install -r requirements.txt
```

6. Apply database migrations:
```
python manage.py migrate
```

7. Create a superuser for admin access:
```
python manage.py createsuperuser
```

8. Start the Django development server:
```
python manage.py runserver
```

9. Access the application at `http://127.0.0.1:8000/` in your web browser.

## Usage:

1. Register an account on the platform or login if you already have one.
2. Create and submit your own recipes for review by administrators.
3. Browse and discover recipes shared by other users.
4. Administrators can approve or reject recipe submissions from the admin dashboard.
