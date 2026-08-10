SELECT * from movies;

select industry,count(*) as movie_count from movies
where industry = 'hollywood';

select * from movies 
where studio like 'marvel%';

select distinct industry from movies;

select distinct industry from movies 
where title like '%thor%';

select * from movies where studio = '';
select * from movies
where imdb_rating>=5 and imdb_rating <=9;

select * from movies
where imdb_rating is null;

select * from movies
where release_year between 2015 and 2025
order by release_year asc limit 5 ;

select * from movies
where studio in('marvel studios','zee studios')
order by studio;



select industry,count(*) from movies
group by industry;

select industry,count(*) as movie_count, 
round(avg(imdb_rating),1) as avg_rating,
min(imdb_rating) as min_rating,
max(imdb_rating) as max_rating  
from movies
group by industry;

select release_year,count(*) as count from movies
group by release_year
having count >= 2 
order by release_year desc


