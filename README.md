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
  | ![A picture of the home.html desktop version.](./readme_files/wireframe_home_desktop_tablet.png "Desktop version of home.html") | ![A picture of the products.html desktop version.](./readme_files/  wireframe_products_desktop_tablet.png "Desktop version of products.html") | ![A picture of the product_detail.html desktop version.](./readme_files/wireframe_product_detail_desktop_tablet.png "Desktop version of   product_detail.html") |
  | ![A picture of the home.html tablet version.](./readme_files/wireframe_home_desktop_tablet.png "Tablet version of home.html") | ![A picture of the products.html tablet version.](./readme_files/ wireframe_products_desktop_tablet.png "Tablet version of products.html") | ![A picture of the product_detail.html tablet version.](./readme_files/wireframe_product_detail_desktop_tablet.png "Tablet version of product_detail. html") |
  | ![A picture of the home.html mobile version.](./readme_files/wireframe_home_mobile.png "Mobile version of home.html") | ![A picture of the products.html mobile version.](./readme_files/wireframe_products_mobile.png "Mobile  version of products.html") | ![A picture of the product_detail.html mobile version.](./readme_files/wireframe_product_detail_mobile.png "Mobile version of product_detail.html") |


  | **cart_summary.html** | **checkout.html** | **profile.html** |
  |---------------------|------------------|------------------|
  | ![A picture of the cart_summary.html desktop version.](./readme_files/wireframe_cart_summary_desktop_tablet.png "Desktop version of cart_summary.html") | ![A picture of the checkout.html desktop version.](./readme_files/  wireframe_checkout_desktop_tablet.png "Desktop version of checkout.html") | ![A picture of the profile.html desktop version.](./readme_files/wireframe_profile_desktop_tablet.png "Desktop version of profile.html") |
  | ![A picture of the cart_summary.html tablet version.](./readme_files/wireframe_cart_summary_desktop_tablet.png "Tablet version of cart_summary.html") | ![A picture of the checkout.html tablet version.](./readme_files/ wireframe_checkout_desktop_tablet.png "Tablet version of checkout.html") | ![A picture of the profile.html tablet version.](./readme_files/wireframe_profile_desktop_tablet.png "Tablet version of profile.html") |
  | ![A picture of the cart_summary.html mobile version.](./readme_files/wireframe_cart_summary_mobile.png "Mobile version of cart_summary.html") | ![A picture of the checkout.html mobile version.](./readme_files/ wireframe_checkout_mobile.png "Mobile version of checkout.html") | ![A picture of the profile.html mobile version.](./readme_files/wireframe_profile_mobile.png "Mobile version of profile.html") |

  | **process_payment.html** | **success.html** | **orders.html** |
  |---------------------|------------------|------------------|
  | ![A picture of the process_payment.html desktop version.](./readme_files/wireframe_process_payment_desktop_tablet.png "Desktop version of process_payment.html") | ![A picture of the success.html desktop version.](./ readme_files/wireframe_success_desktop_tablet.png "Desktop version of success.html") | ![A picture of the orders.html desktop version.](./readme_files/wireframe_orders_desktop_tablet.png "Desktop version of orders.html") |
  | ![A picture of the process_payment.html tablet version.](./readme_files/wireframe_process_payment_desktop_tablet.png "Tablet version of process_payment.html") | ![A picture of the success.html tablet version.](./  readme_files/wireframe_success_desktop_tablet.png "Tablet version of success.html") | ![A picture of the orders.html tablet version.](./readme_files/wireframe_orders_desktop_tablet.png "Tablet version of orders.html") |
  | ![A picture of the process_payment.html mobile version.](./readme_files/wireframe_process_payment_mobile.png "Mobile version of process_payment.html") | ![A picture of the success.html mobile version.](./readme_files/ wireframe_success_mobile.png "Mobile version of success.html") | ![A picture of the orders.html mobile version.](./readme_files/wireframe_orders_mobile.png "Mobile version of orders.html") |


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

# Features

- ## Existing features

* The user can add products to their cart, view their cart, update quantities of items and remove items from their cart.
* The user can register an account for themselves, so they can save, update their details and delete their cart(s) if they wish.
* There is a Django system in place to handle sessions, SessionMiddleware. This allows users without the need of an account to purchase goods.
* The main page showcases the available categories for both baby clothes and baby toys. By clicking on any category, users can view all products in that category.

- ## Features left to be implemented

* Even though a not authenticated user can purchase goods, and at the success page can see their most recent order's details, they cannot search for their previous orders. Implement a search function for orders(by email address)
* 
* 

# Technologies used

1. Languages used:

- HTML
- CSS
- JavaScript
- Python
- PostgresSQL

