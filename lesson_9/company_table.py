from sqlalchemy import create_engine, text, inspect
from sqlalchemy.sql import Engine


class CompanyTable:
    __scripts = {
        "select": text("SELECT * FROM company WHERE deleted_at IS NULL"),
        "select_active": text("SELECT * FROM company WHERE \"is_active\" = true AND deleted_at IS NULL"),
        "delete_by_id": text("DELETE FROM company WHERE id = :id_to_delete"),
        "insert_new": text("INSERT INTO company(\"name\", \"description\") VALUES (:new_name, :new_description)"),
        "get_max_id": text("SELECT MAX(\"id\") FROM company"),
        "select_by_id": text("SELECT * FROM company WHERE id = :select_id AND deleted_at IS NULL"),
    }

    def __init__(self, connection_string: str):

        self.__db: Engine = create_engine(connection_string, echo=False)

    def get_companies(self) -> list:
        with self.__db.connect() as conn:
            result = conn.execute(self.__scripts["select"])
            rows = result.mappings().all()
            return rows

    def get_active_companies(self) -> list:
        with self.__db.connect() as conn:
            result = conn.execute(self.__scripts["select_active"])
            rows = result.mappings().all()
            return rows

    def get_company_by_id(self, company_id: int) -> list:
        with self.__db.connect() as conn:
            result = conn.execute(
                self.__scripts["select_by_id"], {"select_id": company_id})
            rows = result.mappings().all()
            return rows

    def create_company(self, name: str, description: str = "") -> None:
        with self.__db.connect() as conn:
            with conn.begin():
                conn.execute(
                    self.__scripts["insert_new"],
                    {"new_name": name, "new_description": description}
                )

    def delete_company_by_id(self, company_id: int) -> None:
        with self.__db.connect() as conn:
            with conn.begin():
                conn.execute(self.__scripts["delete_by_id"],
                             {"id_to_delete": company_id})

    def get_max_id(self) -> int:
        with self.__db.connect() as conn:
            result = conn.execute(self.__scripts["get_max_id"])
            max_id = result.scalar()
            return max_id if max_id is not None else 0

    def get_table_names(self) -> list:

        inspector = inspect(self.__db)
        return inspector.get_table_names()
