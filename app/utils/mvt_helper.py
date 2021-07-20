from sqlalchemy.orm.session import Session

def get_column_array(db: Session, tablename:str, geoCol: str):

    result = " "
    sql = "select column_name from information_schema.columns where table_name = '" + tablename + "'; "
    query = db.execute(sql)
    for row in query:
        if(str(row["column_name"]) != geoCol):
            result = result + "," + str(row["column_name"])

    return result