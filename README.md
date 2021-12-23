
---

## **_Harvard CS50’s Web Programming with Python and JavaScript Capstone project (MAG) by Nonso Njokede_**

### **About:**

This capstone project MAG (Make Africa Great) is a non-profit fundraising app that allows registered users to create, donate to, and vote for a Cause. A Cause is a project that affects humans and their communities. It could be anything from a bad road, to skill acquisition for the underprivileged. 

---

### **Why:**

No one man can save the entire world. In fact, no one man can save a nation. But if given the right tools to unite under, the people of a nation could save themselves. Say there are 100 kids in Nigeria who need heart surgeries, at 40,000,000 naira ($95,000) per surgery. There are people who have 4,000,000,000 naira ($9,500,000) but that amount of money is harder to give. However, if 4,000,000 people give 1,000 naira ($2.50), then this goal can be achieved. We don't need to wait for politicians and the ultra wealthy to come to our aid. The people can help the people. MAG is a platform I propose to use to give the people a chance at solving their own problems. MAG can help change the situation of things in African nations. From giving academic scholarships, to combating child trafficking, and providing startup grants for female entrepreneurs, etc, MAG has the potential of solving a lot of problems in the African continent.

---

### **Distinctiveness and Complexity:**

The most distinctive feature of this project is probably that Django template language was used to achieved much of the functions that should originally have be achieved with JavaScript. For example, Django template language was used to render different HTML elements all through various pages of the app, depending on whether the user is authenticated, has made monthly donation, has voted, etc. I just think Django's security is better that JavaScript. However the most complex feature of this project would have to be the manner at which images and files of a Cause are uniquely saved into the database and directories, based on the Cause's ID, and whether or not the Cause already has a dedicated directory. 

Others include;
1. Most of the functions performed by JavaScript, particular on <form> elements, have a django back up function in case JavaScript is turned off on a client device.
2. Bootstrap was solely used for the appearance of the app. No single CSS line of code was written.
3. Django User model was redesigned to include more attributes.
4. The Homepage at any given time shows the top 3 Causes with the highest votes.

---

### **Files Created:**

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
/main/templates/main/user-profile-edit.html - User profile edit page HTML file (where Users can edit their profile information).
/main/templates/main/user-profile.html - User profile page HTML file.

/media/main/causes/ - Directory were Cause files are saved.
/media/main/users/profile-pics/ - Directory were user profile pictures are saved.

/others/todo.txt - A to-do list text file.

/.gitignore - A git ignore file.

/README.md - Readme file for this project.

/requirements.txt - A list of required packages for this project

```

---

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
py manage.py runserver

```

---

### **Specification:**

Using Python, JavaScript, HTML, and CSS, this is the implementation of a non-profit fundraising app that allows users to donate, create a Cause, vote on a Cause, and comment on a Cause. The following requirements were fulfilled:

* New User: New user is able to register by filling a form. 
    * New User cannot have the same Username, Email Address, and Phone Number with another Registered User.
    * Some fields in the Registration form are optional.
    * Upon successful registration, User is redirected to Login page.
    * There are irremovable prompts to remind the new User that they have not made Monthly donation and/or voted on a Cause.
    * Registration link would redirect to User's profile, if User is already logged in.

* Login User: Users can log in with either their email or username. 
    * Login link would redirect to User's profile, if User is already logged in.

* Edit User: Logged in users are able to click on an "Edit" button in their profile page to edit their profile.
    * When the "edit" button is clicked, the user is taken to an Edit page, with a form that is pre-filled with the current details of the User.
    * The User is able to change the details of a single field or as many fields as possible.
    * When completed, the User is redirected to the User's profile page and changes (if any) are reflected.

* Causes: The "Causes" link in the navigation bar takes the User to a page where they can see all Causes.
    * Each Cause item displays the Cause's name, cost, expiration days (if any) and total number of votes. Total number of votes is substituted for "Awaiting Approval", if the Cause has not been approved.
    * Only 10 Causes are displayed on the page at a time. If there are more than ten Causes, a "Next" button appears to take the user to the next page of Causes (which should be older than the current page of Causes). If not on the first page, a "Previous" button appears to take the user to the previous page of Causes as well.
    * The Clause's name when clicked redirects to a new page showing details of the Cause. 

* Cause:  Wherever the name of a Cause is shown, clicking on it redirects to a Cause page showing details of that Cause.
    * Using JavaScript, a logged in User is able to comment on a Cause without requiring a reload of the entire page.
    * If the Cause already has comments, they are shown. Otherwise it is stated that there are "no comments".

* Donate: A function to emulate donating.
    * There is a "donate" button that redirects to a donate page.
    * Clicking on "pay" button in the donate page would set the User's account monthly donation status to True, and remove the payment prompt. Thus emulating a payment portal.
    * Upon successful payment, the Total Amount displayed in the Homepage is updated.

* Create Cause: A logged in User, who has made monthly donation, is able to create a new Cause.
    * Uploaded files of New Cause are uniquely saved in the /media directory, under a new directory, based on the Cause's ID. Therefore effectively having all the files of a Cause in a single directory.
    * On successful cause creation, the User is redirected to the newly created Cause page.

* "Vote" and "Unvote": A "Vote" button is made visible for the User who has made monthly donation, and thus the User is able to Vote or Unvote a Cause.
    * When the User clicks on the "vote" button, JavaScript is used to asynchronously let the server know to update the vote count and then update the Cause's vote count displayed, by 1, and change the "vote" button" to "unvote" on the page. Likewise when the User clicks on the "unvote" button, the vote count and the Cause's vote count displayed are both decreased by 1, with the "unvote" button changing to "vote".
    * If the User has not voted for a Cause and clicks on the "vote" button, the irremovable prompt for monthly vote is removed, using JavaScript.

---