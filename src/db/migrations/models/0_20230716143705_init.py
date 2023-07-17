from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "rate" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cargo_type" VARCHAR(5) NOT NULL  DEFAULT 'Other',
    "rate" DECIMAL(4,3) NOT NULL,
    "date" DATE NOT NULL
);
COMMENT ON COLUMN "rate"."cargo_type" IS 'glass: Glass\nother: Other';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
