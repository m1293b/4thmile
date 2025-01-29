# Table of content:

## UX

- User stories
- Design choices
- Business goals
- Developer goals
- Wireframes
- Data schema

## Features

- Existing features
- Features left to be implemented

## Technologies used

## Bugs

## Testing

- Testing with validators
- Manual testing
- Room category selection
- Add extras

## Credits

- Content
- Media
- Code

## Deployment

# UX

- ## User stories

  ### As a new parent or guardian

  - **I want** to easily browse and purchase high-quality baby clothes and toys.
  - **So that** I can ensure my child has the best products.

  ### As an experienced online shopper

  - **I want** a smooth and secure checkout process.
  - **So that** I can complete purchases quickly without concerns about security.

  ### As a parent looking for specific items

  - **I want** to sort products by type (clothes or toys), name and price.
  - **So that** I can find the most suitable products for my baby's needs efficiently.

  ### As someone interested in deals

  - **I want** to see current promotions or discounts on items.
  - **So that** I can save money while purchasing quality products.
  
  ### As a returning customer

  - **I want** to be able to register my account and save my details.
  - **So that** I can purchase products without the need of typing in my details.

  ### As a registered customer

  - **I want** to be able to keep track of my orders.
  - **So that** I can easily check the status of my orders and manage them efficiently.

- ## Design choices

  I chose a warm color palette to create a welcoming atmosphere. The use of the Tailwind framework enabled me to build a responsive and fast-loading website, enhancing user experience across all devices.

- ## Wireframes

| **index.html** | **products.html** | **cart.html** |
|----------------|--------------------|---------------|

- ## Design choices

  I quite like the dark blue and it goes well with the curved edges. I used the Tailwind framework as it allowed me to quickly and efficiently build a responsive website. As the CSS file is compact, loading times are faster as well.

- ## Wireframes

| **index.html** | **home.html** | **recipes.html** |
|----------------|---------------|------------------|
| ![A picture of the index.html desktop version.](./readme_files/wireframe_index_desktop_tablet.png "Desktop version of index.html") | ![A picture of the home.html desktop version.](./readme_files/wireframe_home_desktop_tablet.png "Desktop version of hotel.html") | ![A picture of the recipes.html desktop version.](./readme_files/wireframe_recipes_desktop_tablet.png "Desktop version of recipes.html") |
| ![A picture of the index.html tablet version.](./readme_files/wireframe_index_desktop_tablet.png "Tablet version of index.html") | ![A picture of the home.html tablet version.](./readme_files/wireframe_home_desktop_tablet.png "Tablet version of home.html") | ![A picture of the recipes.html tablet version.](./readme_files/wireframe_recipes_desktop_tablet.png "Tablet version of recipes.html") |
| ![A picture of the index.html mobile version.](./readme_files/wireframe_index_mobile.png "Mobile version of index.html") | ![A picture of the home.html mobile version.](./readme_files/wireframe_home_mobile.png "Mobile version of home.html") | ![A picture of the recipes.html mobile version.](./readme_files/wireframe_recipes_mobile.png "Mobile version of recipes.html") |


| **my_recipes.html** | **sign_in.html** | **sign_up.html** |
|---------------------|------------------|------------------|
| ![A picture of the my_recipes.html desktop version.](./readme_files/wireframe_my_recipes_desktop_tablet.png "Desktop version of my_recipes.html") | ![A picture of the sign_in.html desktop version.](./readme_files/wireframe_sign_in_desktop_tablet.png "Desktop version of sign_in.html") | ![A picture of the sign_up.html desktop version.](./readme_files/wireframe_sign_up_desktop_tablet.png "Desktop version of sign_up.html") |
| ![A picture of the my_recipes.html tablet version.](./readme_files/wireframe_my_recipes_desktop_tablet.png "Tablet version of my_recipes.html") | ![A picture of the sign_in.html tablet version.](./readme_files/wireframe_sign_in_desktop_tablet.png "Tablet version of sign_in.html") | ![A picture of the sign_up.html tablet version.](./readme_files/wireframe_sign_up_desktop_tablet.png "Tablet version of sign_up.html") |
| ![A picture of the my_recipes.html mobile version.](./readme_files/wireframe_my_recipes_mobile.png "Mobile version of my_recipes.html") | ![A picture of the sign_in.html mobile version.](./readme_files/wireframe_sign_in_mobile.png "Mobile version of sign_in.html") | ![A picture of the sign_up.html mobile version.](./readme_files/wireframe_sign_up_mobile.png "Mobile version of sign_up.html") |


