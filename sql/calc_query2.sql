SELECT *, revenue - budget as profit,
if(currency = 'usd',revenue*77,revenue) as revenue_inr 
FROM financials
;
select*,
case
      when unit = 'Billions' then revenue*1000
      when unit = 'thousands' then revenue/1000
      else revenue
end as unit_to_million
 from financials;