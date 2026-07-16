<p align="center">
  <img width="600" height="265" alt="django-rest-framework" src="https://github.com/user-attachments/assets/5f001f1c-0e9d-43bf-9133-f32ede7024db" />
</p>

#

1. Clonar repo
2. Generar el ambiente virtual con `python -m venv {nombre_de_tu_ambiente}`
3. Correr el ambiente virtual con `.\{nombre_virtual}\Scripts\activate` (las rutas pueden variar según el OS)
4. `pip install requirements.txt`
5. Clonar el archivo `.env.template` y ponerle el nombre de `.env`
6. Cambiar las variables de entorno por las tuyas

### En caso de querer correr la app en Docker
1. Ejecutar `docker compose up`
2. Ejecutar `docker compose build`
3. Ejecutar el siguiente comando dentro de la instancia web de Django dentro de <span style="color:blue">Docker</span>
```
ptyhon manage.py import_products
```

Estos pasos levantarán la y llenarán BD de información y a su vez lenvantará el servidor web de Django dentro de <span style="color:blue">Docker</span>
