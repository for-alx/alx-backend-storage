-- Select brands with 'Glam rock' and their style
-- and rank by their logetivity
SELECT band_name,
IFNULL(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, ''))
ORDER BY lifespan DESC;
