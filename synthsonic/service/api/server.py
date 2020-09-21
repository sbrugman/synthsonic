from api.synthesis import get_model, get_data
from fastapi import FastAPI, File
from starlette.responses import Response

model = get_model()

app = FastAPI(title="Synthsonic - synthetic data generator service",
              description='''Obtain synthetic, safely shareable and indistinguishable-from-real synthetic data.''',
              version="0.1.0",
              )


@app.post("/synthesize")
def get_synthetic_data(file: bytes = File(...), rows: int = 100):
    synthetic_data = get_data(model, file, rows + 1)

    return Response(synthetic_data, media_type="text/csv")
