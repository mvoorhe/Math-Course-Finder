from fastapi import FastAPI
from scraper import Math


app = FastAPI()
mathClasses = Math()


@app.get("/{maclass}/{professor}/{weekday}")
async def read_item(maclass, professor, weekday):
    return mathClasses.findclass(maclass, professor, weekday)



