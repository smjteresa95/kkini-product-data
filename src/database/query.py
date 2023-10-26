#product table 생성
create_product_table_query = """
    CREATE TABLE IF NOT EXISTS product (
        product_id BIGINT NOT NULL UNIQUE PRIMARY KEY, 
        product_name VARCHAR(255) NOT NULL,
        mfg_company VARCHAR(255),
        category VARCHAR(255),
        large_category VARCHAR(255),
        med_category VARCHAR(255),
        small_category VARCHAR(255),
        site VARCHAR(255),
        image TEXT,
        product_link TEXT,
        sales_price INT,
        discount_rate DECIMAL(5,2),
        discounted_price INT,
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
    (product_id, product_name, mfg_company, category, large_category, med_category, small_category, total_serving, serving_size, kcal, carbohydrate, protein, fat, sodium, cholesterol, saturated_fat, trans_fat, sugar)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    product_id = VALUES(product_id)
    """