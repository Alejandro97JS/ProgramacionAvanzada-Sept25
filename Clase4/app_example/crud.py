from sqlalchemy.orm import Session
from sqlalchemy import select
import models, schemas
import logging

logger = logging.getLogger("ecommerce")

def create_product(db: Session, data: schemas.ProductCreate) -> models.Product:
    logger.debug(f"[crud] Creando producto: {data}")
    product = models.Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    logger.info(f"[crud] Producto creado: {product.id} - {product.name}")
    return product

def list_products(db: Session) -> list[models.Product]:
    logger.debug("[crud] Listando productos")
    products = db.execute(select(models.Product).order_by(
        models.Product.id.desc())).scalars().all()
    logger.info(f"[crud] Se encontraron {len(products)} productos")
    return products

def get_product(db: Session, product_id: int) -> models.Product | None:
    logger.debug(f"[crud] Buscando producto id={product_id}")
    product = db.get(models.Product, product_id)
    if product:
        logger.info(f"[crud] Producto encontrado: {product.id} - {product.name}")
    else:
        logger.warning(f"[crud] Producto no encontrado: {product_id}")
    return product

def update_product(db: Session, product_id: int, 
                   patch: schemas.ProductUpdate) -> models.Product | None:
    logger.debug(f"[crud] Actualizando producto id={product_id} con {patch}")
    product = db.get(models.Product, product_id)
    if not product:
        logger.warning(f"[crud] Producto a actualizar no encontrado: {product_id}")
        return None
    for field, value in patch.model_dump(exclude_unset=True).items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    logger.info(f"[crud] Producto actualizado: {product.id} - {product.name}")
    return product

def delete_product(db: Session, product_id: int) -> bool:
    logger.debug(f"[crud] Eliminando producto id={product_id}")
    product = db.get(models.Product, product_id)
    if not product:
        logger.warning(f"[crud] Producto a eliminar no encontrado: {product_id}")
        return False
    db.delete(product)
    db.commit()
    logger.info(f"[crud] Producto eliminado: {product_id}")
    return True

def list_products_category_promoted(db: Session) -> list[models.Product]:
    logger.debug(f"[crud] Buscando productos promovidos según su categoría")
    products = db.execute(select(models.Product).join(models.Category).filter(
        models.Category.is_promoted == True)).scalars().all()
    logger.info(f"[crud] Se encontraron {len(products)} productos promovidos")
    if not products:
        logger.warning(f"[crud] No hay productos con categoría promovida: {products}")
    else:
        logger.info(f"[crud] Productos promovidos: {products}")
    return products


# --- CATEGORY CRUD ---
def create_category(db: Session, data: schemas.CategoryCreate) -> models.Category:
    logger.debug(f"[crud] Creando categoría: {data}")
    category = models.Category(**data.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    logger.info(f"[crud] Categoría creada: {category.id} - {category.name}")
    return category

def list_categories(db: Session) -> list[models.Category]:
    logger.debug("[crud] Listando categorías")
    categories = db.execute(select(models.Category).order_by(
        models.Category.id.desc())).scalars().all()
    logger.info(f"[crud] Se encontraron {len(categories)} categorías")
    return categories

def get_category(db: Session, category_id: int) -> models.Category | None:
    logger.debug(f"[crud] Buscando categoría id={category_id}")
    category = db.get(models.Category, category_id)
    if category:
        logger.info(f"[crud] Categoría encontrada: {category.id} - {category.name}")
    else:
        logger.warning(f"[crud] Categoría no encontrada: {category_id}")
    return category

def update_category(db: Session, category_id: int, patch: schemas.CategoryUpdate) -> models.Category | None:
    logger.debug(f"[crud] Actualizando categoría id={category_id} con {patch}")
    category = db.get(models.Category, category_id)
    if not category:
        logger.warning(f"[crud] Categoría a actualizar no encontrada: {category_id}")
        return None
    for field, value in patch.model_dump(exclude_unset=True).items():
        setattr(category, field, value)
    db.commit()
    db.refresh(category)
    logger.info(f"[crud] Categoría actualizada: {category.id} - {category.name}")
    return category

def delete_category(db: Session, category_id: int) -> bool:
    logger.debug(f"[crud] Eliminando categoría id={category_id}")
    category = db.get(models.Category, category_id)
    if not category:
        logger.warning(f"[crud] Categoría a eliminar no encontrada: {category_id}")
        return False
    db.delete(category)
    db.commit()
    logger.info(f"[crud] Categoría eliminada: {category_id}")
    return True
