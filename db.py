from tortoise import Tortoise


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['app.models']}
    )
    try:
        await Tortoise.generate_schemas()
    except:
        print("Schemas already exist!")
