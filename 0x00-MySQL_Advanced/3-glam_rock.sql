-- Script that lists all bands with Glam rock
-- as their main style, ranked by their longevity
-- Column names: band_name and lifespan (in years until 2022)
-- Used attributes formed and split for computing the lifespan
-- Script can be executed on any database

SELECT band_name,
COALESCE(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
