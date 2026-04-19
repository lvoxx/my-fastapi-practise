from wireup import injectable

@injectable
class DatabaseConfig:
    def __init__(self):
        self.host = "localhost"
        self.port = 5432
        self.username = "postgres"
        self.password = "password"
        
    def query(self, sql: str):
        # Simulate a database query
        print(f"Executing query on {self.host}:{self.port} as {self.username}: {sql}")
        
@injectable
class UserService:
    def __init__(self, db_config: DatabaseConfig):
        self.db_config = db_config
        
    def get_user(self, user_id: int):
        # Simulate fetching a user from the database
        self.db_config.query(f"SELECT * FROM users WHERE id = {user_id}")
        return {"id": user_id, "name": "John Doe"}