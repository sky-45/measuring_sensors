#importing modules
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
import pandas as pd

measurement_adc = [{"sensor":"ADC", "date":"14/07/2021", "time":"11:15:10", "value": 15}]
df = pd.DataFrame(measurement_adc)
class Item(BaseModel):
    sensor: str
    value_measured_mem: int

app = FastAPI()

@app.get("/")
async def root():
    #return df.to_dict("index")
    return measurement_adc

@app.post("/post_data")
async def post_data(item: Item):
    now = datetime.now()
    day = now.strftime("%d/%m/%Y")
    hour = now.strftime("%H:%M:%S")
    #df_temp = pd.DataFrame([{"sensor":item.sensor, "date":day, "time":hour, "value": item.value_measured_mem}])
    #df.append(df_temp, ignore_index = True)
    measurement_adc.append({"sensor":item.sensor, "date":day, "time":hour, "value": item.value_measured_mem})
    #return item

@app.get("/aclr")   #acelerometro
async def root():
    return measurement_adc

@app.get("/temperature")   #temperature
async def root():
    return measurement_adc


