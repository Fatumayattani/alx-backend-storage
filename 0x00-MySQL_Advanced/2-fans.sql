-- This query ranks the country origins of bands
-- The ranking is based on the total number of (non-unique) fans
-- The column names in the result will be: origin and nb_fans

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands 
GROUP BY origin
ORDER BY nb_fans DESC;
