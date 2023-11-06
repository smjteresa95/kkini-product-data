#product table 생성
create_product_table_query = """
    CREATE TABLE IF NOT EXISTS product (
        product_id BIGINT NOT NULL UNIQUE PRIMARY KEY, 
        product_name VARCHAR(255) NOT NULL,
        maker_name VARCHAR(255),
        category VARCHAR(255),
        large_category VARCHAR(255),
        med_category VARCHAR(255),
        small_category VARCHAR(255),
        total_serving VARCHAR(255),
        serving_size VARCHAR(255),
        unit_weight VARCHAR(255),
        kcal DECIMAL(10,2),
        carbohydrate DECIMAL(10,2),
        protein DECIMAL(10,2),
        fat DECIMAL(10,2),
        sodium DECIMAL(10,2),
        cholesterol DECIMAL(10,2),
        saturated_fat DECIMAL(10,2),
        trans_fat DECIMAL(10,2),
        sugar DECIMAL(10,2),
        is_green BOOLEAN NOT NULL DEFAULT 0,
        nut_score DECIMAL(10,2),
        score DECIMAL(10,2),
        average_rate DECIMAL(10,2),
        image VARCHAR(255),
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
"""

# 식품코드를 unique key로 사용하여 공공데이터값 중복되지 않게 insert. 
update_product_from_public_data_query = """
    INSERT INTO product
        (product_id, product_name, maker_name, category, large_category, med_category, small_category, total_serving, serving_size, unit_weight, 
        kcal, carbohydrate, protein, fat, sodium, cholesterol, saturated_fat, trans_fat, sugar,
        is_green, nut_score)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        product_id = VALUES(product_id),
        product_name = VALUES(product_name),
        maker_name = VALUES(maker_name),
        category = VALUES(category),
        large_category = VALUES(large_category),
        med_category = VALUES(med_category),
        small_category = VALUES(small_category),
        total_serving = VALUES(total_serving),
        serving_size = VALUES(serving_size),
        unit_weight = VALUES(unit_weight),
        kcal = VALUES(kcal),
        carbohydrate = VALUES(carbohydrate),
        protein = VALUES(protein),
        fat = VALUES(fat),
        sodium = VALUES(sodium),
        cholesterol = VALUES(Cholesterol),
        saturated_fat = VALUES(saturated_fat),
        trans_fat = VALUES(trans_fat),
        sugar = VALUES(sugar)   
"""

#ProductFilter table 
create_filter_table_query = """
    CREATE TABLE IF NOT EXISTS product_filter(
        product_id BIGINT NOT NULL,
        product_name VARCHAR(255),
        category VARCHAR(255),
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
    (product_id, product_name, category, is_low_calorie, is_high_calorie, is_sugar_free, is_low_sugar, is_low_carb, is_high_carb, is_keto, is_low_trans_fat, is_high_protein, is_low_sodium, is_low_cholesterol, is_low_saturated_fat, is_low_fat, is_high_fat, is_green)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    product_id = VALUES(product_id)
"""

#ProductInfo table
create_product_info_table_query = """
    CREATE TABLE IF NOT EXISTS product_info(
        product_id BIGINT UNIQUE,
        site VARCHAR(255),
        product_link VARCHAR(255),
        product_img VARCHAR(255),
        original_price INT,
        sales_price INT,
        discount_rate INT,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
"""

update_product_info_query = """
    INSERT INTO product_info (product_id, site, product_link, product_img, original_price, sales_price, discount_rate, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    ON DUPLICATE KEY UPDATE
        site = VALUES(site),
        product_link = VALUES(product_link),
        product_img = VALUES(product_img),
        original_price = VALUES(original_price),
        sales_price = VALUES(sales_price),
        discount_rate = VALUES(discount_rate),
        created_at = CURRENT_TIMESTAMP,
        updated_at = CURRENT_TIMESTAMP
"""

update_price_query = """
    INSERT INTO product_info (product_id, original_price, sales_price, discount_rate, created_at, updated_at)
    VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    ON DUPLICATE KEY UPDATE
        original_price = VALUES(original_price),
        sales_price = VALUES(sales_price),
        discount_rate = VALUES(discount_rate),
        updated_at = CURRENT_TIMESTAMP
"""


