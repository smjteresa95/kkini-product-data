#product table 생성
create_product_table_query = """
    CREATE TABLE IF NOT EXISTS product (
        product_id BIGINT NOT NULL UNIQUE PRIMARY KEY, 
        product_name VARCHAR(255) NOT NULL,
        brand VARCHAR(255),
        category_name VARCHAR(255),
        large_category VARCHAR(255),
        med_category VARCHAR(255),
        small_category VARCHAR(255),
        total_serving VARCHAR(255),
        serving_size VARCHAR(255),
        kcal DECIMAL(10,2),
        carbohydrate DECIMAL(10,2),
        protein DECIMAL(10,2),
        fat DECIMAL(10,2),
        sodium DECIMAL(10,2),
        cholesterol DECIMAL(10,2),
        saturated_fat DECIMAL(10,2),
        trans_fat DECIMAL(10,2),
        sugar DECIMAL(10,2),
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
"""

# 식품코드를 unique key로 사용하여 공공데이터값 중복되지 않게 insert. 
update_product_from_public_data_query = """
    INSERT INTO product
    (product_id, product_name, brand, category_name, large_category, med_category, small_category, total_serving, serving_size, kcal, carbohydrate, protein, fat, sodium, cholesterol, saturated_fat, trans_fat, sugar)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    product_id = VALUES(product_id)
    """

#ProductFilter table 
create_filter_table_query = """
    CREATE TABLE IF NOT EXISTS product_filter(
        product_id BIGINT NOT NULL,
        category_name VARCHAR(255),
        is_low_calorie BOOLEAN NOT NULL DEFAULT 0,
        is_high_calorie BOOLEAN NOT NULL DEFAULT 0,
        is_sugar_free BOOLEAN NOT NULL DEFAULT 0,
        is_low_sugar BOOLEAN NOT NULL DEFAULT 0,
        is_low_carb BOOLEAN NOT NULL DEFAULT 0,
        is_high_carb BOOLEAN NOT NULL DEFAULT 0,
        is_keto BOOLEAN NOT NULL DEFAULT 0,
        is_low_trans_fat BOOLEAN NOT NULL DEFAULT 0,
        is_low_protein BOOLEAN NOT NULL DEFAULT 0,
        is_high_protein BOOLEAN NOT NULL DEFAULT 0,
        is_low_sodium BOOLEAN NOT NULL DEFAULT 0,
        is_low_cholesterol BOOLEAN NOT NULL DEFAULT 0,
        is_low_saturated_fat BOOLEAN NOT NULL DEFAULT 0,
        is_low_fat BOOLEAN NOT NULL DEFAULT 0,
        is_high_fat BOOLEAN NOT NULL DEFAULT 0,
        is_green BOOLEAN NOT NULL DEFAULT 0
    )
"""

update_filter_query = """
    INSERT INTO product_filter
    (product_id, category_name, is_low_calorie, is_high_calorie, is_sugar_free, is_low_sugar, is_low_carb, is_high_carb, is_keto, is_low_trans_fat, is_high_protein, is_low_sodium, is_low_cholesterol, is_low_saturated_fat, is_low_fat, is_high_fat, is_green)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    product_id = VALUES(product_id)
"""