import mongoengine

# from src.infrastructure.redis_caching import cache_rules
# from infrastructure.redis_caching import RedisCaching
from infrastructure.redis_caching_backup_3 import cache_rules


def create_db_connection():
    mongoengine.register_connection('core', 'credit-scoring')


def launch_app():
    create_db_connection()
    print("credit-scoring mongodb connection is established.")
    cache_rules()


if __name__ == '__main__':
    launch_app()
