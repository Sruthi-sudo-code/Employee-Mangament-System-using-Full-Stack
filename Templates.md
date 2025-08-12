Templates Overview
The Employee Management System uses modular and reusable HTML templates to structure the frontend UI. These templates ensure consistent design, reduce code duplication, and make it easier to manage different pages of the application.

1. layout.html (Base Layout Template)
Purpose: Acts as the main structure for all pages.

Contains:

Header with navigation links

Footer section

Placeholder ({% block content %} in Django / <Outlet /> in React Router / yield in Express with EJS) for page-specific content

Benefit: Provides a unified look and feel across the application.

2. index.html (Home / Dashboard Template)
Purpose: Displays the list of employees in a table format.

Features:

Table with Employee Name, Email, Role, Department, and Actions

"Add Employee" button linking to the add-user page

Edit/Delete buttons for each employee record

Search bar and filter options (if implemented)

3. add_user.html (Add Employee Template)
Purpose: Allows admins to add a new employee to the system.

Fields:

Full Name

Email Address

Phone Number

Department

Role

Date of Joining

Includes:

Input validation (client-side and server-side)

Submit and Cancel buttons

4. edit_user.html (Edit Employee Template)
Purpose: Enables admins to update existing employee details.

Features:

Pre-filled form fields with the employee’s current information

Option to update only necessary fields

Save and Cancel buttons

