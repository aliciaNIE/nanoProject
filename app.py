from re import template
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app=Flask( __name__ )
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://yongxingnie:@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class todoapps(db.Model):
      __tablename__='todos'
      id=db.Column(db.Integer, primary_key=True)
      description=db.Column(db.String(), nullable=False)

      def __init__(self,description):
          self.description=description

      def __repr__(self):
            return f'<todoapps {self.id} {self.description}>'

db.create_all()

@app.route('/TODOAPP/create', methods=['POST'])
def create_todo():
      input_= request.get_json()['description']
      todo = todoapps(description=input_)
      db.session.add(todo)
      db.session.commit()
      return jsonify({
            'description':todo.description
      })


@app.route('/')
def index():
      return render_template('index.html', data=todoapps.query.all())

