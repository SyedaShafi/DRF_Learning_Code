from rest_framework.throttling import UserRateThrottle


class CRUDThrottleRate(UserRateThrottle):
    scope = 'student'






