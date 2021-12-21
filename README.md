Requirements
The most common cause for failure of the final project is not spending enough effort on this next instruction. Read it completely. Your README.md file should be minimally multiple paragraphs in length, and should provide a comprehensive documentation of what you did and, if applicable, why you did it.

In a README.md in your project’s main directory, include a writeup describing your project, and specifically your file MUST include all of the following:
Under its own header within the README called Distinctiveness and Complexity: Why you believe your project satisfies the distinctiveness (distinguishes from other projects in the course) and complexity requirements, mentioned above.
What’s contained in each file you created.
How to run your application.
Any other additional information the staff should know about your project.
Though there is not a hard requirement here, a README.md in the neighborhood of 500 words is likely a solid target, assuming the other requirements are also satisfied.


EXAMPLES BELOW:
EXAMPLES BELOW:
EXAMPLES BELOW:

EXAMPLE 1: PROJECT 4 (NETWORK):
EXAMPLE 1: PROJECT 4 (NETWORK):
EXAMPLE 1: PROJECT 4 (NETWORK):

Specification
Using Python, JavaScript, HTML, and CSS, complete the implementation of a social network that allows users to make posts, follow other users, and “like” posts. You must fulfill the following requirements:

New Post: Users who are signed in should be able to write a new text-based post by filling in text into a text area and then clicking a button to submit the post.
The screenshot at the top of this specification shows the “New Post” box at the top of the “All Posts” page. You may choose to do this as well, or you may make the “New Post” feature a separate page.
All Posts: The “All Posts” link in the navigation bar should take the user to a page where they can see all posts from all users, with the most recent posts first.
Each post should include the username of the poster, the post content itself, the date and time at which the post was made, and the number of “likes” the post has (this will be 0 for all posts until you implement the ability to “like” a post later).
Profile Page: Clicking on a username should load that user’s profile page. This page should:
Display the number of followers the user has, as well as the number of people that the user follows.
Display all of the posts for that user, in reverse chronological order.
For any other user who is signed in, this page should also display a “Follow” or “Unfollow” button that will let the current user toggle whether or not they are following this user’s posts. Note that this only applies to any “other” user: a user should not be able to follow themselves.
Following: The “Following” link in the navigation bar should take the user to a page where they see all posts made by users that the current user follows.
This page should behave just as the “All Posts” page does, just with a more limited set of posts.
This page should only be available to users who are signed in.
Pagination: On any page that displays posts, posts should only be displayed 10 on a page. If there are more than ten posts, a “Next” button should appear to take the user to the next page of posts (which should be older than the current page of posts). If not on the first page, a “Previous” button should appear to take the user to the previous page of posts as well.
See the Hints section for some suggestions on how to implement this.
Edit Post: Users should be able to click an “Edit” button or link on any of their own posts to edit that post.
When a user clicks “Edit” for one of their own posts, the content of their post should be replaced with a textarea where the user can edit the content of their post.
The user should then be able to “Save” the edited post. Using JavaScript, you should be able to achieve this without requiring a reload of the entire page.
For security, ensure that your application is designed such that it is not possible for a user, via any route, to edit another user’s posts.
“Like” and “Unlike”: Users should be able to click a button or link on any post to toggle whether or not they “like” that post.
Using JavaScript, you should asynchronously let the server know to update the like count (as via a call to fetch) and then update the post’s like count displayed on the page, without requiring a reload of the entire page.
Hints
For examples of JavaScript fetch calls, you may find some of the routes in Project 3 useful to reference.
You’ll likely need to create one or more models in network/models.py and/or modify the existing User model to store the necessary data for your web application.
Django’s Paginator class may be helpful for implementing pagination on the back-end (in your Python code).
Bootstrap’s Pagination features may be helpful for displaying pages on the front-end (in your HTML).

EXAMPLE 2: GITHUB DOWNLOAD:
EXAMPLE 2: GITHUB DOWNLOAD:
EXAMPLE 2: GITHUB DOWNLOAD:

---

