{{ config(
    materialized='table'  -- Указываем, что мы хотим создать таблицу
) }}

WITH source_data AS (
    SELECT
        name,
        mass,
        skin_color
    FROM
        {{ ref('star_wars') }}  -- Ссылаемся на другую таблицу, откуда берем данные
)

SELECT
    name,
    mass,
    skin_color
FROM
    source_data
