# Django Blog
This is a Blog Application Created using Django Framework along with Bootstrap and CSS.  
It Supports the Following Functionality

*   Create, Update and Delete Posts
*   Edit/Update User Profile
*   Sort Blogs by User
*   Social Login Via Google

Notable Technologies/Frameworks

*   Python - Django Framework
*   HTML5 and CSS
*   Bootstrap
*   SocialAuth - Google OAUTH
*   Amazon S3 Storage

This website has been deployed using

*   Amazon EC2 Instance
*   Apache2

Github Repository for this project can be found [here](https://github.com/dpsingh287/blogapp-django)  
The Deployed website can be accessed [here](http://ec2-65-1-108-97.ap-south-1.compute.amazonaws.com/)

## Running Locally

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:dpsingh287/blogapp-django.git
    $ cd blogapp-django
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
    
## Screenshots
![image](https://user-images.githubusercontent.com/83512136/208237708-bdf5d3a7-f150-4552-9665-91f6196de6fa.png)
![image](https://user-images.githubusercontent.com/83512136/208237727-998938ba-2071-43ed-9cd7-61b19210a468.png)
![image](https://user-images.githubusercontent.com/83512136/208237763-f76dd300-3014-4613-9bd8-f0acea446872.png)
