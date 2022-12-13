--select * from orders;
--create table orderscopy as select * from orders; 
--delete from orderscopy;
select * from orderscopy;


DO $$
 DECLARE
     order_id   orderscopy.order_num%TYPE;
     customer_id orderscopy.cust_id%TYPE;

 BEGIN
     order_id := 30000;
     customer_id := 'cust_';
     FOR counter IN 1..20
         LOOP
            INSERT INTO orderscopy (order_num, cust_id, order_date)
             VALUES (counter + order_id, customer_id || 100+counter, current_date - counter + 1);
         END LOOP;
 END;
 $$






