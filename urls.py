class Urls:
    BASE_URL = "https://qa-stellarburgers.education-services.ru"
    MAIN_PAGE = f"{BASE_URL}/"
    LOGIN_PAGE = f"{BASE_URL}/login"
    REGISTER_PAGE = f"{BASE_URL}/register"
    FORGOT_PASSWORD_PAGE = f"{BASE_URL}/forgot-password"
    RESET_PASSWORD_PAGE = f"{BASE_URL}/reset-password"
    PROFILE_PAGE = f"{BASE_URL}/account/profile"
    ORDER_HISTORY_PAGE = f"{BASE_URL}/account/order-history"
    FEED_PAGE = f"{BASE_URL}/feed"

    API_REGISTER = "/api/auth/register"
    API_LOGIN = "/api/auth/login"
    API_USER = "/api/auth/user"