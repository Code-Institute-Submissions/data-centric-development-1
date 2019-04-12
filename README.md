# Milestone Project - Data Centric Development (DCD)

Welcome to Derek Dhammaloka's Milestone Project on Data Centric Development (DCD).
My idea is holiday manager.  It has the ability to create (add), read (get), update (edit) and
delete holidays as well as categories.

## UX

My goal on Data Centric Development is to provide information on holidays, as well as
adding (creating), editing (updating) and deleting holidays.  I want to provide a user friendly design
(e.g. using sans serif fonts).

As a user, I want to be able to create, read, update and delete holiday.
I want to find out a holiday that fits my needs (e.g. in terms of categories).
I want to delete a holiday that does not fit my needs (e.g. in terms of categories).
I want to modify the description of my holiday (e.g. the hotel is closed for refurbishment
and an alternative hotel is provided).
I want to add a holiday as soon as it becomes available for my needs.

Category names are in alphabetical order.  Holiday titles are in alphabetical order.

Wireframes are available in the wireframes folder.
Schema is available in the dbdiagram folder.

## Features

Features include Create (Add), Read (Get), Update (Edit) and Delete Holidays and Categories.

Fields include Category Name, Holiday Name, Holiday Description, Nights and Depart Date.

Collapsible body to show or hide holiday description.  The datepicker class is provided for the depart date
field.  The date is picked from the calendar.

Counts for holidays and categories are available.

## Technologies Used

* Materialize
* CSS (External)
* jQuery
* Python Flask
* MongoDB

Materialize for background colors (e.g. mobile versions) and icons.
jQuery to facilitate the datepicker class.
Python Flask to count the number of items using the count method.

## Testing

This site was tested on different browser widths. When the browser width is less than a certain size, it
is for a mobile version.  The mobile version has a light blue background colour (blue lighten-4).

[Color Schemes](https://materializecss.com/color.html)

All links have been tested to ensure that they at the correct destination.
If you click on the delete button for a particular category, that category is deleted.
The count for the category is reduced by 1.

If you click on the add category button, add a category, the count for the category is added by 1.

If you click the delete button for a particular holiday, that particular holiday is deleted.  The
count for the holidays is reduced by 1.

If you successfully add a holiday, the count for the holidays is added by 1.

## Deployment

This site is deployed using Heroku.

## Credits

Visited w3schools and materialize websites for ideas.  In the w3schools website, went to Python and MongoDB.

## Media

Most of the Holiday Descriptions taken from Solos Holidays, Premier Travel and On The Beach.  This can be by
post or E-mail.

## Acknowledgements

Mentor - Olawaseun Owonikoko, especially for [DB Diagram](https://dbdiagram.io/d)
Visit to website [Materialize](https://materializecss.com) for use of colors, icons, etc.

