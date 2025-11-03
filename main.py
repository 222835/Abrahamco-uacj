# =================================================================
# === INSTRUCCIÓN PARA EL EQUIPO: SOLO DESCOMENTAR TU SECCIÓN ===
# =================================================================

# Importaciones de módulos centrales (Usados por todos)
from src.data_manager import load_accounts, save_accounts, get_account
from src.core_logic import update_balance

# -----------------------------------------------------------------
# 📌 EQUIPO 1: Proceso de Onboarding Digital
# -----------------------------------------------------------------
# from src.modules.mod_onboarding import create_new_account, toggle_account_status, check_status

# if __name__ == "__main__":
#     print("--- 📌 Equipo 1: Pruebas de Onboarding ---")
#
#     # HU 1.1 y 1.2: Probar la creación (Validación de nombre y depósito mínimo)
#     print("\nProbando creación de cuenta...")
#     new_id = create_new_account("Nuevo Cliente", 60.00)
#     new_acc = get_account(new_id)
#     print(f"Cuenta {new_id} creada: {new_acc['owner']}")
#
#     # HU 1.3: Probar cambio de estado (toggle_account_status)
#     print("Cambiando estado...")
#     toggle_account_status(new_id)
#
#     # HU 1.4: Probar verificación de estado (check_status)
#     print(f"Estado de {new_id}: {'ACTIVA' if check_status(new_id) else 'INACTIVA'}")
#
#     print("------------------------------------------")


# -----------------------------------------------------------------
# 📌 EQUIPO 2: Transferencias Interbancarias Rápidas
# -----------------------------------------------------------------
# El Equipo 2 prueba directamente la función update_balance después de modificarla en core_logic.py
# (No necesita importar funciones de su propio módulo, solo probar las modificaciones hechas a core_logic.py)

# if __name__ == "__main__":
#     print("--- 📌 Equipo 2: Pruebas de Transferencias ---")
#     # Usaremos la cuenta A1001 (balance inicial: 1500.50)
#     ACCOUNT_ID = "A1001"
#
#     # HU 2.1 y 2.4: Probar límite y comisión (retiro de 1100.00)
#     print("\nProbando retiro con límites y comisiones (debería fallar por límite o aplicar comisión si es >= 500)...")
#     status, msg = update_balance(ACCOUNT_ID, -1100.00, "Retiro grande")
#     print(f"Estado: {status}, Mensaje: {msg}")
#
#     # HU 2.3: Probar fecha dinámica (cualquier transacción exitosa)
#     print("\nProbando transacción exitosa (verificar fecha en JSON)...")
#     status, msg = update_balance(ACCOUNT_ID, -10.00, "Pequeño pago")
#     print(f"Estado: {status}, Mensaje: {msg}")
#
#     # HU 2.2: Probar registro de error por fondos insuficientes (si balance es bajo)
#     print("\nProbando fondos insuficientes (debería fallar)...")
#     status, msg = update_balance(ACCOUNT_ID, -50000.00, "Retiro imposible")
#     print(f"Estado: {status}, Mensaje: {msg}")
#
#     print("------------------------------------------")


# -----------------------------------------------------------------
# 📌 EQUIPO 3: Gestión de Tarjetas Virtuales
# -----------------------------------------------------------------
# from src.modules.mod_cards import freeze_card, unfreeze_card, is_card_frozen

# if __name__ == "__main__":
#     print("--- 📌 Equipo 3: Pruebas de Tarjetas Virtuales ---")
#     ACCOUNT_ID = "A1001"

#     # HU 3.3: Congelar tarjeta
#     freeze_card(ACCOUNT_ID)
#     acc_info = get_account(ACCOUNT_ID)
#     print(f"Estado después de congelar: {acc_info['virtual_card_status']}")

#     # HU 3.2: Probar Bloqueo de Transacción (debería fallar)
#     print("\nIntentando transacción con tarjeta congelada (debería fallar)...")
#     status, msg = update_balance(ACCOUNT_ID, -50.00, "Pago de prueba")
#     print(f"Estado de Transacción: {status}, Mensaje: {msg}")

#     # HU 3.4: Descongelar tarjeta
#     unfreeze_card(ACCOUNT_ID)
#     acc_info = get_account(ACCOUNT_ID)
#     print(f"Estado después de descongelar: {acc_info['virtual_card_status']}")