2. Frameworks, Libraries & Programs Used:

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
- [I used a self-hosted instance of Stable Diffusion to create images of the products and favicons.](https://stablediffusionweb.com/)

# Bugs

It proved to be quite challenging to host my website, as I had trouble signing up to Heroku with the Github Student Pack, so I ended up needing to host my app on another hosting service, called Linode. I learnt how to install an OS(Debian) to serve as my web server, host my website with Apache, create a domain and create A records so the user can reach my app with a domain name rather than the fix IP, route all requests through Cloudflare where I was able to enable Full(strict) mode after a lot of reading about how to get a certificate signed for HTTPS connections and get my Apache server to listen to these 443 requests. I quite enjoyed learning all about these, and I hope I could submit a well designed app too.

# Testing

## Testing with validators

## JSLint

1. script.js
  - Only issue I got is this: "Wrap a ternary expression in parens, with a line break after the left paren." Which is due to the formatting of the file. This warning does not break the code.  

2.  stripe_elements.js
  - A couple of "Unexpected ','" at the end of the list. Also a "Undeclared 'Stripe'." and a "Move variable declaration to top of function or script.", even though I have declared Stripe in stripe_elements.js. These warnings do not break the code.

3.  theme-switcher.js
  - 

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

![A screenshot of the finished website on different screen sizes.](./readme_files/responsiveness_mobile.png "A screenshot of the finished website on different screen sizes.")
![A screenshot of the finished website on different screen sizes.](./readme_files/responsiveness_tablet.png "A screenshot of the finished website on different screen sizes.")
![A screenshot of the finished website on different screen sizes.](./readme_files/responsiveness_desktop.png "A screenshot of the finished website on different screen sizes.")

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
- **Test Passed**: The registration process is straightforward, with confirmation emails sent successfully. Saved user details are accurately stored and recalled during subsequent visits, streamlining the checkout process for registered users.

## As a registered customer
### Story: Tracking Orders Efficiently
- **I want** to be able to keep track of my orders.
- **So that** I can easily check the status of my orders and manage them efficiently.

#### Test Result:
- **Test Passed**: Registered customers have access to an order history section where they can view past orders, current statuses, and expected delivery dates. The interface is user-friendly and provides accurate, up-to-date information on each order.

# Credits

1. ## Content

- [The colours used for the website were found on colorhunt.com](https://colorhunt.co/palette/22283131363f76abaeeeeeee)

2. ## Code

- Official site like W3School and Tailwind help to create a great layout that functions well.
- StackOverflow helped me to see how others solved the issues their code had and I manage to use some of the solutions after customising them to fit my code.
- Codeinstitute's walkthrough videos gave me some ideas of how best to manipulate databases with Python. I had to watch other videos as well to fully understand the purpose of the code.

# Deployment

- I used GitHub for version control and Linode to deploy my website. I used Visual Studio Code to access code on my server and to push code to GitHub.
- I have built a Docker container out of this app, which makes deployment easier for some. I also included deployment for those who do not user Docker.

## Development Procedure for Containerized Django App

This guide outlines how to set up a development environment for a containerized Django application using Docker, with the image available on Docker Hub.

### Prerequisites

- **Docker Installed**: Ensure Docker is installed and running on your system.
- **PostgreSQL Available**: You can either run PostgreSQL locally or use a remote instance (e.g., AWS RDS).
- **Access to Internet**: To pull the Docker image from Docker Hub.

### Steps to Set Up

#### 1. Clone the Repository

If needed, clone the repository for any project files that are not included in the container.

```bash
git clone https://github.com/m1293b/babysuite.git
cd babysuite
```

#### 2. Create a `.env` File

Create a file named `.env` in your project directory with necessary environment variables.

**Example `.env` content:**

```plaintext
DATABASE_URL=postgresql://username:password@localhost/dbname
SECRET_KEY=your_secret_key
DEBUG=False
```

#### 3. Pull the Docker Image

Pull the pre-built image from Docker Hub:

```bash
docker pull m1293b/babysuite
```

#### 4. Run PostgreSQL Container (if needed locally)

If you don't have a remote PostgreSQL database, run it in another container.

```bash
docker run --name postgres-container \
  -e POSTGRES_USER=username \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=dbname \
  -p 5432:5432 \
  -d postgres
```

#### 5. Run the Django Application Container

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
      - DATABASE_URL=postgresql://username:password@postgres-container/dbname
      - SECRET_KEY=your_secret_key
      - DEBUG=False

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
  -e DATABASE_URL=postgresql://username:password@localhost/dbname \
  -e SECRET_KEY=your_secret_key \
  -e DEBUG=False \
  m1293b/babysuite
```

#### 6. Access the Application

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