-- Create a temporary table to store the lifespan of each band
CREATE TEMPORARY TABLE band_lifespan AS
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, '')) > 0;

-- Retrieve the bands ranked by their longevity
SELECT band_name, lifespan
FROM band_lifespan
ORDER BY lifespan DESC;

-- Drop the temporary table
DROP TEMPORARY TABLE IF EXISTS band_lifespan;

