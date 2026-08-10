select movies.movie_id,title,budget,revenue,unit,currency
from movies
left join financials
on movies.movie_id = financials.movie_id;

select movies.movie_id,title,budget,revenue,unit,currency
from movies
right join financials
on movies.movie_id = financials.movie_id;

select movies.movie_id,title,budget,revenue,unit,currency
from movies
left join financials
on movies.movie_id = financials.movie_id

union

select movies.movie_id,title,budget,revenue,unit,currency
from movies
right join financials
on movies.movie_id = financials.movie_id;
