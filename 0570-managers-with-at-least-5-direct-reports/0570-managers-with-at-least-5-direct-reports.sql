# Write your MySQL query statement below
with ok as (select managerId, count(id) as final
from Employee
group by managerId)
select e.name
from Employee e
inner join ok 
on e.id = ok.managerId and ok.final>=5;