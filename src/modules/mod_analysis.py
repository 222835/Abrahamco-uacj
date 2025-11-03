from src.data_manager import get_account

# --- Funciones de Cálculo para Reportes (HU 4.1, 4.2, 4.3) ---

def get_total_income(account_id):
    """HU 4.1: Suma solo las transacciones positivas (ingresos)."""
    # El equipo debe implementar la lógica para iterar y sumar los montos > 0
    pass

def get_total_expenses(account_id):
    """HU 4.2: Suma solo las transacciones negativas (gastos). Retorna un valor positivo."""
    # El equipo debe implementar la lógica para iterar, sumar los montos < 0 y multiplicar por -1
    pass

def count_transactions(account_id):
    """HU 4.3: Devuelve el número total de transacciones."""
    # El equipo debe implementar la lógica para contar los ítems en 'transactions'
    pass

# --- Función de Soporte para core_logic (HU 4.4) ---

def check_low_balance_warning(new_balance):
    """
    HU 4.4: Verifica si el nuevo balance está entre $0.01 y $10.00.
    Si se cumple, debe retornar un string de advertencia; de lo contrario, retornar None.
    """
    # El equipo debe implementar la lógica de la advertencia.
    pass

if __name__ == '__main__':
    # Zona de prueba para el equipo 4
    pass