#     # Probar que la transacción ahora funcione
#     print("\nIntentando transacción con tarjeta activa (debería funcionar)...")
#     status, msg = update_balance(ACCOUNT_ID, -10.00, "Pago final")
#     print(f"Estado de Transacción: {status}, Mensaje: {msg}")
#
#     print("------------------------------------------")


# -----------------------------------------------------------------
# 📌 EQUIPO 4: Visualización y Análisis de Gastos
# -----------------------------------------------------------------
# from src.modules.mod_analysis import get_total_income, get_total_expenses, count_transactions

# if __name__ == "__main__":
#     print("--- 📌 Equipo 4: Pruebas de Análisis de Gastos ---")
#     ACCOUNT_ID = "A1001"
#
#     # Las transacciones deben estar en el JSON
#
#     # HU 4.3: Conteo de Transacciones
#     count = count_transactions(ACCOUNT_ID)
#     print(f"\nTotal de transacciones: {count}")

#     # HU 4.1: Sumar Ingresos
#     income = get_total_income(ACCOUNT_ID)
#     print(f"Total Ingresos: {income}")

#     # HU 4.2: Sumar Gastos
#     expenses = get_total_expenses(ACCOUNT_ID)
#     print(f"Total Gastos: {expenses}")

#     # HU 4.4: Alerta de Sobregiro (Requiere que el Equipo 2 ya haya implementado 4.4 en core_logic)
#     print("\nProbando alerta de sobregiro (Balance final < 10.00)...")
#     # Ajustar la cantidad para que el balance final quede entre 0 y 10
#     status, msg = update_balance(ACCOUNT_ID, -1495.00, "Retiro crítico")
#     print(f"Mensaje de Transacción (Buscar Alerta): {msg}")
#
#     print("------------------------------------------")


# -----------------------------------------------------------------
# 📌 EQUIPO 5: Módulo de Contacto y Soporte por Chat
# -----------------------------------------------------------------
# from src.modules.mod_support import log_incident, get_incident_history

# if __name__ == "__main__":
#     print("--- 📌 Equipo 5: Pruebas de Soporte y Chat ---")
#     ACCOUNT_ID = "B2002"

#     # HU 5.2 y 5.4: Registrar Incidentes con prioridad
#     print("\nRegistrando incidentes...")
#     log_incident(ACCOUNT_ID, "No puedo ingresar a la aplicación", priority="ALTA")
#     log_incident(ACCOUNT_ID, "Consulta sobre extracto bancario")

#     # HU 5.3: Visualización de Historial
#     history = get_incident_history(ACCOUNT_ID)
#     print(f"\nHistorial de incidentes para {ACCOUNT_ID} (total {len(history)}):")
#     for i, inc in enumerate(history):
#         print(f"  {i+1}. {inc.get('description')} - Prioridad: {inc.get('priority')}")

#     print("------------------------------------------")


# -----------------------------------------------------------------
# 📌 EQUIPO 6: Metas de Ahorro Programadas
# -----------------------------------------------------------------
# from src.modules.mod_savings import deposit_to_goal, check_goal_achieved

# if __name__ == "__main__":
#     print("--- 📌 Equipo 6: Pruebas de Metas de Ahorro ---")
#     ACCOUNT_ID = "A1001"

#     # HU 6.1: (Asumir estructura de goal ya creada por mod_onboarding)
#
#     # HU 6.2: Depósito a la meta (usa update_balance internamente)
#     print("\nDepositando $100.00 a la meta...")
#     deposit_to_goal(ACCOUNT_ID, 100.00)
#     acc = get_account(ACCOUNT_ID)
#     print(f"Balance actual: {acc['balance']}, Meta actual: {acc['savings_goal']['current']}")

#     # HU 6.3: Verificar logro de meta (target 0.00 por defecto, debería ser True si current > 0)
#     is_achieved = check_goal_achieved(ACCOUNT_ID)
#     print(f"Meta lograda?: {is_achieved}")

#     # HU 6.4: Probar Requisito de Retiro (Bloqueo si balance cae por debajo de $50)
#     print("\nProbando retiro que dejaría el balance bajo $50 (debería fallar)...")
#     # Asumiendo que el balance es 1400.50 y el retiro es 1351.00 (deja 49.50)
#     status, msg = update_balance(ACCOUNT_ID, -1351.00, "Retiro riesgoso")
#     print(f"Estado de Transacción: {status}, Mensaje: {msg}")

#     print("------------------------------------------")