## Database Schema

This project uses a relational database to manage `Users` and `Recipes`. Below is a detailed description of the data schema for each table and the relationships between them.

### Users Model (`users`)

| **Column Name**   | **Data Type**   | **Constraints**                      | **Description**                                                |
|-------------------|-----------------|--------------------------------------|----------------------------------------------------------------|
| `user_id`         | `Integer`       | `Primary Key`, `Auto Increment`      | Unique identifier for each user.                               |
| `username`        | `String`        | `Unique`, `Not Null`                 | User's chosen username, must be unique.                        |
| `password_hash`   | `String`        | `Not Null`                           | Hashed password for secure storage.                            |
| `email_address`   | `String`        | `Not Null`                           | User's email address, required for communication.              |
| `points`          | `Integer`       |                                      | User's points, representing rewards or system credit.          |
| `liked_recipes`   | `ARRAY(Integer)`|                                      | Array of `recipe_id`s that the user has liked.                 |
| `admin`           | `Boolean`       |                                      | Flag indicating if the user has admin privileges. To be implemented|

#### Relationships:
- **One-to-Many with Recipes**: A user can create multiple recipes. This relationship is facilitated by the `user_id` foreign key in the `recipes` table, which references the `user_id` in the `users` table.

---

### Recipes Model (`recipes`)

| **Column Name**     | **Data Type**     | **Constraints**                     | **Description**                                                |
|---------------------|-------------------|-------------------------------------|----------------------------------------------------------------|
| `recipe_id`         | `Integer`         | `Primary Key`, `Auto Increment`     | Unique identifier for each recipe.                             |
| `recipe_name`       | `String(20)`      | `Unique`, `Not Null`                | Name of the recipe, must be unique and less than 20 characters. |
| `course`            | `String`          | `Not Null`                          | Course type, e.g., starter, main course, etc.                |
| `picture`           | `String`          |                                     | URL or path to the recipe's picture.                           |
| `user_id`           | `Integer`         | `Foreign Key(users.user_id)`        | Links the recipe to the user who created it.                   |
| `ingredients`       | `String`          | `Not Null`                          | List of ingredients used in the recipe.                        |
| `instructions`      | `String`          | `Not Null`                          | Cooking instructions for the recipe.                           |
| `vegetarian`        | `String`          | `Default='no'`                      | Indicates if the recipe is vegetarian (yes/no).                |
| `gluten_free`       | `String`          | `Default='no'`                      | Indicates if the recipe is gluten-free (yes/no).               |
| `nut_free`          | `String`          | `Default='no'`                      | Indicates if the recipe is nut-free (yes/no).                  |
| `shellfish_free`    | `String`          | `Default='no'`                      | Indicates if the recipe is shellfish-free (yes/no).            |

#### Relationships:
- **Many-to-One with Users**: The `user_id` is a foreign key that establishes a relationship with the `users` table, indicating that each recipe is created by one user.

---

### Entity-Relationship (ER) Overview

- **Users (`users`)**: Users have unique profiles identified by `user_id`. They can like multiple recipes (stored in `liked_recipes`) and create multiple recipes. A user can also have admin privileges(to be implemented).
- **Recipes (`recipes`)**: Each recipe is identified by `recipe_id` and is created by a specific user (`user_id`). Recipes also contain essential information such as name, ingredients, instructions, and dietary labels (vegetarian, gluten-free, nut-free, shellfish-free).

---

### Relationships

1. **One-to-Many Relationship (Users to Recipes)**: Each user can have multiple recipes associated with them. This is facilitated by the `user_id` foreign key in the `recipes` table, which references the `user_id` in the `users` table.
   
