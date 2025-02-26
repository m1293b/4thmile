# Table of content:

## UX

- User stories
- Design choices
- Wireframes
- Data schema

## Features

- Existing features
- Features left to be implemented

## Technologies used

- Languages used
- Frameworks, Libraries & Programs used
- Websites used

## Bugs

- Sort function
- Payment with Stripe javascript
- Javascript file not updating

## Testing

- Testing with validators
- Manual testing
- Automated testing

## Credits

- Content
- Media
- Code

## Deployment#

- Using Docker
- Cloning github, deploying locally

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

  - **I want** to see current discounts on items.
  - **So that** I can save money while purchasing quality products.
  
  ### As a returning customer

  - **I want** to be able to register my account and save my details.
  - **So that** I can purchase products without the need of typing in my details.

  ### As a registered customer

  - **I want** to be able to keep track of my orders.
  - **So that** I can easily check the status of my orders and manage them efficiently.

- ## Design choices

  I chose a darker and a lighter color palette, which the customer is free to choose from, to create a welcoming atmosphere. I used a framework to create a responsive website, that provide a better user experience across all devices.

- ## Wireframes

  | **home.html** | **home.html** | **recipes.html** |
  |----------------|---------------|------------------|
  | ![A picture of the desktop version.](./readme_files/wireframe_desktop_view.png "Desktop view") | ![A picture of the tablet version.](./readme_files/wireframe_tablet_view.png "Tablet view.") | ![A picture of the mobile version.](./readme_files/wireframe_mobile_view.png "Mobile view.") |

 - ## Data Schema

    ### Accounts App

    #### Models

    - **Customer**
      - `user`: ForeignKey to User (Django's built-in User model)
      - `username`: CharField, max_length=255
      - `first_name`: CharField, max_length=255
      - `last_name`: CharField, max_length=255
      - `email`: EmailField, unique=True
      - `phone_number`: CharField, max_length=20
      - `address`: TextField
      - `created_at`: DateTimeField, auto_now_add=True
      - `updated_at`: DateTimeField, auto_now=True
      - `notes`: TextField (optional)

    ### Cart App

    #### Models

    - **Cart**
      - `user`: ForeignKey to User, null=True, blank=True
      - `active_cart`: BooleanField, default=True
      - `total_price`: DecimalField, max_digits=10, decimal_places=2, default=999.99
      - `total_items`: IntegerField, default=0
      - `created_at`: DateTimeField, auto_now_add=True
      - `updated_at`: DateTimeField, auto_now=True

    - **CartItem**
      - `cart`: ForeignKey to Cart, related_name="items"
      - `product`: ForeignKey to Product
      - `quantity`: PositiveIntegerField
      - `created_at`: DateTimeField, auto_now_add=True
      - `updated_at`: DateTimeField, auto_now=True

    ### Orders App

    #### Models

    - **Order**
      - `total`: DecimalField, max_digits=10, decimal_places=2
      - `status`: CharField, max_length=50
      - `created_at`: DateTimeField, auto_now_add=True
      - `updated_at`: DateTimeField, auto_now=True
      - `notes`: TextField (optional)
      - `user`: ForeignKey to User, null=True, blank=True
      - `email`: EmailField, null=True, blank=True

    - **OrderItem**
      - `order`: ForeignKey to Order, related_name="order_items"
      - `price`: DecimalField, max_digits=10, decimal_places=2
      - `product`: ForeignKey to Product
      - `quantity`: IntegerField
      - `created_at`: DateTimeField, auto_now_add=True
      - `updated_at`: DateTimeField, auto_now=True

    ### Products App

    #### Models

    - **Category**
      - `name`: CharField, max_length=100
      - `friendly_name`: CharField, max_length=100 (optional)
      - `main_category`: CharField, max_length=100
      - `description`: TextField (optional)
      - `created_at`: DateTimeField, auto_now_add=True
      - `updated_at`: DateTimeField, auto_now=True

    - **Tag**
      - `name`: CharField, max_length=50, unique=True

    - **Product**
      - `name`: CharField, max_length=100, default="New product"
      - `description`: TextField (required)
      - `image`: ImageField, upload_to="products/images/"
      - `price`: DecimalField, max_digits=10, decimal_places=2
      - `stock`: PositiveIntegerField
      - `category`: ForeignKey to Category, on_delete=models.CASCADE, default=1
      - `color`: CharField, max_length=50 (optional)
      - `size`: CharField, max_length=10 (optional)
      - `tags`: ManyToManyField to Tag, related_name="products"
      - `created_at`: DateTimeField, auto_now_add=True
      - `updated_at`: DateTimeField, auto_now=True
      - `notes`: TextField (optional)
      - `smiles`: IntegerField, default=0
      - `purchases`: IntegerField, default=0
      - `views`: IntegerField, default=0
      - `sales`: IntegerField, default=0
      - `is_on_sale`: BooleanField, default=False
      - `sale_price`: DecimalField, max_digits=10, decimal_places=2, default=999

    ### Reviews App

    #### Models

    - **Review**
      - `review_id`: AutoField (primary key)
      - `product`: ForeignKey to Product, on_delete=models.CASCADE
      - `user`: ForeignKey to User, on_delete=models.CASCADE
      - `rating`: PositiveIntegerField, choices=[(1, "1 Star"), (2, "2 Stars"), (3, "3 Stars"), (4, "4 Stars"), (5, "5 Stars")]
      - `comment`: TextField
      - `created_at`: DateTimeField, auto_now_add=True
 - ## Database Model Relationships

    ### Products and Related Models

    - **Product**
      - **Category**: Each product belongs to a single category, represented by a `ForeignKey` relationship (`product = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)`).
      - **Tag**: A Product can have multiple Tags associated with it using a `ManyToManyField` relationship (`tags = models.ManyToManyField(Tag, related_name="products")`).

    - **Category**
      - No direct relationships to other models besides being referenced by the `Product`.

    - **Tag**
      - Associated with multiple products via the `ManyToManyField` in the Product model.

    ### User and Account Models

    - **User**: This is a Django built-in User model used across various models for user information.

    - **Customer** (from `accounts/models.py`)
      - **User**: Each customer has an optional associated User (`user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)`), allowing the linkage of Django's authentication system to a more detailed    Customer model.

    ### Reviews

    - **Review**
      - **Product**: Each review is linked to one product using a `ForeignKey` relationship (`product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")`).
      - **User**: Each review is associated with one user via a `ForeignKey` relationship (`user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")`).

    ### Orders and Related Models

    - **Order**
      - **User**: An order can be linked to an optional User object (`user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)`).

    - **OrderItem** (from `orders/models.py`)
      - **Order**: Each OrderItem is associated with one order using a `ForeignKey` relationship (`order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")`).
      - **Product**: An OrderItem represents a specific product included in an order, linked via a `ForeignKey` (`product = models.ForeignKey(Product, on_delete=models.CASCADE)`).

    ### Cart and Related Models

    - **Cart**
      - **User**: A cart is associated with an optional User, allowing for both authenticated and guest users to have carts (`user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)`).

    - **CartItem** (from `cart/models.py`)
      - **Cart**: Each CartItem belongs to one cart using a `ForeignKey` relationship (`cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")`).
      - **Product**: A CartItem includes a specific product linked via a `ForeignKey` (`product = models.ForeignKey(Product, on_delete=models.CASCADE)`).

## Summary

The above relationships illustrate how these models interact within the Django project:

- Products are central to multiple aspects of the application, linking with Categories and Tags for organization and Reviews for customer feedback.
- Users can be associated with Customers for additional details, and they place Orders that include OrderItems linked to specific Products.
- Carts allow registered users to store CartItems temporarily before converting them into an order.

These connections enable the application to manage data effectively across different features like product management, user accounts, reviews, orders, and shopping carts.

# Features

- ## Existing features

* The user can add products to their cart, view their cart, update quantities of items and remove items from their cart.
* The user can register an account for themselves, so they can save, update their details and delete their cart(s) if they wish.
* There is a Django system in place to handle sessions, SessionMiddleware. This allows users without the need of an account to purchase goods.
* The main page showcases the available categories for both baby clothes and baby toys. By clicking on any category, users can view all products in that category.

- ## Features left to be implemented

* Even though a not authenticated user can purchase goods, and at the success page can see their most recent order's details, they cannot search for their previous orders. Implement a search function for orders(by email address)
* After doing the Lighthouse tests, it advised me to convert images to .webp format as it provides better performance and reduces file size.

# Technologies used

1. Languages used:

- HTML
- CSS
- JavaScript
- Python
- SQL (only when had to fix issues with the database at some point.)

1. Frameworks, Libraries & Programs Used:

- Django - Used to run the backend, that have control over the frontend.
- Django-Tailwind - Used to create boxes for the main and footer sections, and to control some of the animations(e.g. navbar links while hovered over).
- Django-Allauth - Used to handle authentication and registration.
- jQuery - Used to handle animations and events.
- FontAwesome - Used for icons.
- GitHub - Used for making my files available on the web.
- Visual Studio Code - Used for the programming environment

3. Websites used

- [I used stackoverflow to check for solution when I got tired/stuck.](https://stackoverflow.com/)
- [I used YouTube to look for tutorials when I was stuck.](https://www.youtube.com/)
- [The previously used website to show responsiveness didn't with this project, so I used a Chrome browser extension, called Mobile simulator.](https://chromewebstore.google.com/detail/mobile-simulator-responsi/ckejmhbmlajgoklhgbapkiccekfoccmk)
- [I used Tailwind's website a lot, especially to get a better idea how to create "boxes" to visually separate areas.](https://tailwind.com/)

# Bugs

  1. The Cart model's "total" doesn't get the sale price when product is on sale, but it stores the regular price.
    - This issue is caused by the fact that the Cart model's "total" is calculated using the product's regular price, which is stored in the database. I added a ternary conditional operator, so it adds the sale price if the product is on sale, otherwise it sets it to the regular price to the total.
  
  2. The theme for the whole body, theme-boys or theme-girls, is not being applied correctly. When visiting the admin page, and clicking on "Visit site", most of the background is white instead of the selected theme color.
    - This issue is caused by the Admin panel's theme being applied in the same way, so it overrides the JS file instructions for some reason. I have set the default class to be "theme-boys", and it sorted out the "blinding whitness issue."

  3. Sorting function doesn't work properly.
    - While updating the code, I must have accidentally changed the sorting function's logic. It was supposed to sort by price from lowest to highest, but it was not sorting at all. This is now working, sorting items within the categories correctly based on the selected option.
  
  4. JavaScript file not updating.
    - Any changes in the JavaScript files are not being updated on the site. I have tried clearing the cache and refreshing the page, but it still didn't work. I found a workaround, by adding and updating "?v=1" at the end of the URL, the changes are reflected on a page refresh.

# Testing

## Testing with validators

## JSLint

1. script.js
  - Only issue I got is this: "Wrap a ternary expression in parens, with a line break after the left paren." Which is due to the formatting of the file. This warning does not break the code.  

2.  stripe_elements.js
  - A couple of "Unexpected ','" at the end of the list. Also a "Undeclared 'Stripe'." and a "Move variable declaration to top of function or script.", even though I have declared Stripe in stripe_elements.js. These warnings do not break the code.

3.  theme-switcher.js
  - 0 warnings.

## Lighthouse

  ### Lighthouse mobile

- ![A screenshot of the Lighthouse results for the mobile version](./readme_files/lighthouse_mobile_test.jpg "Lighthouse test for the mobile version of the site.")

  ### Lighthouse desktop

- ![A screenshot of the Lighthouse desktop result.](./readme_files/lighthouse_desktop_test.jpg "A screenshot of the Lighthouse desktop result.")

## W3C HTML

  ### home.html

- ![A screenshot of the home.html validation result.](./readme_files/home_html_validation.png "A screenshot of the home.html validation result.")

  ### contact.html

- ![A screenshot of the contact.html validation result.](./readme_files/contact_html_validation.png "A screenshot of the contact.html validation result.")

  ### about.html

- ![A screenshot of the about.html validation result.](./readme_files/about_html_validation.png "A screenshot of the about.html validation result.")

  ### process_payment.html

- ![A screenshot of the process_payment.html validation result.](./readme_files/process_payment_html_validation.png "A screenshot of the process_payment.html validation result.")

  ### profile.html

- ![A screenshot of the profile.html validation result.](./readme_files/profile_html_validation.png "A screenshot of the profile.html validation result.")

  ### success.html

- ![A screenshot of the success.html validation result.](./readme_files/success_html_validation.png "A screenshot of the success.html validation result.")

  ### cart_summary.html

- ![A screenshot of the cart_summary.html validation result.](./readme_files/cart_summary_html_validation.png "A screenshot of the cart_summary.html validation result.")

  ### checkout.html

- ![A screenshot of the checkout.html validation result.](./readme_files/checkout_html_validation.png "A screenshot of the checkout.html validation result.")

  ### orders.html

- ![A screenshot of the orders.html validation result.](./readme_files/orders_html_validation.png "A screenshot of the siordersgn_up.html validation result.")

  ### product_details.html

- ![A screenshot of the product_details.html validation result.](./readme_files/product_details_html_validation.png "A screenshot of the product_details.html validation result.")

  ### products.html

- ![A screenshot of the products.html validation result.](./readme_files/products_html_validation.png "A screenshot of the products.html validation result.")

## W3C CSS(Jigsaw)

- ![A screenshot of the CSS validation result.](./readme_files/css_validation.png "A screenshot of the CSS validation result.")
- As using a library to control motions and animations in CSS, I got these errors. Does not brake the app, and it can be seen used on mobile view while opening the menu.

## Final website

![A screenshot of the finished website on mobile screen.](./readme_files/responsiveness_mobile.png "A screenshot of the finished website on mobile screen.")
![A screenshot of the finished website on tablet screen.](./readme_files/responsiveness_tablet.png "A screenshot of the finished website on tablet screen.")
![A screenshot of the finished website on desktop screen.](./readme_files/responsiveness_desktop.png "A screenshot of the finished website on desktop screen.")

## Manual testing

## User Stories Testing Results

## As a new parent or guardian
### Story: Browsing and Purchasing High-Quality Baby Products
- **I want** to easily browse and purchase high-quality baby clothes and toys.
- **So that** I can ensure my child has the best products.

#### Test Result:
- **Test Passed**: The product catalog is well-organized, allowing easy browsing by categories (clothes and toys). High-quality images and detailed descriptions are available for each item. Checkout process works seamlessly, indicating a successful purchase.
  
## As an experienced online shopper
### Story: Smooth and Secure Checkout Process
- **I want** a smooth and secure checkout process.
- **So that** I can complete purchases quickly without concerns about security.

#### Test Result:
- **Test Passed**: The checkout process is intuitive with clear instructions. Security features such as SSL encryption, and payment gateway integration present, ensuring user data protection during transactions.

## As a parent looking for specific items
### Story: Sorting Products by Type, Name, and Price
- **I want** to sort products by type (clothes or toys), name, and price.
- **So that** I can find the most suitable products for my baby's needs efficiently.

#### Test Result:
- **Test Passed**: The website provides sorting options on product pages. Users can select filters such as type, name, and price without any issues, resulting in accurate and relevant product lists according to selected criteria. The search functionality also works as expected when filtering products by keywords.

## As someone interested in deals
### Story: Seeing Current Discounts
- **I want** to see current discounts on items.
- **So that** I can save money while purchasing quality products.

#### Test Result:
- **Test Passed**: If the product is on sale, the discounted price shows in red, and the original price is crossed out.

## As a returning customer
### Story: Account Registration and Detail Saving
- **I want** to be able to register my account and save my details.
- **So that** I can purchase products without needing to type in my details each time.

#### Test Result:
- **Test Passed**: The registration process is straightforward. Saved user details are accurately stored and recalled during subsequent visits, streamlining the checkout process for registered users.

## As a registered customer
### Story: Tracking Orders Efficiently
- **I want** to be able to keep track of my orders.
- **So that** I can easily check the status of my orders and manage them efficiently.

#### Test Result:
- **Test Passed**: Registered customers have access to an order history section where they can view past orders, current statuses. The interface is user-friendly and provides accurate, up-to-date information on each order.

## Automated testing

  - **Tests Passed**: The automated tests are set up for each app to verify that all views work as expected.

# Credits

1. ## Media

- All icons and images were generated using a locally ran Stable Diffusion instance.

2. ## Code

- Official site like W3School and Tailwind help to create a great layout that functions well.
- StackOverflow helped me to see how others solved the issues their code had and I manage to use some of the solutions after customising them to fit my code.
- Codeinstitute's walkthrough videos gave me some ideas of how best to manipulate databases with Python.
- I also had to watch YouTube videos to understand how to use the session object in Python, how to set up Stripe to handle payments, and how to use jQuery Ajax to handle forms without refreshing the page.
  - [Most particurarly this video playlist was very helpful](https://www.youtube.com/watch?v=u6R4vBa7ZK4&list=PLCC34OHNcOtpRfBYk-8y0GMO4i1p1zn50)

# Deployment

- I used GitHub for version control and Hetzner to deploy my website. I used Visual Studio Code to access code on my server and to push code to GitHub.
- I have built a Docker container out of this app, which makes deployment easier for some. I also included deployment for those who do not user Docker.

## Development Procedure for Containerized Django App

This guide outlines how to set up a development environment for a containerized Django application using Docker, with the image available on Docker Hub.

### Prerequisites

- **Docker Installed**: Ensure Docker is installed and running on your system.
- **PostgreSQL Available**: You can either run PostgreSQL locally or use a remote instance (e.g., AWS RDS).
- **Access to Internet**: To pull the Docker image from Docker Hub.

### Steps to Set Up

#### 1. Run PostgreSQL Container (if needed locally)

If you don't have a remote PostgreSQL database, run it in another container.

```bash
docker run --name postgres-container \
  -e POSTGRES_USER=username \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=dbname \
  -p 5432:5432 \
  -d postgres
```

#### 2. Run the Django Application Container

Start your Django app using Docker Compose or directly with Docker.

##### Using `docker-compose` (create a `docker-compose.yml` file):

```yaml
version: '3.8'

services:
  web:
    image: m1293b/babysuite
    command: python manage.py runserver 0.0.0.0:5000
    volumes:
      - .:/app
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://username:password@postgres-container/dbname # or postgress when using postgresql container 
      - DJANGO_SECRET_KEY = '{your_secret_key}' \
      - STRIPE_PUBLISHABLE_KEY= {your_publishable_key} \
      - STRIPE_SECRET_KEY= {your_secret_key} \
      - FREE_DELIVERY_THRESHOLD=50 \
      - STRIPE_STANDARD_DELIVERY_PERCENTAGE=10 \
      - DB_HOST= {your_db_host}'
      - DB_PORT= {your_db_port}
      - DB_NAME = '{your_db_name}'
      - DB_USER = '{your_db_user}'
      - DB_PASSWORD = '{your_db_password}'
      - DEBUG=False \

  db:
    image: postgres
    environment:
      POSTGRES_USER: username
      POSTGRES_PASSWORD: password
      POSTGRES_DB: dbname
```

Then run:

```bash
docker-compose up --build
```

##### Run Directly with Docker:

If you prefer not to use `docker-compose`, run the container directly.

```bash
docker run -d \
  --name babysuite-app \
  -p 5000:5000 \
  -v $(pwd):/app \
  -e DATABASE_URL=postgresql://username:password@localhost/dbname # or postgress when using postgresql container \
  -e DJANGO_SECRET_KEY = '{your_secret_key}' \
  -e STRIPE_PUBLISHABLE_KEY= {your_publishable_key} \
  -e STRIPE_SECRET_KEY= {your_secret_key} \
  -e FREE_DELIVERY_THRESHOLD=50 \
  -e STRIPE_STANDARD_DELIVERY_PERCENTAGE=10 \
  -e DB_HOST = '{your_db_host}' \
  -e DB_PORT = '{your_db_port}' \
  -e DB_NAME = '{your_db_name}'
  -e DB_USER = '{your_db_user}'
  -e DB_PASSWORD = '{your_db_password}'
  -e DEBUG=False \
  -e AWS_ACCESS_KEY_ID = {your_aws_access_key_id}
  -e AWS_SECRET_ACCESS_KEY = {your_aws_secret_key}
  -e AWS_STORAGE_BUCKET_NAME = '{your_buckets_name}'
  -e AWS_S3_REGION_NAME = '{your_buckets_region_name}'
  
  m1293b/babysuite
```

#### 3. Access the Application

Open your browser and navigate to `http://localhost:5000` to access your Django application.

### Additional Tips

- **Database Migrations**: Run database migrations inside the container if needed.

  ```bash
  docker exec -it babysuite-app python manage.py migrate
  ```

- **Debugging**: Use Docker logs for debugging issues.

  ```bash
  docker logs babysuite-app
  ```

- **Stopping Containers**:

  To stop and remove containers, use:

  ```bash
  docker-compose down
  # or
  docker stop babysuite-app && docker rm babysuite-app
  ```

This setup allows you to quickly start your development environment using a pre-built Docker image. Adjust configurations as needed for production environments.

## Deploying Locally

To deploy the app by cloning the GitHub repository and running it on your local machine, follow these steps. This guide assumes you have Python and PostgreSQL installed and are not using Docker.

## Prerequisites

- **Python**: Ensure Python (and `pip`) is installed.
- **PostgreSQL**: Install PostgreSQL locally or use a remote instance.
- **Git**: Make sure Git is installed to clone the repository.

## Steps to Deploy Locally

### 1. Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/m1293b/babysuite.git
cd babysuite
```

This command copies the project files to your local machine.

### 2. Set Up Environment Variables

Create an `.env` file in your project directory with necessary environment variables:

**Example `.env` content:**

```plaintext
DJANGO_SECRET_KEY = '{your_django_secret_key}'

STRIPE_SECRET_KEY = {your_stripe_secret_key}
STRIPE_PUBLISHABLE_KEY = {your_stripe_publishable_key}
FREE_DELIVERY_THRESHOLD = 50
STRIPE_STANDARD_DELIVERY_PERCENTAGE = 10

DB_HOST = '{your_db_host}'
DB_PORT = '{your_db_port}'
DB_NAME = '{your_db_name}'
DB_USER = '{your_db_username}'
DB_PASSWORD = '{your_db_password}'

AWS_ACCESS_KEY_ID = {your_aws_access_key_id}
AWS_SECRET_ACCESS_KEY = {your_aws_secret_key}
AWS_STORAGE_BUCKET_NAME = '{your_buckets_name}'
AWS_S3_REGION_NAME = '{your_buckets_region_name}'

USE_AWS = True
```

Replace `username`, `password`, `dbname`, and `your_secret_key` with appropriate values.

### 3. Install Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

This installs all dependencies listed in the `requirements.txt` file.

### 4. Set Up PostgreSQL Database

If running PostgreSQL locally, create a new database and configure it as per your `.env` settings:

1. Start the PostgreSQL service.
2. Create a new database and user with appropriate permissions:

```bash
psql -U postgres
CREATE DATABASE dbname;
CREATE USER username WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE dbname TO username;
\q
```

Replace `dbname`, `username`, and `password` accordingly.

### 5. Migrate Database

Run Django migrations to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates necessary tables in your PostgreSQL database based on your Django models.

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Access the app at `http://127.0.0.1:5000/`.

## Additional Steps

- **Create a Superuser**: To manage the application, create an admin user:

  ```bash
  python manage.py createsuperuser
  ```

- **Test the Application**: Ensure all features work by following any manual or automated tests described in the `README.md`.

This guide provides basic setup instructions for running the Django app locally. For advanced configurations and production environments, refer to best practices for security and performance optimizations.

If you encounter issues, review sections of the README related to bugs, testing, or deployment for further insights.