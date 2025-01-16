from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Record

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    records = Record.query.all()
    return render_template('read.html', records=records)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_record = Record(name=request.form['name'], description=request.form['description'])
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create.html')

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    record = Record.query.get_or_404(id)
    if request.method == 'POST':
        record.name = request.form['name']
        record.description = request.form['description']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('update.html', record=record)

@bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    record = Record.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(record)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('delete.html', record=record)