2. **Optional Liked Recipes**: Users can store an array of liked recipe IDs (`liked_recipes`) in their profile, which allows tracking which recipes the user has liked. This array contains references to the `recipe_id` from the `recipes` table.

---

### SQL Representation

```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email_address VARCHAR(255) NOT NULL,
    points INTEGER,
    liked_recipes INTEGER[],
    admin BOOLEAN
);

CREATE TABLE recipes (
    recipe_id SERIAL PRIMARY KEY,
    recipe_name VARCHAR(20) UNIQUE NOT NULL,
    course VARCHAR(255) NOT NULL,
    picture VARCHAR(255),
    user_id INTEGER REFERENCES users(user_id),
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL,
    vegetarian VARCHAR(3) DEFAULT 'no',
    gluten_free VARCHAR(3) DEFAULT 'no',
    nut_free VARCHAR(3) DEFAULT 'no',
    shellfish_free VARCHAR(3) DEFAULT 'no'
);
```
---

This schema captures the relationships and attributes for managing user data, their associated recipes, and dietary options.

# Features

- ## Existing features

* The user can register an account for themselves, so they can also create, edit and delete their recipes, not just view other's.
* After the user left the website or logged out, they are able to log back in to open a new session where they can alter their recipes.(Update/Delete)
* The main page showcases the newest recipe in it's category. The recipes page showcases the top 4 newest recipes. Users can view all recipes by clicking on the View All button next to the categories' name.

- ## Features left to be implemented

* I would like to add a new column for the Users table, so users can have a role assigned to them
* After the roles have been assigned, I would like to add admin features to "My Profile" page.
* Users will be able to send suggestions to admins
* The admins will be able to accept suggestions and put them on a list.
* These above mentioned tasks will be displayed on the main page to show users what updates to expect in the future.

# Technologies used

1. Languages used:

- HTML
- CSS
- JavaScript
- Python
- PostgresSQL

2. Frameworks, Libraries & Programs Used:

- Tailwind - Used to create boxes for the main and footer sections, and to control some of the animations(e.g. navbar links while hovered over).
- SQLAlchemy - Used to help creating SQL commands in a more pythonian way.
- Flask - Used to run the backend, that have control over the frontend.
- GitHub - Used for making my files available on the web.
- Visual Studio Code - Used for the programming environment

3. Websites used

