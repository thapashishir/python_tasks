CREATE SEQUENCE serial_managers;
CREATE TABLE managers (
    manager_id integer  DEFAULT nextval('serial_managers'::regclass) NOT NULL,
    full_name character varying NOT NULL,
    address character varying,
    contact_no bigint NOT NULL,
    CONSTRAINT pk_manager PRIMARY KEY (manager_id)
);
-- serial key for employee id
CREATE SEQUENCE serial_employees; 
 -- Employee table created
CREATE TABLE employees (
    employee_id integer DEFAULT nextval('serial_employees'::regclass) NOT NULL,
    first_name character varying NOT NULL,
    middle_name character varying,
    last_name character varying NOT NULL,
    join_date timestamp,
    monthly_salary float,
    dept_id integer NOT NULL,
	CONSTRAINT pk_employee_id PRIMARY KEY (employee_id)
);

CREATE SEQUENCE serial_departments;
-- Department table created
CREATE TABLE departments (
    dept_id integer  DEFAULT nextval('serial_departments'::regclass) NOT NULL,
    dept_name character varying NOT NULL,
    dept_code character varying,
    parent_dept_id integer NOT NULL,
    manager_id integer,
    description character varying,
    active Boolean NOT NULL,
	CONSTRAINT pk_dept_id PRIMARY KEY (dept_id)
);

-- Q.1 Write a Single Query to find the Total Earnings by Employees grouped by Departments.
select dept_id,
SUM(monthly_salary * (extract(day from current_date::timestamp - join_date::timestamp))/30)::float as total_earnings 
from employees 
group by dept_id;

-- Q.2 Write a Single Query to find the list of Employees belonging to Department Sales, with service
--length of more than 6 months.

select e.employee_id, e.first_name || ' ' || e.middle_name  || ' ' || e.last_name as full_name
from employees e
inner join departments d on d.dept_id = e.dept_id
where d.dept_id = 1
and ((extract(day from current_date::timestamp - join_date::timestamp)/30) > 6)

-- Q.3 Write a Single Query to list Employees with their Department Name and their Manager Name.
select e.employee_id, d.dept_name, m.manager_id, m.full_name as manager_name
from departments d
join employees e on e.dept_id = d.dept_id
join managers m on m.manager_id = d.manager_id
