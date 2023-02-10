# PROBLEM 1
# How many artists are there?
# Return a single column called "count" with a single row containing the count.
query_1 = """
select
	count ("ArtistId")
from
	"Artist"
    """

# PROBLEM 2
# How many Artists do not have an Album associated with them?
# Return a single column called "count" with a single row containing the count.
query_2 = """
select
	count(art."ArtistId")
from
	"Artist" as art
left join "Album" as alb on
	art."ArtistId" = alb."ArtistId"
where
	alb."AlbumId" is null

"""

# PROBLEM 3
# How many Albums do not have an artist in the Artist table associated with them?
# Return a single column called "count" with a single row containing the count.
query_3 = """
select
	count(art."ArtistId")
from
	"Artist" as art
right join "Album" as alb on
	art."ArtistId" = alb."ArtistId"
where
	art."ArtistId" is null

"""

# PROBLEM 4
# List the tracks by "AC/DC"
# Return a single column called "AC/DC Tracks",
# in any order.
query_4 = """
select
	tr."Name" as "AC/DC Tracks"
from
	"Artist" as art
join "Album" as alb on
	art."ArtistId" = alb."ArtistId"
join "Track" as tr on
	alb."AlbumId" = tr."AlbumId"
where
	art."Name" = 'AC/DC'

"""

# PROBLEM 5
# Find the total sales of AC/DC Tracks.
# Return a single column called "Total Sales" with a single row containing the total.

query_5 = """
select
	sum(inv."UnitPrice" * inv."Quantity") as "Total Sales"
from
	"Artist" as art
join "Album" as alb on
	art."ArtistId" = alb."ArtistId"
join "Track" as tr on
	alb."AlbumId" = tr."AlbumId"
join "InvoiceLine" as inv on
	tr."TrackId" = inv."TrackId"
where
	art."Name" = 'AC/DC' 

"""

# PROBLEM 6
# Calculate total sales for each artist,
# as defined by the "Artist" table,
# Return two columns, "Artist" and "Total Sales",
# for the artists with less than or equal to $5 in sales,
# in any order.

query_6 = """
select
	sum(inv."UnitPrice" * inv."Quantity") as "Total Sales",
	art."Name" as "Artist"
from
	"Artist" as art
join "Album" as alb on
	art."ArtistId" = alb."ArtistId"
join "Track" as tr on
	alb."AlbumId" = tr."AlbumId"
join "InvoiceLine" as inv on
	tr."TrackId" = inv."TrackId"
group by
	art."Name"
having
	sum(inv."UnitPrice" * inv."Quantity") <= 5 

"""

# PROBLEM 7
# Calculate total sales for each artist,
# as defined by the "Artist" table,
# Return two columns, "Artist" and "Total Sales",
# in descending order of "Total Sales".

query_7 = """

"""

# PROBLEM 8
# Find all of "Michael Mitchell"'s direct reports.
# Return 2 columns called "Name" and "Title".
# "Name" should have the employee's name in the form "last name, first name",
# for example, someone with the last name "Smith" and first name "Bob" should be "Bob, Smith".
# Hint: this requires a self join, picking clear aliases will help.

query_8 = """
select 
	concat(emp."LastName",', ', emp."FirstName") as "Name",
	emp."Title"
from 
	"Employee" as emp
join "Employee" as mgr on
	emp."ReportsTo" = mgr."EmployeeId"
where 
	mgr."FirstName" = 'Michael' and mgr."LastName" = 'Mitchell'

"""

# PROBLEM 9
# Make a reporting chart. For each employee, find their name, title, manager's name and manager's title.
# Return 4 columns called "Employee Name" and "Employee Title", "Manager Name" and "Manager Title",
# "Employee Name" and "Manager Name" should have the employee's name as in the form "last name, first name",
# for example someone with the last name "Smith "and first name "Bob" should be "Bob, Smith".
# Hint: this requires a self join, picking clear aliases will help.

query_9 = """
select 
	concat(emp."LastName",', ', emp."FirstName") as "Employee Name",
	emp."Title" as "Employee Title",
	concat(mgr."LastName",', ', mgr."FirstName") as "Manager Name",
	mgr."Title" as "Manager Title"
from 
	"Employee" as emp
join "Employee" as mgr on
	emp."ReportsTo" = mgr."EmployeeId"

"""

# PROBLEM 10
# Find the most recently hired employee(s) and their hire date(s)
# Return two columns called "Name" and "Hire Date",
# in any order.
# "Name" should have the employee's name as in the form "last name, first name",
# for example someone with the last name "Smith "and first name "Bob" should be "Bob, Smith"

query_10 = """
select 
	concat(emp."LastName",', ', emp."FirstName") as "Name",
	"HireDate" as "Hire Date"
from
	"Employee" as emp
where
	emp."HireDate" = (select max("HireDate") from "Employee")

"""

# PROBLEM 11
# Assume today is "2010-01-01", find every employee's tenure.
# Return 3 columns called "First Name" "Last Name", "Tenure",
# in any order.

query_11 = """
select 
	"FirstName" as "First Name",
	"LastName" as "Last Name",
	'2010-01-01' - "HireDate" as "Tenure"
from "Employee"

"""
# PROBLEM 12
# Assume today is 2010-01-01, find every employee with a tenure of less than 7 365-day years.
# Return 3 columns called "First Name" "Last Name", "Tenure",
# in ascending order of tenure.

query_12 = """

"""
