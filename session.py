import redis
import settings as settings

redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.SESSION_REDIS_DB)


def get_session_value(session_id):
    redis_key = "image.captcha:{0}".format(session_id)
    redis_value = redis_client.get(redis_key)
    return redis_value


def get_captcha(session_id):
    return get_session_value(session_id)
