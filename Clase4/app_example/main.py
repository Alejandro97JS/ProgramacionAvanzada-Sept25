
import logging
from fastapi import FastAPI, HTTPException, Depends
from database import SessionLocal, engine
from models import DecBase
import schemas, crud

# Configuración de logging
logger = logging.getLogger("ecommerce")
logger.setLevel(logging.DEBUG)

# Handler para consola (DEBUG+)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_format = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)

# Handler para archivo debug.log (DEBUG+)
debug_file_handler = logging.FileHandler("debug.log", encoding="utf-8")
debug_file_handler.setLevel(logging.DEBUG)
debug_file_handler.setFormatter(console_format)
logger.addHandler(debug_file_handler)

# Handler para archivo warning.log (WARNING+)
warning_file_handler = logging.FileHandler("warning.log", encoding="utf-8")
warning_file_handler.setLevel(logging.WARNING)
warning_file_handler.setFormatter(console_format)
logger.addHandler(warning_file_handler)


app = FastAPI(title="Ecommerce API")
logger.info("FastAPI app initialized")

DecBase.metadata.create_all(bind=engine)
logger.debug("Database tables created (if not exist)")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products")
def create_product(payload: schemas.ProductCreate, db=Depends(get_db)):
    logger.debug(f"POST /products payload: {payload}")
    product = crud.create_product(db, payload)
    logger.info(f"Product created: {product.id} - {product.name}")
    return product

@app.get("/products")
def list_products(db=Depends(get_db)):
    logger.debug("GET /products called")
    products = crud.list_products(db)
    logger.info(f"Returned {len(products)} products")
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int, db=Depends(get_db)):
    logger.debug(f"GET /products/{product_id} called")
    product = crud.get_product(db, product_id)
    if not product:
        logger.warning(f"Product not found: {product_id}")
        raise HTTPException(status_code=404, detail="Product not found")
    logger.info(f"Product returned: {product.id} - {product.name}")
    return product

@app.patch("/products/{product_id}")
def patch_product(product_id: int, patch: schemas.ProductUpdate, db=Depends(get_db)):
    logger.debug(f"PATCH /products/{product_id} payload: {patch}")
    product = crud.update_product(db, product_id, patch)
    if not product:
        logger.warning(f"Product to patch not found: {product_id}")
        raise HTTPException(status_code=404, detail="Product not found")
    logger.info(f"Product updated: {product.id} - {product.name}")
    return product

@app.delete("/products/{product_id}")
def remove_product(product_id: int, db=Depends(get_db)):
    logger.debug(f"DELETE /products/{product_id} called")
    ok = crud.delete_product(db, product_id)
    if not ok:
        logger.warning(f"Product to delete not found: {product_id}")
        raise HTTPException(status_code=404, detail="Product not found")
    logger.info(f"Product deleted: {product_id}")
    return None



# --- CATEGORY ENDPOINTS ---

@app.post("/categories")
def create_category(payload: schemas.CategoryCreate, db=Depends(get_db)):
    logger.debug(f"POST /categories payload: {payload}")
    category = crud.create_category(db, payload)
    logger.info(f"Category created: {category.id} - {category.name}")
    return category

@app.get("/categories")
def list_categories(db=Depends(get_db)):
    logger.debug("GET /categories called")
    categories = crud.list_categories(db)
    logger.info(f"Returned {len(categories)} categories")
    return categories

@app.get("/categories/{category_id}")
def get_category(category_id: int, db=Depends(get_db)):
    logger.debug(f"GET /categories/{category_id} called")
    category = crud.get_category(db, category_id)
    if not category:
        logger.warning(f"Category not found: {category_id}")
        raise HTTPException(status_code=404, detail="Category not found")
    logger.info(f"Category returned: {category.id} - {category.name}")
    return category

@app.patch("/categories/{category_id}")
def patch_category(category_id: int, patch: schemas.CategoryUpdate, db=Depends(get_db)):
    logger.debug(f"PATCH /categories/{category_id} payload: {patch}")
    category = crud.update_category(db, category_id, patch)
    if not category:
        logger.warning(f"Category to patch not found: {category_id}")
        raise HTTPException(status_code=404, detail="Category not found")
    logger.info(f"Category updated: {category.id} - {category.name}")
    return category

@app.delete("/categories/{category_id}")
def remove_category(category_id: int, db=Depends(get_db)):
    logger.debug(f"DELETE /categories/{category_id} called")
    ok = crud.delete_category(db, category_id)
    if not ok:
        logger.warning(f"Category to delete not found: {category_id}")
        raise HTTPException(status_code=404, detail="Category not found")
    logger.info(f"Category deleted: {category_id}")
    return None


# --- PRODUCT-CATEGORY ASSOCIATION ENDPOINT ---
@app.patch("/products/{product_id}/category/{category_id}")
def assign_product_to_category(product_id: int, category_id: int, db=Depends(get_db)):
    logger.debug(f"PATCH /products/{product_id}/category/{category_id} called")
    product = crud.get_product(db, product_id)
    category = crud.get_category(db, category_id)
    if not product:
        logger.warning(f"Product not found: {product_id}")
        raise HTTPException(status_code=404, detail="Product not found")
    if not category:
        logger.warning(f"Category not found: {category_id}")
        raise HTTPException(status_code=404, detail="Category not found")
    product.category_id = category_id
    db.commit()
    db.refresh(product)
    logger.info(f"Product {product_id} assigned to category {category_id}")
    return {}

@app.get("/products/{product_id}/category")
def get_product_category(product_id: int, db=Depends(get_db)):
    logger.debug(f"GET /products/{product_id}/category called")
    product = crud.get_product(db, product_id)
    if not product:
        logger.warning(f"Product not found: {product_id}")
        raise HTTPException(status_code=404, detail="Product not found")
    category = product.category
    if not category:
        logger.warning(f"Category not found: {product.category_id}")
        raise HTTPException(status_code=404, detail="Category not found")
    logger.info(f"Product {product_id} belongs to category {category.id}")
    return category

@app.get("/products/category/{category_id}/precio/{unit_price_cents}")
def get_category_products_under_price(category_id: int, unit_price_cents: int, db=Depends(get_db)):
    logger.debug(f"GET /products/category/{category_id}/precio/{unit_price_cents} called")
    category = crud.get_category(db, category_id)
    if not category:
        logger.warning(f"Category not found: {category_id}")
        raise HTTPException(status_code=404, detail="Category not found")
    products = category.products
    products_sol = []
    for product in products:
        if product.unit_price_cents < unit_price_cents:
            products_sol.append(product)
      
    logger.info(f"Products found {len(products_sol)} belongs to category {category.name} and price lower than {unit_price_cents}")
    return products_sol

@app.get("/products_promoted_categories")
def get_promoted_categories(db=Depends(get_db)):
    logger.debug(f"GET /products_promoted_categories called")
    products_category_promoted = crud.list_products_category_promoted(db)
    if not products_category_promoted:
        raise HTTPException(status_code=404, detail="No promoted products found")
    logger.info(f"Promoted products found: {len(products_category_promoted)}")
    return products_category_promoted
