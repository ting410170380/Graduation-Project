from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)

app.config["SECRET_KEY"] = "d3y23udh2noidmp2o"

#定義表單類型
class RegisterForm(FlaskForm):
    """自定義註冊表單類型"""
    user_name = StringField(label="用戶名", validators=[DataRequired("用戶名不可為空")])
    password = PasswordField(label="密碼", validators=[DataRequired("密碼不能為空")])
    password2 = PasswordField(label="確認密碼", validators=[DataRequired("確認密碼不能為空"),
                                                        EqualTo("password","再次密碼不一致")])
    submit = SubmitField(label="提交")


@app.route("/", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        uname = form.user_name.data
        pwd = form.password.data
        pwd2 = form.password2.data
        print(uname, pwd, pwd2)
        with open('example.txt', 'w', encoding='utf-8') as f:
            f.write(uname+'\n'+pwd+'\n'+pwd2)
        session["user_name"] = uname
        return redirect(url_for("index"))

    return render_template("a.html", form=form)

@app.route("/index")
def index():
    username = session.get("user_name")
    return "hello %s" % username


if __name__ == '__main__':
    app.run(debug=True)