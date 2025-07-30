from pysatl_knowledge.services.auth_service import AuthService
from pysatl_knowledge.services.critical_value_service import CriticalValuesService


def get_cv_service() -> CriticalValuesService:
    return CriticalValuesService()


def get_auth_service() -> AuthService:
    return AuthService()
