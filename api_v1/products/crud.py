from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from sqlalchemy.engine import Result
from sqlalchemy import select

from .schemas import ProductCreate, ProductUpdate, ProductUpdatePartial


async def get_products(session: AsyncSession) -> [Product]:
    smtn = select(Product).order_by(Product.id)
    result: Result = await session.execute(smtn)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)

    return product


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductUpdate | ProductUpdatePartial,
    partial: bool = False,
) -> Product:
    print(
        f"Updating product {product.id} with data: {product_update.model_dump(exclude_unset=partial)}"
    )
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
        print(f"Set {name} = {value}")
    await session.commit()
    await session.refresh(product)
    print(f"Product updated: {product.name}, {product.description}, {product.price}")
    return product


# async def update_product_partial(
#         session: AsyncSession,
#         product: Product,
#         product_update: ProductUpdatePartial,
#
# ) -> Product:
#     for name, value in  product_update.model_dump(exclude_unset=True).items():
#         setattr(product, name, value)
#     await session.commit()
#     return product


async def delete_product(
    session: AsyncSession,
    product: Product,
) -> None:
    await session.delete(product)
    await session.commit()
