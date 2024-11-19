import pymysql
from dbconfig import getDBConnection
from flask import Flask, redirect, render_template, request, url_for

from app import app


@app.route("/", methods=["GET"])
def index():
    connection = getDBConnection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT * FROM personas")
        personas = cursor.fetchall()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        personas = []
    finally:
        cursor.close()
        connection.close()

    return render_template("frm.html", personas=personas)


@app.route("/", methods=["POST"])
def submit():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]

    connection = getDBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO personas (nombre, apellido) VALUES (%s,%s)", (nombre, apellido)
        )
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for("index"))


# Ruta para cargar el formulario de edición
@app.route("/edit/<int:id>", methods=["GET"])
def edit(id):
    connection = getDBConnection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT * FROM personas WHERE id = %s", (id,))
        persona = cursor.fetchone()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        persona = None
    finally:
        cursor.close()
        connection.close()

    return render_template("edit_frm.html", persona=persona)


# Ruta para actualizar un registro en la base de datos
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]

    connection = getDBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "UPDATE personas SET nombre = %s, apellido = %s WHERE id = %s",
            (nombre, apellido, id),
        )
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for("index"))


# Ruta para eliminar un registro en la base de datos
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    connection = getDBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM personas WHERE id = %s", (id,))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
