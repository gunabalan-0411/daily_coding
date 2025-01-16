-- | product_id | low_fats | recyclable |
-- | ---------- | -------- | ---------- |
-- | 0          | Y        | N          |
-- | 1          | Y        | Y          |
-- | 2          | N        | Y          |
-- | 3          | Y        | Y          |
-- | 4          | N        | N          |
-- # Write your MySQL query statement below
select product_id from Products where low_fats = 'Y' and recyclable = 'Y'

-- | product_id |
-- | ---------- |
-- | 1          |
-- | 3          |