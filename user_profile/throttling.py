from rest_framework.throttling import UserRateThrottle

class PinRateThrottle(UserRateThrottle):
    scope = 'pin'
