from typing import Optional
from src.data_manager import get_account


def get_total_income(account_id: str) -> float:
    """HU 4.1: Suma solo las transacciones positivas (ingresos)."""
    pass


def get_total_expenses(account_id: str) -> float:
    """HU 4.2: Suma solo las transacciones negativas (gastos). Retorna un valor positivo."""
    account = get_account(account_id)
    
    if account is None:
        return 0.0
    
    total_expenses = 0.0
    
    for transaction in account.get("transactions", []):
        amount = transaction.get("amount", 0.0)
        if amount < 0:
            total_expenses += abs(amount)
    
    return total_expenses


def count_transactions(account_id: str) -> int:
    """HU 4.3: Devuelve el número total de transacciones."""
    pass


def check_low_balance_warning(new_balance: float) -> Optional[str]:
    """
    HU 4.4: Verifica si el nuevo balance está entre $0.01 y $10.00.
    Retorna el mensaje de advertencia si se cumple, None si no. Llamada por core_logic.
    """
    pass
