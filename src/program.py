import mongoengine


# from src.infrastructure.redis_caching import cache_rules
# from infrastructure.redis_caching import RedisCaching
# from infrastructure.caching.redis_caching import cache_rules


def create_db_connection():
    mongoengine.register_connection('core', 'scoring-engine')


def launch_app():
    create_db_connection()
    print("credit-scoring mongodb connection is established.")
    # RedisCaching().cache_rules()


if __name__ == '__main__':
    launch_app()