## **_Harvard CS50’s Web Programming with Python and JavaScript Capstone project (MAG) by Nonso Njokede_**

### **About:**

This capstone project MAG (Make Africa Great) is a fundraising app that allows users to create, donate to, and vote for a Cause. A Cause is a project that affects humans and their communities. It could be anything from a bad road, to skill acquisition for the underprivileged. 

**NOTE: MAG has real world application and it is my intent to continue working on it long after my training.**

### **Distinctiveness and Complexities:**

The most distinctive feature of this project is probably that Django template language was used to achieved much of the functions that should originally have be achieved with JavaScript. For example, Django template language was used to render different HTML elements all through various pages of the app, depending on whether the user is authenticated, has made monthly donation, has voted, etc. I just think Django's security is better that JavaScript. However the most complex feature of this project would have to be the manner at which images and files of a Cause are uniquely saved into the database and directories, based on the Cause's ID, and whether or not the Cause already has a dedicated directory. 

Others include;
1. Most of the functions performed by JavaScript, particular on <form> elements, have a django back up function in case JavaScript is turned off on a client device.
2. Bootstrap was solely used for the appearance of the app. No single CSS line of code was written.
3. Django User model was redesigned to include more fields.
4. The Homepage at any given time shows the top 3 Causes with the highest votes.


### **Why:**

No one man can save the entire world. In fact, no one man can save a nation. But if given the right tools to unite under, the people of a nation could save themselves. Say there are 100 kids in Nigeria who need heart surgeries, at 40,000,000 naira ($95,000) per surgery. There are people who have 4,000,000,000 naira ($9,500,000) but that amount of money is harder to give. However, if 4,000,000 people give 1,000 naira ($2.50), then this goal can be achieved. We don't need to wait for politicians and the ultra wealthy to come to our aid. The people can help the people. MAG is a platform I propose to use to give the people a chance at solving their own problems. MAG can help change the situation of things in African nations. From giving academic scholarships, to combating child trafficking, and providing startup grants for female entrepreneurs, etc, MAG has the potential of solving a lot of problems in the African continent.


### **Files:**

Below are the files that were created for the purpose of this project. This does not include default project files.

```
/main/static/main/index.js - Main project JavaScript file.

/main/templates/main/about.html - About page HTML file (About MAG).
/main/templates/main/cause.html - Cause page HTML file (Details of a Cause).
/main/templates/main/causes.html - Causes page HTML file (list of all Causes).
/main/templates/main/contact.html - Contact page HTML file.
/main/templates/main/donate.html - Donate page HTML file (Where donation payment is initialized).
/main/templates/main/index.html - Home page HTML file.
/main/templates/main/layout.html - HTML file all other HTML files extends from.
/main/templates/main/login.html - Login page HTML file.
/main/templates/main/new-cause.html - HTML file to create a new Cause.
/main/templates/main/register.html - Registration page HTML file.
/main/templates/main/test.html - Test page HTML file (Where some functionalities are tested so as not to break anything).
/main/templates/main/user-profile-edit.html - HTML file where Users can edit their profile information.
/main/templates/main/user-profile.html - User profile page HTML file.
/main/templates/main/about.html - About page HTML file.

/media/main/causes/ - Directory were Cause files are saved.
/media/main/users/profile-pics/ - Directory were user profile pictures are saved.

/others/todo.txt - A to-do list text file.

/.gitignore - A git ignore file.

/README.md - Read me file for the project.

/requirements.txt - A list of required packages for this project

```

---

<br>

### **How to run application:**

**Django server**

1. Navigate to the project folder and create a virtual environment and activate it.

```
virtualenv mag-venv
source mag-venv/Scripts/activate
```

2. Install all required packages.

```
pip install -r requirements.txt
```

3. Initialize the database for the app with makemigrations mag, migrate, then create superuser.

```
py manage.py makemigrations mag
py manage.py migrate
py manage.py createsuperuser
```

4. Launch the Django server. If set up correctly, server will launch on http://127.0.0.1:8000/.

```
py manange.py runserver
```
