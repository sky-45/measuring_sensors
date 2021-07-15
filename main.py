#importing modules
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
import pandas as pd
from fastapi.responses import FileResponse
import random
from img_process import *

measurement_adc = [{"sensor":"ADC", "datetime":"14/07/2021 11:15:10", "value": 5},
                  {"sensor":"ADC", "datetime":"14/07/2021 11:17:10", "value": 2},
                  {"sensor":"ADC", "datetime":"14/07/2021 11:19:10", "value": 4},
                  {"sensor":"ADC", "datetime":"14/07/2021 11:20:10", "value": 6},
                  {"sensor":"ADC", "datetime":"14/07/2021 11:21:10", "value": 4},
                  {"sensor":"ADC", "datetime":"14/07/2021 11:22:10", "value": 7}
                  ]
for k in range(1,600):
    temp = {"sensor":"ADC", "datetime":"14/07/2021 11:{}:{}".format(k%50, random.randint(2, 55)), "value": 5+random.random()}
    measurement_adc.append(temp)

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
    measurement_adc.append({"sensor":item.sensor, "datetime":day+' '+hour, "value": item.value_measured_mem})
    return item

@app.get("/temperature/{last_num}")   #temperature
async def fig_temp(last_num:int):
    pth_img=get_plt_sensor("ADC", last_num, measurement_adc)
    return FileResponse(pth_img)


