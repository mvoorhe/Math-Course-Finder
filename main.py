from fastapi import FastAPI, HTTPException
from scraper import Math



app = FastAPI()
mathClasses = Math()


@app.get("/{mclass}/{professor}/{weekday}")
async def read_item(mclass, professor, weekday):
    return mathClasses.findclass(mclass, professor, weekday)



