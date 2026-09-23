from models import Order
import requests

def create_order(user_id, amount, notifier, logger, db, user_repository):
    # TODO: obtener el email desde el repositorio
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    email = requests.get(url)

    if email.status_code == 200:
        # Convertir la respuesta a un diccionario de Python
        datos = email.json()
        
        # Extraer el email del diccionario
        email = datos.get("email")
        print(f"El correo es: {email}")
    else:
        print(f'No se pudo crear la orden: No se encuentra el Email del usuario {user_id}')
   
   # TODO: validar que amount sea positivo, de lo contrario lanzar el error "Invalid amount"
    if amount > 0:
        order = Order(user_email=email, amount=amount, status='CREATED')
    else:
        print(f"invalid Amount")
    
    # TODO: persistir la orden
    db.add(order)
    db.commit()
    
    notifier.send(email, 'Order created')
    return order