- [I used stackoverflow to check for solution when I got tired/stuck.](https://stackoverflow.com/)
- [I used w3schools to check for correct syntax whenever I had my code stop working.](https://www.w3schools.com/)
- [The website I used to check if my website is responsive. I also included a screenshot in the testing section.](https://ui.dev/)
- [I used Tailwind's website a lot, especially to get a better idea how to create "boxes" to visually separate areas.](https://tailwind.com/)
- [I used Pexels to find appropriate photos and videos to fit in the subject of my website.](https://www.pexels.com)

# Bugs

It proved to be quite challenging to host my website, as I had trouble signing up to Heroku with the Github Student Pack, so I ended up needing to host my app on another hosting service, called Linode. I learnt how to install an OS(Debian) to serve as my web server, host my website with Apache, create a domain and create A records so the user can reach my app with a domain name rather than the fix IP, route all requests through Cloudflare where I was able to enable Full(strict) mode after a lot of reading about how to get a certificate signed for HTTPS connections and get my Apache server to listen to these 443 requests. I quite enjoyed learning all about these, and I hope I could submit a well designed app too.

# Testing

## Testing with validators

### JSLint

- ![A screenshot of the JSLint result.](./readme_files/jslint_result.png "A screenshot of the JSLint result.")

### Lighthouse

  ### Lighthouse mobile

- ![A screenshot of the Lighthouse results for the mobile version](./readme_files/lighthouse_mobile_test.png "Lighthouse test for the mobile version of the site.")

  ### Lighthouse desktop

- ![A screenshot of the initial Lighthouse desktop result.](./readme_files/lighthouse_desktop_test.png "A screenshot of the initial Lighthouse desktop result.")

## W3C HTML


  ### home.html

- ![A screenshot of the home.html validation result.](./readme_files/home_html_validation.png "A screenshot of the home.html validation result.")

  ### index.html

- ![A screenshot of the index.html validation result.](./readme_files/index_html_validation.png "A screenshot of the index.html validation result.")

  ### recipes.html

- ![A screenshot of the recipes.html validation result.](./readme_files/recipes_html_validation.png "A screenshot of the recipes.html validation result.")

  ### sign_in.html

- ![A screenshot of the sign_in.html validation result.](./readme_files/sign_in_html_validation.png "A screenshot of the sign_in.html validation result.")

  ### sign_up.html

- ![A screenshot of the sign_up.html validation result.](./readme_files/sign_up_html_validation.png "A screenshot of the sign_up.html validation result.")

## W3C CSS(Jigsaw)

- ![A screenshot of the CSS validation result.](./readme_files/css_validation.png "A screenshot of the CSS validation result.")

## Final website

![A screenshot of the finished website on different screen sizes.](./readme_files/responsiveness.png "A screenshot of the finished website on different screen sizes.")

## Manual testing

### Function testing

| **Action** | **Image** |
|------------|-----------|
| Adding a new recipe | ![A picture of testing adding a new recipe.](./readme_files/testing_adding_new_recipe.png "Adding new recipe test.") |
| Confirming deletion of a recipe | ![A picture of testing the need of confirmation before recipe deletion.](./readme_files/testing_confirmation_before_delete.png "Confirming before recipe deletion.") |
| Recipe deletion | ![A picture of testing recipe deletion.](./readme_files/testing_deletion.png "Testing recipe deletion.") |
| Updating recipe | ![A picture of testing updating recipe.](./readme_files/testing_updating_recipe.png "Updating recipe.") |
| Form validation while adding new recipe | ![A picture of testing form validation while adding a new recipe.](./readme_files/testing_form_validation_add_recipe_page.png "Form validation test while trying to add new recipe.") |
| Form validation(username) on sign up page. | ![A picture of testing form validation(username) on sign up page.](./readme_files/testing_form_validation_sign_up_username.png "Form validation(username) on sign up page.") |
| Form validation(password) on sign up page. | ![A picture of testing form validation(password) on sign up page.](./readme_files/testing_form_validation_sign_up_password.png "Form validation(password) on sign up page.") |
| Logging out of the session | ![A picture of testing the logout function..](./readme_files/testing_logout.png "Testing the logout function.") |
| Testing models.py | ![A picture of testing models.py.](./readme_files/testing_models_py.png "Testing models.py") |
| Testing routes.py | ![A picture of testing routes.py.](./readme_files/testing_routes_py.png "Adding new recipe test.") |

### User Stories

#### As a newly found home cook

- **Story**: I want an easy way to find a recipe, so that I can start preparing my meal for the upcoming days.
- **Test Result**: The first page the user gets to displays recipes straight away. It also gives options to the user to view more recipes.

#### As a parent

- **Story**: I want to be able to find meals that are recommended for kids, so that I can prepare a meal for my child as quickly as possible.
- **Test Result**: The Kid's meals are displayed on each site where recipes are shown.

#### As a first time view

- **Story**: I want to be able to register an account for myself., so that I can post my recipes.
- **Test Result**: As the user gets to the main page, they find the "Sign in" button on the top right corner. By clicking on it, the app takes them to the next page where they can either sign in, or register a new account.

#### As a returning registered user

- **Story**: I want to be able to update my recipes, so that I can improve them.
- **Test Result**: As the user signs in, they can view all of their recipes by clicking on the picture under the "My recipes" header. On the next page, under each displayed recipe there is an "Edit" button.
  By clicking on it, the user is able to edit the selected recipe on the next page.

#### As a returning registered user

- **Story**: I want to be able to delete my recipes so that I don't have them anymore in my collection.
- **Test Result**: The user could also delete any of their recipes by clicking on the "Delete" button under the recipe.
  They will have to confirm this action by clicking on the next appearing "Confirm" button, or cancel the action by clicking on the "X".

# Credits

1. ## Content

- [The colours used for the website were found on colorhunt.com](https://colorhunt.co/palette/22283131363f76abaeeeeeee)

2. ## Code

- Official site like W3School and Tailwind help to create a great layout that functions well.
- StackOverflow helped me to see how others solved the issues their code had and I manage to use some of the solutions after customising them to fit my code.
- Codeinstitute's walkthrough videos gave me some ideas of how best to manipulate databases with Python. I had to watch other videos as well to fully understand the purpose of the code.

## Deployment

- I used GitHub for version control and Linode to deploy my website. I used Visual Studio Code to access code on my server and to push code to GitHub.

### 1. Server Setup

Ensure your server has Apache, Python, and necessary modules installed:

1. **Update your package list** and install Apache and necessary dependencies:

```bash
sudo apt update
sudo apt install apache2 python3 python3-venv libapache2-mod-wsgi-py3 git
```

2. **Clone the GitHub repository** to your server:

Navigate to the desired directory where the application will be hosted and clone the repository:

```bash
cd /var/www/
sudo git clone https://github.com/codeim1293b/3rd_milestone.git
```

3. **Set up the virtual environment:**

Navigate to the application folder and create a virtual environment for the Flask app:

```bash
cd /var/www/your-flask-app
python3 -m venv venv
source venv/bin/activate
```

4. **Install application dependencies:**

Use pip to install the required packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```

5. **Set up environment variables:**

Create an .env file or export the necessary environment variables for Flask (e.g., SECRET_KEY, FLASK_APP, DATABASE_URI, etc.).

### 2. Configure Apache

1. **Create an Apache configuration file** for your Flask app:

Open a new Apache configuration file for your Flask application:

```bash
sudo nano /etc/apache2/sites-available/your-flask-app.conf
```

Add the following configuration:

```apache
<VirtualHost *:443>
    ServerName your_domain_or_ip

    WSGIDaemonProcess your-flask-app python-path=/var/www/your-flask-app:/var/www/your-flask-app/venv/lib/python3.8/site-packages
    WSGIProcessGroup your-flask-app
    WSGIScriptAlias / /var/www/your-flask-app/your-flask-app.wsgi
    ProxyPass / http://server_IP:5000/
    ProxyPassReverse / http://server_IP:5000/


    <Directory /var/www/your-flask-app>
        Require all granted
    </Directory>

    Alias /static /var/www/your-flask-app/static
    <Directory /var/www/your-flask-app/static>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/your-flask-app-error.log
    CustomLog ${APACHE_LOG_DIR}/your-flask-app-access.log combined
</VirtualHost>
```

2. **Create a WSGI entry point for the Flask app:**

In your application directory, create a your-flask-app.wsgi file:

```bash
sudo nano /var/www/your-flask-app/your-flask-app.wsgi
```

Add the following lines to the file:

```python
import sys
import os

# Activate your virtual environment
activate_this = '/var/www/your-flask-app/venv/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

sys.path.insert(0, '/var/www/your-flask-app')

from app import app as application
```

3. **Enable the new site configuration and the WSGI module:**

```bash
sudo a2ensite your-flask-app
sudo a2enmod wsgi
```

4. **Restart Apache to apply the changes:**

```bash
sudo systemctl restart apache2
```

### 3. **Set Up Git for Version Control**

1. **Pull latest changes from GitHub:**

If you make updates to your repository, pull the changes directly to the server:

```bash
cd /var/www/your-flask-app
sudo git pull origin main
```

### 4. **Set Up a Firewall**

Allow HTTP and HTTPS traffic by updating your firewall rules:

```bash
sudo ufw allow 'Apache Full'
```

### 5. **Securing the Application**

1. **Install and configure SSL** (optional but recommended):

If using a domain, set up SSL for secure HTTPS access using Certbot:

```bash
sudo apt install certbot python3-certbot-apache
sudo certbot --apache -d your_domain
```

### 6. **Final Checks**

Once all steps are complete, your Flask application should be live and accessible at your server's IP address or domain. You can view the logs for any issues:

```bash
tail -f /var/log/apache2/your-flask-app-error.log
```
