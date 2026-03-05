CREATE TABLE public.product_revenue (
    product VARCHAR(50),
    revenue DECIMAL(10, 2)
);


0r 

CREATE TABLE public.product_revenue (
    product VARCHAR(50),
    revenue FLOAT
);

SELECT * FROM public.product_revenue ORDER BY revenue DESC;