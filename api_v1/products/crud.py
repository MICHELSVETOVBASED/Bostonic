from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from sqlalchemy.engine import Result
from sqlalchemy import select


async def get_products(session: AsyncSession) -> [Product]:
    smtn = select(Product).order_by(Product.id)
    result: Result = await session.execute(smtn)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_id: ProductCreate) -> Product:
    product = Product(**product_id.model_dump())
    session.add(product)
    await session.commit()


#######4+ěč+č
