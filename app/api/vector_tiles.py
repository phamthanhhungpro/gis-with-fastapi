from starlette.responses import Response
from app.utils.utils import tile2bbox
from app.utils import mvt_helper
from sqlalchemy.orm.session import Session
from app.database.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter()


@router.get("/{z}/{x}/{y}.pbf")
async def get_mvt(*, db: Session = Depends(get_db), z: int, x: int, y: int, geoCol: str, layername: str):

    bbox = tile2bbox(z, x, y)
    get_column_array = mvt_helper.get_column_array(db, layername, geoCol)

    sql = ("SELECT ST_AsMVT(mvtgeom.*) as bindata FROM(SELECT ST_AsMVTGeom(" + geoCol + ", ST_MakeEnvelope(" + bbox + ", 4326)) AS geom" + get_column_array + " FROM " + layername
    + " WHERE ST_Intersects(geom,  ST_MakeEnvelope(" + bbox + "))"
    + ") mvtgeom")

    query = db.execute(sql)
    for row in query:
        content = bytes(row["bindata"])
        return Response(content,media_type = "application/protobuf")

    return Response()
