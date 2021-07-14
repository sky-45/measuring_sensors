#importing modules
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel



measurement_adc = {"ADC":{"14/07/2021":{"11:15:10":15}}}
class Item(BaseModel):
    sensor: str
    value_measured_mem: int


app = FastAPI()

@app.get("/")
async def root():
    return {"message": measurement_adc}

@app.post("/post_data")
async def post_data(item: Item):
    now = datetime.now()
    day = now.strftime("%d/%m/%Y")
    hour = now.strftime("%H:%M:%S")
    measurement_adc[item.sensor][day][hour] = item.value_measured_mem
    return item

