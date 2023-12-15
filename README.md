# DSFAdminLTE
Proyecto desarrollado para la materia desarrollo de software 1, para la Universidad del Valle 2-2023
Para instalar dependencias usar "python -m pip install -r requirements.txt"
Tutorial de instalacion: https://www.youtube.com/watch?v=vndGHvTkeGg
Repositorio original: https://github.com/colorlibhq/AdminLTE
Para correr el localhost usar comando "py manage.py runserver" (windows) / "python3 manage.py runserver" (linux)
Para generar el startapp "py manage.py startapp 'exampleName'" (windows) / "python3 manage.py startapp 'exampleName'" (linux) ////no hay que hacerlo
Crear un entorno virtual PYTHON Y DARLE UN NOMBRE
.\ElNombreDeMiEntorno\Scripts\activate   <---------- activa el entorno virtual
py -m pip install -r requirements.txt  <------ isntala los paquetes necesarios en el entorno virutal
Para instalar el postgres "pip install psycopg2" 
Para generar los models.py "py manage.py inspectdb > adminlte/models.py" (tener cuidado con el UTF-8) //////////// NO HAY QUE HACERLO
Para migrar "py manage.py makemigrations", luego "py manage.py migrate"
Para usar el shell de django "py manage.py shell"
from adminlte.models import Vendedor  
jefe_taller = Vendedor.objects.get(id_vendedor='VEN0001')
jefe_taller.pass_field = '123facil123'
jefe_taller.save()
