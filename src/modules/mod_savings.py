from src.data_manager import load_accounts, save_accounts, get_account
# Importar la función update_balance del core_logic para la HU 6.2
# from src.core_logic import update_balance as core_update_balance

def deposit_to_goal(account_id, amount):
    """
    HU 6.2: Mueve dinero del balance principal al 'savings_goal.current'.
    Debe usar la función update_balance para restar el monto del balance principal.
    """
    # El equipo debe implementar la lógica para llamar a update_balance (resta)
    # y luego actualizar el campo 'savings_goal.current' (suma).
    pass


def check_goal_achieved(account_id):
    """HU 6.3: Devuelve True si el ahorro actual es >= el objetivo."""
    # El equipo debe obtener los valores 'current' y 'target' de 'savings_goal' y compararlos.
    pass

# --- Función de Soporte para core_logic (HU 6.4) ---

def check_minimum_balance_rule(new_balance):
    """
    HU 6.4: Verifica si el nuevo balance cumple con la regla de mínimo $50.00 después de un retiro.
    Debe retornar (True, "") si es válido o (False, "mensaje de error") si falla.
    """
    # El equipo debe implementar la lógica para verificar si new_balance es menor a $50.00.
    pass

if __name__ == '__main__':
    # Zona de prueba para el equipo 6
    pass
