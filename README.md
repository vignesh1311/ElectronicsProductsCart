# ElectronicsProductsCart

Download the Code to local

Then open the project in your IDE

Install below modules
    Django
    django-cors-headers 
    djangorestframework 
    django-rest-knox  
    django_rest_passwordreset
    
Then do migrations by running below comments in cmd 
    python manage.py makemigrations  
    python manage.py migrate   
    
Start the Server
    python manage.py runserver   
    
Visit below sites to do Crud and login logout operations

http://127.0.0.1:8000/electronic-items for get and post methods
http://127.0.0.1:8000/electronic-items/<item-id> for patch and delete
http://127.0.0.1:8000/api/register for user registration
http://127.0.0.1:8000/api/login for user login
http://127.0.0.1:8000/api/logout for user logout
