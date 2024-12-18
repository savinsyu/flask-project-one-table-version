from flask import Blueprint, redirect, url_for, render_template, request, flash

from modules import connect

bp = Blueprint('add', __name__)


@bp.route("/add", methods=["GET", "POST"])
def add_bash_command():
    if request.method == "POST":
        new_bash_command = request.form["bash_command"]
        new_bash_name = request.form["bash_name"]

        if len(request.form['bash_command']) > 1 and len(request.form['bash_name']) > 10:
            conn = connect.get_db_connection()
            conn.execute(
                "INSERT INTO bash (bash_command, bash_name) VALUES (?, ?)",
                (new_bash_command, new_bash_name)
            )
            conn.commit()
            conn.close()
            if not new_bash_command:
                flash('Ошибка сохранения записи, вы ввели мало символов!', category='danger')
            else:
                flash('Запись успешно добавлена!', category='success')
            # В случае соблюдения условий заполнения полей, произойдёт перенаправление
            return redirect(url_for("bash_list_commands.bash_list_commands"))

        else:
            flash('Ошибка сохранения записи, вы ввели мало символов!', category='danger')

    return render_template("bash/add_bash_command.html")
