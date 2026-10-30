# --- Extract Constant: Evitar números mágicos ---
DESCUENTO_VIP = 0.80
DESCUENTO_ESTUDIANTE = 0.85
DESCUENTO_MAYORISTA = 0.70

UMBRAL_DISTANCIA_ALTA = 100
DESCUENTO_DISTANCIA_ALTA = 5.0

UMBRAL_DISTANCIA_MEDIA = 50
DESCUENTO_DISTANCIA_MEDIA = 2.0


# --- Extract Method: Funciones secundarias auxiliares ---
def calcular_subtotal(lista_productos):
    """Calcula el subtotal multiplicando precio por cantidad de cada producto."""
    subtotal = 0.0
    for precio, cantidad in lista_productos:
        subtotal += precio * cantidad
    return subtotal


def aplicar_descuento_cliente(monto, tipo_cliente):
    """Aplica el porcentaje de descuento segun el tipo de cliente."""
    if tipo_cliente == "vip":
        return monto * DESCUENTO_VIP
    elif tipo_cliente == "est":
        return monto * DESCUENTO_ESTUDIANTE
    elif tipo_cliente == "may":
        return monto * DESCUENTO_MAYORISTA
    return monto


def aplicar_descuento_distancia(monto, distancia_km):
    """Aplica un descuento fijo basado en la distancia de envio."""
    if distancia_km > UMBRAL_DISTANCIA_ALTA:
        return monto - DESCUENTO_DISTANCIA_ALTA
    elif distancia_km > UMBRAL_DISTANCIA_MEDIA:
        return monto - DESCUENTO_DISTANCIA_MEDIA
    return monto


# --- Función Principal Refactorizada (Renaming: de proc a procesar_total_compra) ---
def procesar_total_compra(lista_productos, tipo_cliente, distancia_km):
    """Calcula el monto total final de la compra coordinando los descuentos."""
    subtotal = calcular_subtotal(lista_productos)
    monto_con_descuento_cliente = aplicar_descuento_cliente(subtotal, tipo_cliente)
    total_final = aplicar_descuento_distancia(monto_con_descuento_cliente, distancia_km)

    return max(0.0, total_final)